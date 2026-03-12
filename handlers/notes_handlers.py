from utils.decorators import input_error


@input_error
def add_note(args, manager):
    text = " ".join(args)
    manager.add(text)

    return "Note added."

@input_error
def edit_note(args, book):
    name, index_str, *note_parts = args
    new_text = " ".join(note_parts)
    record = book.find(name)
    if not record:
        raise KeyError()
    record.edit_note(int(index_str), new_text)
    return "Note updated."

@input_error
def delete_note(args, book):
    name, index_str = args
    record = book.find(name)
    if not record:
        raise KeyError()
    record.delete_note(int(index_str))
    return "Note deleted."

@input_error
def show_notes(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError()
    notes = record.list_notes()
    return "\n".join(notes) if notes else "No notes."