"""Handlers for managing per-contact notes via the CLI."""

from utils.decorators import input_error


@input_error
def add_note(args, book):
    """Add a note with optional tags to the given contact."""
    name, *rest = args
    tags = []

    if rest and rest[-1].startswith("tags:"):
        tag_str = rest.pop()
        tags = [t.strip() for t in tag_str[5:].split(",") if t.strip()]

    note_text = " ".join(rest)
    record = book.find(name)
    if not record:
        raise KeyError(f"Contact '{name}' not found.")

    record.add_note(note_text, tags)
    return "Note added."

@input_error
def edit_note(args, book):
    """Edit an existing note for a contact, updating text and/or tags."""
    name, index_str, *rest = args
    new_tags = None

    if rest and rest[-1].startswith("tags:"):
        tag_str = rest.pop()
        new_tags = [t.strip() for t in tag_str[5:].split(",") if t.strip()]

    new_text = " ".join(rest) if rest else None
    record = book.find(name)
    if not record:
        raise KeyError(f"Contact '{name}' not found.")

    record.edit_note(int(index_str), new_text, new_tags)
    return "Note updated."

@input_error
def delete_note(args, book):
    """Delete a note by index for the given contact."""
    name, index_str = args
    record = book.find(name)
    if not record:
        raise KeyError(f"Contact '{name}' not found.")

    record.delete_note(int(index_str))
    return "Note deleted."

@input_error
def show_notes(args, book):
    """Show all notes for a contact, optionally filtered by tag."""
    if not args:
        return "Please specify contact name. Example: notes Vasya"

    name = args[0]
    filter_tag = args[1] if len(args) > 1 else None
    record = book.find(name)
    if not record:
        raise KeyError(f"Contact '{name}' not found.")

    notes = record.list_notes(filter_tag)
    return "\n".join(notes) if notes else "No notes found."

@input_error
def search_notes(args, book):
    name, tag = args

    record = book.find(name)

    if not record:
        return "Contact not found."

    result = [
        note for note in record.notes
            if tag.lower() in [t.lower() for t in note["tags"]]
        ]

    if not result:
        return f"No notes with tag '{tag}'."

    lines = []
    lines.append("=" * 40)
    lines.append(f"📝 Notes with tag '{tag}'")
    lines.append(f"📇 Contact: {record.name.value}")
    lines.append("")

    for i, note in enumerate(result, 1):
        tags = ", ".join(note["tags"]) if note["tags"] else "no tags"

        lines.append(f"  {i}. 📄 {note['text']}")
        lines.append(f"     🏷 Tags: {tags}")
        lines.append("")

    lines.append("=" * 40)

    return "\n".join(lines)