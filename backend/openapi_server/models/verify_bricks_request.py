from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class VerifyBricksRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, brick_serial_numbers=None, tenant=None):  # noqa: E501
        """VerifyBricksRequest - a model defined in OpenAPI

        :param brick_serial_numbers: The brick_serial_numbers of this VerifyBricksRequest.  # noqa: E501
        :type brick_serial_numbers: List[str]
        :param tenant: The tenant of this VerifyBricksRequest.  # noqa: E501
        :type tenant: str
        """
        self.openapi_types = {
            'brick_serial_numbers': List[str],
            'tenant': str
        }

        self.attribute_map = {
            'brick_serial_numbers': 'brickSerialNumbers',
            'tenant': 'tenant'
        }

        self._brick_serial_numbers = brick_serial_numbers
        self._tenant = tenant

    @classmethod
    def from_dict(cls, dikt) -> 'VerifyBricksRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The verifyBricks_request of this VerifyBricksRequest.  # noqa: E501
        :rtype: VerifyBricksRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def brick_serial_numbers(self) -> List[str]:
        """Gets the brick_serial_numbers of this VerifyBricksRequest.


        :return: The brick_serial_numbers of this VerifyBricksRequest.
        :rtype: List[str]
        """
        return self._brick_serial_numbers

    @brick_serial_numbers.setter
    def brick_serial_numbers(self, brick_serial_numbers: List[str]):
        """Sets the brick_serial_numbers of this VerifyBricksRequest.


        :param brick_serial_numbers: The brick_serial_numbers of this VerifyBricksRequest.
        :type brick_serial_numbers: List[str]
        """

        self._brick_serial_numbers = brick_serial_numbers

    @property
    def tenant(self) -> str:
        """Gets the tenant of this VerifyBricksRequest.


        :return: The tenant of this VerifyBricksRequest.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant: str):
        """Sets the tenant of this VerifyBricksRequest.


        :param tenant: The tenant of this VerifyBricksRequest.
        :type tenant: str
        """

        self._tenant = tenant
