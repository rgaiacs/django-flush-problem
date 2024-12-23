#!/bin/sh

# Run database migration
# This need to be first to avoid errors due missing tables
python3 manage.py migrate \
    --no-input \
    --traceback

# Remove all existing data
python3 manage.py flush \
    --no-input \
    --traceback

# Start Django development server
python3 manage.py runserver \
    0.0.0.0:8000