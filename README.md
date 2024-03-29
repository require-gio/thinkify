# API-first Angular Web App with Flask Backend and OpenAPI Integration

## Overview
This project is intended to demonstrate best practices and less-code principles when it comes to web development. The Angular frontend was generated via Angular-CLI. Almost the whole Python-Flask backend, on the other hand, was generated by the [OpenAPI Generator](https://openapi-generator.tech) project. The communication between the frontend and backend is specified through an OpenAPI 3.0 file that is also the base for the code generator. 

![alt text](https://github.com/require-gio/thinkify/blob/master/screenshot.png?raw=true)

## Usage

### Starting Backend
To run the backend server, please execute the following from the backend root directory:

```
cd backend
pip install -r requirements.txt
uvicorn openapi_server.app:app --port 8081
```

you can see the swagger documentation in your browser here:

```
http://localhost:8081/api/v1/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:8081/api/v1/openapi.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

### Starting Frontend
Go to the frontend directory and execute the following:

```
cd frontend
npm install
npm run start
```

### Starting Database
Got to project root and execute:
```bash
docker-compose up -d db
```

## Running everything with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the images and starting all containers
docker-compose up -d
```