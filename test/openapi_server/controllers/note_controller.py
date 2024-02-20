import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.verify_bricks_request import VerifyBricksRequest  # noqa: E501
from openapi_server import util


def get_all_notes():  # noqa: E501
    """Persist sim invoices

    Array of all notes invoices will be saved in database # noqa: E501


    :rtype: Union[List[Note], Tuple[List[Note], int], Tuple[List[Note], int, Dict[str, str]]
    """
    return 'do some magic!'


def save_sim_invoices(id):  # noqa: E501
    """Persist sim invoices

    Array of all notes invoices will be saved in database # noqa: E501

    :param id: the user identifier, as userId
    :type id: str

    :rtype: Union[List[Note], Tuple[List[Note], int], Tuple[List[Note], int, Dict[str, str]]
    """
    return 'do some magic!'


def verify_bricks(verify_bricks_request):  # noqa: E501
    """Checks for brick correctness

    Array of bricks will be processed to find out whether they exist, whether they refer to the specified tenant and whether each of them has a sim card. # noqa: E501

    :param verify_bricks_request: 
    :type verify_bricks_request: dict | bytes

    :rtype: Union[List[Note], Tuple[List[Note], int], Tuple[List[Note], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        verify_bricks_request = VerifyBricksRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
