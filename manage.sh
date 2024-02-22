#!/bin/bash
# Requires the database to be up
FLASK_ENV=development DATABASE_URI=postgresql://user:admin@127.0.0.1:5432/db python3 manage.py
