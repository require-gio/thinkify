import unittest

from flask import json

from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.verify_bricks_request import VerifyBricksRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNoteController(BaseTestCase):
    """NoteController integration test stubs"""

    def test_get_all_notes(self):
        """Test case for get_all_notes

        Persist sim invoices
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/note/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_sim_invoices(self):
        """Test case for save_sim_invoices

        Persist sim invoices
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/note/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_verify_bricks(self):
        """Test case for verify_bricks

        Checks for brick correctness
        """
        verify_bricks_request = openapi_server.VerifyBricksRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/note/verifyBricks',
            method='POST',
            headers=headers,
            data=json.dumps(verify_bricks_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
