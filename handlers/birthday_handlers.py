from utils.decorators import input_error


@input_error
def add_birthday(args, book):

    name, birthday = args

    record = book.find(name)

    if not record:
        raise KeyError()

    record.add_birthday(birthday)

    return "Birthday added."


@input_error
def show_birthday(args, book):

    name = args[0]

    record = book.find(name)

    if not record:
        raise KeyError()

    if not record.birthday:
        return "Birthday not set."

    return str(record.birthday)


@input_error
def birthdays(args, book):

    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return "No upcoming birthdays."

    return "\n".join(
        f"{item['name']} - {item['congratulation_date']}"
        for item in upcoming
    )