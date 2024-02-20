#!/usr/bin/env python3

import connexion
from flask_cors import CORS

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Thinkify - OpenAPI 3.0'},
                pythonic_params=True)

    # add CORS support
    CORS(app.app)

    app.run(port=8081)


if __name__ == '__main__':
    main()
