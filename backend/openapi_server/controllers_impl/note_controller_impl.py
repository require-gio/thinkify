import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.note import Note  # noqa: E501
from openapi_server import util

from datetime import datetime


def get_all_notes_impl():  # noqa: E501
    """Retrieve list of all notes

    Array of all notes # noqa: E501


    :rtype: Union[List[NoteMetaData], Tuple[List[NoteMetaData], int], Tuple[List[NoteMetaData], int, Dict[str, str]]
    """
    sampleNote = Note(1, datetime.now(), datetime.now(),
                      'Note1', 'Raw Text', 'AI Output')
    return [sampleNote]


def get_note_by_id_impl(id):  # noqa: E501
    """Get one single note by id

    Full note object with all attributes # noqa: E501

    :param id: the user identifier, as userId
    :type id: str

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    return Note(1, datetime.now(), datetime.now(),
                'Note1', 'Raw Text', 'AI Output')


def update_note_by_id_impl(note_id, note):  # noqa: E501
    """Update one single note by id

    Full note object with all attributes # noqa: E501

    :param note_id: the note identifier, as noteId
    :type note_id: str
    :param note: 
    :type note: dict | bytes

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        note = Note.from_dict(connexion.request.get_json())  # noqa: E501
        print(note)
    return note
