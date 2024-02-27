import connexion
import io

from openapi_server.models.generate_response_for_raw_note_request import GenerateResponseForRawNoteRequest
from openapi_server.services.ai_service import transcribe_audio_file, apply_prompt
from openapi_server.db_models.note import Note as DBNote
from openapi_server.database import db


def generate_response_for_raw_note_impl(note_id, generate_response_for_raw_note_request: GenerateResponseForRawNoteRequest):
    """Generate an AI response based on a raw note and prompt

    raw note is taken as input # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str
    :param generate_response_for_raw_note_request: 
    :type generate_response_for_raw_note_request: dict | bytes

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    # get raw note from note_id
    db_note: DBNote = DBNote.query.get(note_id)
    raw_note = db_note.raw_note
    generated_response = apply_prompt(
        raw_note, generate_response_for_raw_note_request.prompt)
    db_note.ai_output = generated_response
    # save
    db.session.commit()
    return generated_response


def transcribe_audio_for_note_impl(note_id, file=None):
    """Transcribe an audio file

    Take an audio file and transcribe it, so we have a textual representation of its content # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str
    :param file_name: 
    :type file_name: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    uploaded_audio = file.read()
    buffer = io.BytesIO(uploaded_audio)
    buffer.name = 'file.mp3'
    transcribed_audio = transcribe_audio_file(buffer)
    # update note object raw text
    db_note: DBNote = DBNote.query.get(note_id)
    if db_note.raw_text is None:
        db_note.raw_text = "" + transcribed_audio
    else:
        db_note.raw_text += '<br><br>' + transcribed_audio
    db.session.commit()
    return transcribed_audio
