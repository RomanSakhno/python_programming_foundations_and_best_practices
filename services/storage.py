"""Persistence helpers for saving and loading the address book."""

import pickle
import os
from addressbook.address_book import AddressBook

DATA_FILE = "data/addressbook.pkl"


def save_data(book, filename=DATA_FILE):
    """Serialize and save the address book to disk."""

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=DATA_FILE):
    """Load the address book from disk or return an empty one."""

    try:
        if os.path.getsize(filename) == 0:
            return AddressBook()

        with open(filename, "rb") as f:
            return pickle.load(f)

    except (FileNotFoundError, EOFError):
        return AddressBook()