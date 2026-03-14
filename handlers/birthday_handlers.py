"""Handlers for birthday-related CLI commands."""

from utils.decorators import input_error
from services.birthday_range_service import get_birthdays_within


@input_error
def add_birthday(args, book):
    """Attach a birthday to an existing contact."""

    name, birthday = args

    record = book.find(name)

    if not record:
        raise KeyError()

    record.add_birthday(birthday)

    return "Birthday added."


@input_error
def show_birthday(args, book):
    """Show the stored birthday for a contact, if any."""

    name = args[0]

    record = book.find(name)

    if not record:
        raise KeyError()

    if not record.birthday:
        return "Birthday not set."

    return str(record.birthday)


@input_error
def birthdays(args, book):
    """Show upcoming birthdays in the next seven days."""

    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return "No upcoming birthdays."

    return "\n".join(
        f"{item['name']} - {item['congratulation_date']}"
        for item in upcoming
    )


@input_error
def birthdays_in(args, book):
    """Show birthdays that fall within the next given number of days."""

    if not args:
        raise IndexError()

    days_str = args[0]

    try:
        days = int(days_str)
    except ValueError:
        raise ValueError("Days must be an integer.")

    if days < 0:
        raise ValueError("Days must be a non-negative integer.")

    upcoming = get_birthdays_within(book, days)

    if not upcoming:
        return f"No birthdays within {days} days."

    return "\n".join(
        f"{item['name']} - {item['congratulation_date']}"
        for item in upcoming
    )