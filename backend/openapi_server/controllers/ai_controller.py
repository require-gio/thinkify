import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.ai_response import AIResponse  # noqa: E501
from openapi_server.models.generate_response_for_raw_note_request import GenerateResponseForRawNoteRequest  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server import util

from openapi_server.controllers_impl import generate_response_for_raw_note_impl


def generate_response_for_raw_note(generate_response_for_raw_note_request):  # noqa: E501
    """Generate an AI response based on a raw note and prompt

    raw note is taken as input # noqa: E501

    :param generate_response_for_raw_note_request: 
    :type generate_response_for_raw_note_request: dict | bytes

    :rtype: Union[AIResponse, Tuple[AIResponse, int], Tuple[AIResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        generate_response_for_raw_note_request = GenerateResponseForRawNoteRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return generate_response_for_raw_note_impl(generate_response_for_raw_note_request)

from openapi_server.controllers_impl import transcribe_audio_for_note_impl


def transcribe_audio_for_note(note_id=None, file_name=None):  # noqa: E501
    """Transcribe an audio file

    Take an audio file and transcribe it, so we have a textual representation of its content # noqa: E501

    :param note_id: 
    :type note_id: str
    :param file_name: 
    :type file_name: str

    :rtype: Union[List[Note], Tuple[List[Note], int], Tuple[List[Note], int, Dict[str, str]]
    """
    return transcribe_audio_for_note_impl(note_id=None, file_name=None)
