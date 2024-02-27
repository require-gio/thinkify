import unittest

from flask import json

from openapi_server.test import BaseTestCase


class TestCORSController(BaseTestCase):
    """CORSController integration test stubs"""

    def test_note_note_id_options(self):
        """Test case for note_note_id_options

        CORS support
        """
        headers = { 
        }
        response = self.client.open(
            '/api/v1/note/{note_id}'.format(note_id='note_id_example'),
            method='OPTIONS',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
