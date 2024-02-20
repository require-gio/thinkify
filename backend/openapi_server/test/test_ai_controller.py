import unittest

from flask import json

from openapi_server.models.ai_response import AIResponse  # noqa: E501
from openapi_server.models.generate_response_for_raw_note_request import GenerateResponseForRawNoteRequest  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAiController(BaseTestCase):
    """AiController integration test stubs"""

    def test_generate_response_for_raw_note(self):
        """Test case for generate_response_for_raw_note

        Generate an AI response based on a raw note and prompt
        """
        generate_response_for_raw_note_request = openapi_server.GenerateResponseForRawNoteRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/ai/generateResponseForRawNote',
            method='POST',
            headers=headers,
            data=json.dumps(generate_response_for_raw_note_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_transcribe_audio_for_note(self):
        """Test case for transcribe_audio_for_note

        Transcribe an audio file
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(note_id='note_id_example',
                    file_name='/path/to/file')
        response = self.client.open(
            '/api/v1/ai/transcribeAudioForNote',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
