import pickle
import os
from addressbook.address_book import AddressBook

DATA_FILE = "data/addressbook.pkl"


def save_data(book, filename=DATA_FILE):

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename=DATA_FILE):

    try:
        if os.path.getsize(filename) == 0:
            return AddressBook()

        with open(filename, "rb") as f:
            return pickle.load(f)

    except (FileNotFoundError, EOFError):
        return AddressBook()