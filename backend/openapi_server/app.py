#!/usr/bin/env python3

import openapi_server.db_models
import os
from connexion import FlaskApp
from flask_cors import CORS
from openapi_server.database import db
from dotenv import load_dotenv
from flask_migrate import Migrate
from openapi_server.encoder import JSONEncoder
from flask import request


load_dotenv()
app = FlaskApp(__name__, jsonifier=JSONEncoder(), pythonic_params=True)
app.add_api('./openapi/openapi.yaml')

app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'SQLALCHEMY_DATABASE_URI')
db.init_app(app.app)
with app.app.app_context():
    db.create_all()


migrate = Migrate(app.app, db)

# import models here so that flask-migrate can detect them

# add CORS support
CORS(app.app)

# builder method required for flask-cli


@app.app.route('/api/v1/hi', methods=["POST"])
def helloWorld():
    data = request.json
    print(data)
    return "Hi"


def create_app():
    return app.app


if __name__ == "__main__":
    app.run()
