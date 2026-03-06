# Session authentication

This project implements session authentication for a web API.

## Resources
- REST API Authentication Mechanisms
- HTTP Cookie
- Flask
- Flask Cookie

## Learning Objectives
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Requirements
### Python Scripts
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle style (version 2.6)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation

## Tasks

### 0. Et moi et moi et moi!
Copy all your work of the Basic authentication project in this new folder.

Add a new endpoint: `GET /users/me` to retrieve the authenticated User object.

- Update `@app.before_request` in `api/v1/app.py`:
  - Assign the result of `auth.current_user(request)` to `request.current_user`
  
- Update method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
  - If `<user_id>` is equal to `me` and `request.current_user` is `None`: `abort(404)`
  - If `<user_id>` is equal to `me` and `request.current_user` is not `None`: return the authenticated User in a JSON response
  - Otherwise, keep the same behavior
