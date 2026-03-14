"""Value objects for validated contact fields."""

import re
from datetime import datetime


class Field:
    """Base class for all field types."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Contact name, must be non-empty."""

    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        super().__init__(value)


class Phone(Field):
    """Phone number consisting of exactly 10 digits."""

    def __init__(self, value):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    """Birthday stored as a datetime parsed from DD.MM.YYYY."""

    def __init__(self, value):
        try:
            date_obj = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(date_obj)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Email(Field):
    """Email address validated by a simple regex."""

    EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    def __init__(self, value):

        if not re.fullmatch(self.EMAIL_REGEX, value):
            raise ValueError("Invalid email format.")

        super().__init__(value)