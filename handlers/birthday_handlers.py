"""Handlers for birthday-related commands (pure application logic)."""

from services.birthday_range_service import get_birthdays_within


class CommandResult:
    """Encapsulate the outcome of a command."""
    def __init__(self, success: bool, payload=None, message: str = ""):
        self.success = success
        self.payload = payload  # can be data dict or list
        self.message = message  # optional short text message


def add_birthday(args, book) -> CommandResult:
    """Attach a birthday to an existing contact."""
    if len(args) != 2:
        return CommandResult(False, message="Expected name and birthday")

    name, birthday = args
    record = book.find(name)
    if not record:
        return CommandResult(False, message="Contact not found")

    record.add_birthday(birthday)
    return CommandResult(True, payload={"name": name, "birthday": record.birthday.value})


def show_birthday(args, book) -> CommandResult:
    """Return the stored birthday for a contact."""
    if len(args) != 1:
        return CommandResult(False, message="Expected contact name")

    name = args[0]
    record = book.find(name)
    if not record:
        return CommandResult(False, message="Contact not found")

    if not record.birthday:
        return CommandResult(True, payload=None, message="Birthday not set")

    return CommandResult(True, payload={"name": name, "birthday": record.birthday.value})


def birthdays(args, book) -> CommandResult:
    """Return upcoming birthdays in the next 7 days."""
    upcoming = book.get_upcoming_birthdays()
    return CommandResult(True, payload=upcoming)


def birthdays_in(args, book) -> CommandResult:
    """Return birthdays within the next N days."""
    if not args:
        return CommandResult(False, message="Days argument required")

    try:
        days = int(args[0])
        if days < 0:
            raise ValueError
    except ValueError:
        return CommandResult(False, message="Days must be a non-negative integer")

    upcoming = get_birthdays_within(book, days)
    return CommandResult(True, payload=upcoming)