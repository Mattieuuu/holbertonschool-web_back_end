# User Authentication Service
This project implements a basic authentication service using Python, Flask, and SQLAlchemy.

## Features
- User registration and password hashing
- Basic Flask app with welcome route
- SQLAlchemy ORM for user management

## Setup
- Python 3.9 (Ubuntu 20.04 LTS)
- Install dependencies: `pip3 install flask bcrypt`

## Usage
- Run the Flask app: `python3 app.py`
- Access the welcome route: `GET /` returns `{"message": "Bienvenue"}`

## Requirements
- All files must be executable and follow pycodestyle
- All modules, classes, and functions are documented
- Only public methods of Auth and DB are used outside these classes
