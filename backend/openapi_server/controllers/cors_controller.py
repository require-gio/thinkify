import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server import util

from openapi_server.controllers_impl import ai_generate_response_cors_impl


def ai_generate_response_cors(note_id): 
    """CORS support

    Enable CORS by returning correct headers  # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return ai_generate_response_cors_impl(note_id)

from openapi_server.controllers_impl import ai_transcribe_cors_impl


def ai_transcribe_cors(note_id): 
    """CORS support

    Enable CORS by returning correct headers  # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return ai_transcribe_cors_impl(note_id)

from openapi_server.controllers_impl import new_note_cors_impl


def new_note_cors(): 
    """CORS support

    Enable CORS by returning correct headers  # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return new_note_cors_impl()

from openapi_server.controllers_impl import note_cors_impl


def note_cors(note_id): 
    """CORS support

    Enable CORS by returning correct headers  # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return note_cors_impl(note_id)
