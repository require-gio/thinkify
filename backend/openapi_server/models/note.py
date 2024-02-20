from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Note(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, created_at=None, updated_at=None, name=None, raw_text=None, ai_output=None):  # noqa: E501
        """Note - a model defined in OpenAPI

        :param id: The id of this Note.  # noqa: E501
        :type id: int
        :param created_at: The created_at of this Note.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this Note.  # noqa: E501
        :type updated_at: datetime
        :param name: The name of this Note.  # noqa: E501
        :type name: str
        :param raw_text: The raw_text of this Note.  # noqa: E501
        :type raw_text: str
        :param ai_output: The ai_output of this Note.  # noqa: E501
        :type ai_output: str
        """
        self.openapi_types = {
            'id': int,
            'created_at': datetime,
            'updated_at': datetime,
            'name': str,
            'raw_text': str,
            'ai_output': str
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'name': 'name',
            'raw_text': 'rawText',
            'ai_output': 'aiOutput'
        }

        self._id = id
        self._created_at = created_at
        self._updated_at = updated_at
        self._name = name
        self._raw_text = raw_text
        self._ai_output = ai_output

    @classmethod
    def from_dict(cls, dikt) -> 'Note':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Note of this Note.  # noqa: E501
        :rtype: Note
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Note.


        :return: The id of this Note.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Note.


        :param id: The id of this Note.
        :type id: int
        """

        self._id = id

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this Note.


        :return: The created_at of this Note.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this Note.


        :param created_at: The created_at of this Note.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self) -> datetime:
        """Gets the updated_at of this Note.


        :return: The updated_at of this Note.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """Sets the updated_at of this Note.


        :param updated_at: The updated_at of this Note.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def name(self) -> str:
        """Gets the name of this Note.


        :return: The name of this Note.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Note.


        :param name: The name of this Note.
        :type name: str
        """

        self._name = name

    @property
    def raw_text(self) -> str:
        """Gets the raw_text of this Note.


        :return: The raw_text of this Note.
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text: str):
        """Sets the raw_text of this Note.


        :param raw_text: The raw_text of this Note.
        :type raw_text: str
        """

        self._raw_text = raw_text

    @property
    def ai_output(self) -> str:
        """Gets the ai_output of this Note.


        :return: The ai_output of this Note.
        :rtype: str
        """
        return self._ai_output

    @ai_output.setter
    def ai_output(self, ai_output: str):
        """Sets the ai_output of this Note.


        :param ai_output: The ai_output of this Note.
        :type ai_output: str
        """

        self._ai_output = ai_output
