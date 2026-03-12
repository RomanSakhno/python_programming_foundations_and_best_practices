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

    def add_note(self, note_text, tags=None):
        if tags is None:
            tags = []
        self.notes.append({"text": note_text, "tags": tags})

    def edit_note(self, index, new_text=None, new_tags=None):
        if index < 0 or index >= len(self.notes):
            raise IndexError("Note index out of range.")
        if new_text is not None:
            self.notes[index]["text"] = new_text
        if new_tags is not None:
            self.notes[index]["tags"] = new_tags

    def list_notes(self, filter_tag=None):
        result = []
        for i, note in enumerate(self.notes):
            if filter_tag and filter_tag not in note["tags"]:
                continue
            tags_str = f" [{', '.join(note['tags'])}]" if note["tags"] else ""
            result.append(f"{i}: {note['text']}{tags_str}")
        return result

    def delete_note(self, index):
        if index < 0 or index >= len(self.notes):
            raise IndexError("Note index out of range.")
        del self.notes[index]

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        raise ValueError("Phone not found.")

    def __str__(self):
        # Верхняя граница блока контакта
        lines = [f"{'=' * 40}"]

        # Name
        lines.append(f"📇 Name: {self.name.value}")

        # Phones
        if self.phones:
            phones_str = "; ".join(p.value for p in self.phones)
            lines.append(f"  📞 Phones: {phones_str}")
        else:
            lines.append("  📞 Phones: Not set")

        # Email
        lines.append(f"  ✉ Email: {self.email if self.email else 'Not set'}")

        # Birthday
        lines.append(f"  🎂 Birthday: {str(self.birthday) if self.birthday else 'Not set'}")

        # Notes
        if self.notes:
            lines.append("  📝 Notes:")
            for i, note in enumerate(self.notes):
                tags_str = f" [{', '.join(note['tags'])}]" if note["tags"] else ""
                lines.append(f"    {i}. {note['text']}{tags_str}")
        else:
            lines.append("  📝 Notes: None")

        # Нижняя граница блока контакта
        lines.append(f"{'=' * 40}")

        return "\n".join(lines)