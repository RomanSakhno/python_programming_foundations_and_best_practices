from .fields import Name, Phone, Birthday, Email
from colorama import Fore, Style
white = f"{Style.BRIGHT}"


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
        lines = []

        # Name
        lines.append(f"📇 {Style.BRIGHT}Name: {Fore.GREEN}{self.name.value}{Style.RESET_ALL}")

        # Phones
        if self.phones:
            phones_str = "; ".join(p.value for p in self.phones)
            lines.append(f"{white}  📞 Phones: {phones_str}{Style.RESET_ALL}")
        else:
            lines.append(f"{white}  📞 Phones: Not set{Style.RESET_ALL}")

        # Email
        lines.append(f"{white}  ✉ Email: {self.email if self.email else 'Not set'}{Style.RESET_ALL}")

        # Birthday
        lines.append(f"{white}  🎂 Birthday: {str(self.birthday) if self.birthday else 'Not set'}{Style.RESET_ALL}")

        # Notes
        if self.notes:
            lines.append(f"{white}  📝 Notes:{Style.RESET_ALL}")
            for i, note in enumerate(self.notes):
                tags_str = f" [{', '.join(note['tags'])}]" if note["tags"] else ""
                lines.append(f"{white}    {i}. {note['text']}{tags_str}{Style.RESET_ALL}")
        else:
            lines.append(f"{white}  📝 Notes: None{Style.RESET_ALL}")

        return "\n".join(lines)