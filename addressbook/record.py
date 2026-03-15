"""Contact record with phones, email, birthday and notes (pure domain logic)."""

from .fields import Name, Phone, Birthday, Email


class Record:
    """Represents a single contact in the address book."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.birthday = None
        self.notes = []

    def __setstate__(self, state):
        """Restore state for older pickled objects missing new attributes."""
        self.__dict__.update(state)
        if not hasattr(self, "email"):
            self.email = None
        if not hasattr(self, "notes"):
            self.notes = []

    # -----------------------------
    # Domain methods
    # -----------------------------

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        raise ValueError("Old phone not found.")

    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        raise ValueError("Phone not found.")

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def add_email(self, email: str):
        self.email = Email(email)

    def add_note(self, note_text: str, tags=None):
        if tags is None:
            tags = []
        self.notes.append({"text": note_text, "tags": tags})

    def edit_note(self, index: int, new_text=None, new_tags=None):
        if index < 0 or index >= len(self.notes):
            raise IndexError("Note index out of range.")
        if new_text is not None:
            self.notes[index]["text"] = new_text
        if new_tags is not None:
            self.notes[index]["tags"] = new_tags

    def delete_note(self, index: int):
        if index < 0 or index >= len(self.notes):
            raise IndexError("Note index out of range.")
        del self.notes[index]

    # -----------------------------
    # Pure data access / domain getters
    # -----------------------------

    def get_data(self):
        """Return a dictionary of the record's raw data (no UI formatting)."""
        return {
            "name": self.name.value,
            "phones": [p.value for p in self.phones],
            "email": self.email.value if self.email else None,
            "birthday": self.birthday.value if self.birthday else None,
            "notes": self.notes.copy()
        }