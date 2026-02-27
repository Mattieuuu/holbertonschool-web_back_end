# Basic Authentication

This project contains a Simple API for learning Basic Authentication concepts.

## Description

A simple HTTP API built with Flask for working with the User model and implementing basic authentication.

## Requirements

- Python 3.9
- pip 25.3
- Ubuntu 20.04 LTS

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

Start the server:
```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## API Endpoints

- `GET /api/v1/status` - Returns the status of the API
- `GET /api/v1/stats` - Returns statistics of the API
- `GET /api/v1/users` - Returns the list of users
- `GET /api/v1/users/:id` - Returns a user based on ID
- `DELETE /api/v1/users/:id` - Deletes a user based on ID
- `POST /api/v1/users` - Creates a new user (JSON parameters: email, password, last_name, first_name)
- `PUT /api/v1/users/:id` - Updates a user based on ID (JSON parameters: last_name, first_name)

## Project Structure

```
Basic_authentication/
├── SimpleAPI/
│   ├── api/
│   │   └── v1/
│   │       ├── app.py
│   │       └── views/
│   ├── models/
│   │   ├── base.py
│   │   └── user.py
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Author

Holberton School Project
