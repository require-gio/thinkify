import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.note_meta_data import NoteMetaData  # noqa: E501
from openapi_server import util

from openapi_server.controllers_impl import create_new_note_impl


def create_new_note(body): 
    """put new note object

    Adds new note object to database # noqa: E501

    :param note: 
    :type note: dict | bytes

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    note = Note.from_dict(body)  # noqa: E501
    return create_new_note_impl(note)

from openapi_server.controllers_impl import get_all_notes_impl


def get_all_notes(): 
    """Retrieve list of all notes

    Array of all notes # noqa: E501


    :rtype: Union[List[NoteMetaData], Tuple[List[NoteMetaData], int], Tuple[List[NoteMetaData], int, Dict[str, str]]
    """
    return get_all_notes_impl()

from openapi_server.controllers_impl import get_note_by_id_impl


def get_note_by_id(note_id): 
    """Get one single note by id

    Full note object with all attributes # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    return get_note_by_id_impl(note_id)

from openapi_server.controllers_impl import update_note_by_id_impl


def update_note_by_id(note_id, body): 
    """patch note object

    Full note object with all attributes # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str
    :param note: 
    :type note: dict | bytes

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    note = Note.from_dict(body)  # noqa: E501
    return update_note_by_id_impl(note_id, note)
