"""Contact command handlers (pure application logic)."""

from addressbook.record import Record


class CommandResult:
    """Encapsulate the outcome of a command."""
    def __init__(self, success: bool, payload=None, message: str = ""):
        self.success = success
        self.payload = payload  # raw data, e.g., record or list of records
        self.message = message  # optional short message


def add_contact(args, book) -> CommandResult:
    """Add a new contact or update existing."""
    if len(args) < 2:
        return CommandResult(False, message="Expected name and phone")

    name, phone, *_ = args
    record = book.find(name)
    is_new = False

    if not record:
        record = Record(name)
        book.add_record(record)
        is_new = True

    record.add_phone(phone)

    return CommandResult(True, payload=record, message="Contact added." if is_new else "Contact updated.")


def change_contact(args, book) -> CommandResult:
    """Edit an existing phone number for a contact."""
    if len(args) != 3:
        return CommandResult(False, message="Expected name, old phone, new phone")

    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return CommandResult(False, message="Contact not found")

    record.edit_phone(old_phone, new_phone)
    return CommandResult(True, payload=record, message="Phone updated.")


def show_phone(args, book) -> CommandResult:
    """Return all phones for a contact."""
    if len(args) != 1:
        return CommandResult(False, message="Expected contact name")

    name = args[0]
    record = book.find(name)
    if not record:
        return CommandResult(False, message="Contact not found")

    phones = [p.value for p in record.phones]
    return CommandResult(True, payload={"name": name, "phones": phones})


def show_all(args, book) -> CommandResult:
    """Return all contacts."""
    if not book.data:
        return CommandResult(True, payload=[], message="No contacts found.")

    return CommandResult(True, payload=list(book.data.values()))


def search_contacts(args, book) -> CommandResult:
    """Search contacts by name, phone, or email substring."""
    if not args:
        return CommandResult(False, message="Search query required")

    query = args[0]
    results = book.search(query)
    return CommandResult(True, payload=results, message="No contacts found." if not results else "")


def delete_contact(args, book) -> CommandResult:
    if len(args) != 1:
        return CommandResult(False, message="Expected contact name")

    name = args[0]
    record = book.delete(name)
    if not record:
        return CommandResult(False, message="Contact not found")

    return CommandResult(True, payload={"name": name}, message="Contact deleted.")


def edit_email(args, book) -> CommandResult:
    if len(args) != 2:
        return CommandResult(False, message="Expected name and new email")

    name, new_email = args
    record = book.find(name)
    if not record:
        return CommandResult(False, message="Contact not found")

    record.add_email(new_email)
    return CommandResult(True, payload=record, message="Email updated.")


def edit_name(args, book) -> CommandResult:
    if len(args) != 2:
        return CommandResult(False, message="Expected old name and new name")

    old_name, new_name = args
    record = book.rename(old_name, new_name)
    if not record:
        return CommandResult(False, message="Contact not found")

    return CommandResult(True, payload=record, message="Contact renamed.")


def delete_phone(args, book) -> CommandResult:
    if len(args) != 2:
        return CommandResult(False, message="Expected name and phone")

    name, phone = args
    record = book.find(name)
    if not record:
        return CommandResult(False, message="Contact not found")

    record.remove_phone(phone)
    return CommandResult(True, payload=record, message="Phone deleted.")