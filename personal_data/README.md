# Personal Data

This project focuses on handling Personally Identifiable Information (PII) securely in Python applications.

## Learning Objectives

At the end of this project, you should be able to explain:

- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5)
- All files must be executable
- All modules, classes, and functions should have documentation
- All functions should be type annotated

## Project Structure

```
personal_data/
├── filtered_logger.py      # Main logging and database module
├── encrypt_password.py     # Password encryption and validation
├── setup_db.sql           # Database setup script
└── README.md
```

## Installation

Install required packages:

```bash
pip3 install mysql-connector-python bcrypt
```

## Features

### 1. PII Filtering (`filtered_logger.py`)

**PII_FIELDS**: Tuple containing 5 important PII fields:
- `name`, `email`, `phone`, `ssn`, `password`

**filter_datum(fields, redaction, message, separator)**: Obfuscates specified fields in log messages using regex.

**RedactingFormatter**: Custom logging formatter that filters PII fields in log records.

**get_logger()**: Returns a configured logger that obfuscates PII fields.

**get_db()**: Securely connects to MySQL database using environment variables:
- `PERSONAL_DATA_DB_USERNAME` (default: "root")
- `PERSONAL_DATA_DB_PASSWORD` (default: "")
- `PERSONAL_DATA_DB_HOST` (default: "localhost")
- `PERSONAL_DATA_DB_NAME` (required)

**main()**: Retrieves and displays user data from database with PII fields obfuscated.

### 2. Password Encryption (`encrypt_password.py`)

**hash_password(password)**: Hashes a password using bcrypt with automatic salt generation.

**is_valid(hashed_password, password)**: Validates a password against its hash.

## Usage

### Setup Database

```bash
cat setup_db.sql | mysql -uroot -p
```

### Run the Logger

```bash
PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
```

### Password Hashing Example

```python
from encrypt_password import hash_password, is_valid

password = "MySecurePassword123"
hashed = hash_password(password)
print(is_valid(hashed, password))  # True
```

### Log Filtering Example

```python
from filtered_logger import filter_datum

fields = ["password", "ssn"]
message = "name=John;password=secret;ssn=123-45-6789;"
filtered = filter_datum(fields, "***", message, ";")
# Output: name=John;password=***;ssn=***;
```

## Security Best Practices

✅ Never store passwords in plain text - Always use bcrypt hashing  
✅ Never hardcode credentials - Use environment variables  
✅ Always obfuscate PII in logs - Use RedactingFormatter  
✅ Use unique salts - bcrypt generates them automatically

## Author

Holberton School Project - Back-end Development

## Repository

- **GitHub repository**: `holbertonschool-web_back_end`
- **Directory**: `personal_data`
