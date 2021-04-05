#!/usr/bin/env bash
pycodestyle "api/v1/app.py" "api/v1/auth/auth.py" "api/v1/auth/basic_auth.py"

#python3 -c 'print(__import__("api/v1/app").__doc__)'
#python3 -c 'print(__import__("api/v1/auth/auth.py").Auth.__doc__)'

#mypy api/v1/app.py
#mypy api/v1/auth/auth.py
#mypy api/v1/auth/basic_auth.py
