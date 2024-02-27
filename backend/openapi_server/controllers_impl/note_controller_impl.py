import connexion

from openapi_server.models.note_meta_data import NoteMetaData
from openapi_server.models.note import Note
from openapi_server.db_models.note import Note as DBNote
from openapi_server.database import db

from datetime import datetime


def create_new_note_impl(note: Note):  # noqa: E501
    """put new note object

    Adds new note object to database # noqa: E501

    :param note: 
    :type note: dict | bytes

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    db_note = DBNote()
    if note.name is not None:
        db_note.name = note.name
    if note.raw_text is not None:
        db_note.raw_text = note.raw_text
    db.session.add(db_note)
    db.session.commit()
    return db_note.id, 201


def get_all_notes_impl():  # noqa: E501
    """Retrieve list of all notes

    Array of all notes # noqa: E501


    :rtype: Union[List[NoteMetaData], Tuple[List[NoteMetaData], int], Tuple[List[NoteMetaData], int, Dict[str, str]]
    """
    # sqlalchemy get all note objects
    notes = DBNote.query.all()
    # convert to NoteMetaData
    noteMetaDataList = []
    for note in notes:
        noteMetaDataList.append(NoteMetaData(
            note.id, note.created_at, note.updated_at, note.name))

    return noteMetaDataList


def get_note_by_id_impl(id):  # noqa: E501
    """Get one single note by id

    Full note object with all attributes # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    # get note by id from sqlalchemy
    note: DBNote = DBNote.query.get(id)
    # return Note(
    #    "1", datetime.now(), datetime.now(), "Note 1", "Raw", "AI")
    return Note(note.id, note.created_at, note.updated_at, note.name, note.raw_text, note.ai_output)


def update_note_by_id_impl(note_id, body):  # noqa: E501
    """Update one single note by id

    Full note object with all attributes # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str
    :param note: 
    :type note: dict | bytes

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    if body:
        patch_note = body
        # sqlalchemy get note by id
        db_note: DBNote = DBNote.query.get(note_id)
        if db_note is not None:
            # update note with new values if they are not None
            if patch_note.name is not None:
                db_note.name = patch_note.name
            if patch_note.raw_text is not None:
                db_note.raw_text = patch_note.raw_text
            db_note.updated_at = datetime.now()
            # commit changes to db
            db.session.commit()
        else:
            return "Note not found", 404
    return body
