# MySQL Advanced

This directory contains SQL scripts for advanced MySQL tasks as part of the Holberton School curriculum.

## Table of Contents
- 0-uniq_users.sql: Create a `users` table with a unique email constraint

## Usage

All scripts are designed to be run on Ubuntu 20.04 LTS with MySQL 8.0. To execute a script, use:

```
cat <script_name.sql> | mysql -uroot -p <database_name>
```

## Requirements
- Each SQL file starts with a comment describing the task
- Each SQL query is preceded by a comment
- SQL keywords are in uppercase
- Scripts are idempotent (won't fail if run multiple times)

## Example
```
echo "SELECT * FROM users;" | mysql -uroot -p holberton
```

## Author
Holberton School Students
