from .fields import Name, Phone, Birthday, Email


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.birthday = None
        self.notes = []

    def __setstate__(self, state):
        self.__dict__.update(state)

        if not hasattr(self, "email"):
            self.email = None

        if not hasattr(self, "notes"):
            self.notes = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        raise ValueError("Old phone not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        self.email = Email(email)

    def add_note(self, text):
        self.notes.append(text)

    def edit_note(self, index, new_text):
        if index < 0 or index >= len(self.notes):
            raise IndexError("Note index out of range.")
        self.notes[index] = new_text

    def list_notes(self):
        return [f"{i}: {note}" for i, note in enumerate(self.notes)]

    def delete_note(self, index):
        self.notes.pop(index)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        raise ValueError("Phone not found.")

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = str(self.birthday) if self.birthday else "Not set"
        return f"Name: {self.name.value}, Phones: {phones}, Birthday: {birthday}"