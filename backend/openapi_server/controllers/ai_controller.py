import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.generate_response_for_raw_note_request import GenerateResponseForRawNoteRequest  # noqa: E501
from openapi_server import util

from openapi_server.controllers_impl import generate_response_for_raw_note_impl


def generate_response_for_raw_note(note_id, body): 
    """Generate an AI response based on a raw note and prompt

    raw note is taken as input # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str
    :param generate_response_for_raw_note_request: 
    :type generate_response_for_raw_note_request: dict | bytes

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    generate_response_for_raw_note_request = GenerateResponseForRawNoteRequest.from_dict(body)  # noqa: E501
    return generate_response_for_raw_note_impl(note_id, generate_response_for_raw_note_request)

from openapi_server.controllers_impl import transcribe_audio_for_note_impl


def transcribe_audio_for_note(note_id, file=None): 
    """Transcribe an audio file

    Take an audio file and transcribe it, so we have a textual representation of its content # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str
    :param file: 
    :type file: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return transcribe_audio_for_note_impl(note_id, file)
