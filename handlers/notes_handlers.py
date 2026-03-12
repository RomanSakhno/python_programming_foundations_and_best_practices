from utils.decorators import input_error


@input_error
def add_note(args, book):
    name, *rest = args
    tags = []

    if rest and rest[-1].startswith("tags:"):
        tag_str = rest.pop()
        tags = [t.strip() for t in tag_str[5:].split(",") if t.strip()]

    note_text = " ".join(rest)
    record = book.find(name)  # Используем AddressBook
    if not record:
        raise KeyError(f"Contact '{name}' not found.")

    record.add_note(note_text, tags)
    return "Note added."

@input_error
def edit_note(args, book):
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
    name, index_str = args
    record = book.find(name)
    if not record:
        raise KeyError(f"Contact '{name}' not found.")

    record.delete_note(int(index_str))
    return "Note deleted."

@input_error
def show_notes(args, book):
    name = args[0]
    filter_tag = args[1] if len(args) > 1 else None
    record = book.find(name)
    if not record:
        raise KeyError(f"Contact '{name}' not found.")

    notes = record.list_notes(filter_tag)
    return "\n".join(notes) if notes else "No notes found."