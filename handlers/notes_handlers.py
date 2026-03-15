"""Pure application logic for per-contact notes."""

from typing import List, Dict

class CommandResult:
    """Encapsulate the outcome of a command."""
    def __init__(self, success: bool, payload=None, message: str = ""):
        self.success = success
        self.payload = payload  # raw data, e.g., record, list of notes
        self.message = message

def add_note(args, book) -> CommandResult:
    if len(args) < 2:
        return CommandResult(False, message="Expected contact name and note text")

    name, *rest = args
    tags: List[str] = []

    if rest and rest[-1].startswith("tags:"):
        tag_str = rest.pop()
        tags = [t.strip() for t in tag_str[5:].split(",") if t.strip()]

    note_text = " ".join(rest)
    record = book.find(name)
    if not record:
        return CommandResult(False, message=f"Contact '{name}' not found.")

    record.add_note(note_text, tags)
    return CommandResult(True, payload=record, message="Note added.")


def edit_note(args, book) -> CommandResult:
    if len(args) < 2:
        return CommandResult(False, message="Expected contact name and note index")

    name, index_str, *rest = args
    new_tags: List[str] = None

    if rest and rest[-1].startswith("tags:"):
        tag_str = rest.pop()
        new_tags = [t.strip() for t in tag_str[5:].split(",") if t.strip()]

    new_text = " ".join(rest) if rest else None
    record = book.find(name)
    if not record:
        return CommandResult(False, message=f"Contact '{name}' not found.")

    record.edit_note(int(index_str), new_text, new_tags)
    return CommandResult(True, payload=record, message="Note updated.")


def delete_note(args, book) -> CommandResult:
    if len(args) != 2:
        return CommandResult(False, message="Expected contact name and note index")

    name, index_str = args
    record = book.find(name)
    if not record:
        return CommandResult(False, message=f"Contact '{name}' not found.")

    record.delete_note(int(index_str))
    return CommandResult(True, payload=record, message="Note deleted.")


def show_notes(args, book) -> CommandResult:
    if not args:
        return CommandResult(False, message="Please specify contact name")

    name = args[0]
    filter_tag = args[1] if len(args) > 1 else None
    record = book.find(name)
    if not record:
        return CommandResult(False, message=f"Contact '{name}' not found.")

    notes: List[str] = record.list_notes(filter_tag)
    return CommandResult(True, payload=notes, message="No notes found." if not notes else "")


def search_notes(args, book) -> CommandResult:
    if len(args) != 2:
        return CommandResult(False, message="Expected contact name and tag")

    name, tag = args
    record = book.find(name)
    if not record:
        return CommandResult(False, message="Contact not found.")

    result: List[Dict] = [
        note for note in record.notes
        if tag.lower() in [t.lower() for t in note["tags"]]
    ]

    return CommandResult(True, payload=result, message=f"No notes with tag '{tag}'." if not result else "")