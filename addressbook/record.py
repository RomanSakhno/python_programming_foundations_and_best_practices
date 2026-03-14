"""Contact record with phones, email, birthday and notes."""

from .fields import Name, Phone, Birthday, Email
from colorama import Fore, Style

white = f"{Style.BRIGHT}"


class Record:
    """Represents a single contact in the address book."""

    def __init__(self, name):
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

    def add_phone(self, phone):
        """Append a new phone number to the record."""
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        """Replace an existing phone number with a new one."""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        raise ValueError("Old phone not found.")

    def find_phone(self, phone):
        """Return the phone value if present on this record."""
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def add_birthday(self, birthday):
        """Set the birthday for the contact."""
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        """Set or update the email address for the contact."""
        self.email = Email(email)

    def add_note(self, note_text, tags=None):
        """Add a note with optional list of tags."""
        if tags is None:
            tags = []
        self.notes.append({"text": note_text, "tags": tags})

    def edit_note(self, index, new_text=None, new_tags=None):
        """Edit an existing note by index, changing text and/or tags."""
        if index < 0 or index >= len(self.notes):
            raise IndexError("Note index out of range.")
        if new_text is not None:
            self.notes[index]["text"] = new_text
        if new_tags is not None:
            self.notes[index]["tags"] = new_tags

    def list_notes(self, filter_tag=None):
        """Return a list of formatted notes, optionally filtered by tag."""
        result = []
        for i, note in enumerate(self.notes):
            if filter_tag and filter_tag not in note["tags"]:
                continue
            tags_str = f" [{', '.join(note['tags'])}]" if note["tags"] else ""
            result.append(f"{i}: {note['text']}{tags_str}")
        return result

    def delete_note(self, index):
        """Delete the note at the given index."""
        if index < 0 or index >= len(self.notes):
            raise IndexError("Note index out of range.")
        del self.notes[index]

    def remove_phone(self, phone):
        """Remove a phone number from the record."""
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        raise ValueError("Phone not found.")

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones) if self.phones else "Not set"
        email = self.email if self.email else "Not set"
        birthday = str(self.birthday) if self.birthday else "Not set"

        notes_str = ""
        if self.notes:
            for i, note in enumerate(self.notes, 1):
                tags = f" [{', '.join(note['tags'])}]" if note['tags'] else ""
                notes_str += f"{i}. {note['text']}{tags}\n"
        else:
            notes_str = "No notes"

        return (
            f"**📇 Name:** {self.name.value}\n"
            f"📞 Phones: {phones}\n"
            f"✉ Email: {email}\n"
            f"🎂 Birthday: {birthday}\n"
            f"📝 Notes:\n{notes_str}"
        )