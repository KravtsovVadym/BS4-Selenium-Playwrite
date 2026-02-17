"""
This module connects to Django models using the load_django import,
reads the json file and writes to the postgres database.
"""

from load_django import *

from django.core.exceptions import ValidationError
from django.db import IntegrityError, DatabaseError

import json

from parser_app.models import Product


def push_db():
    try:
        with open("../files/parse_data_brain.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"File error: {e}")
        return

    try:
        obj, create = Product.objects.get_or_create(**data)
        print(f"{obj}, {create}")
    except (ValidationError, IntegrityError, DatabaseError, TypeError) as e:
        print(f"Database error: {e}")


if __name__ == "__main__":
    push_db()
