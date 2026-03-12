from utils.decorators import input_error
from addressbook.record import Record


@input_error
def add_contact(args, book):

    name, phone, *_ = args

    record = book.find(name)

    if record is None:

        record = Record(name)
        book.add_record(record)

        message = "Contact added."

    else:
        message = "Contact updated."

    record.add_phone(phone)

    return message


@input_error
def change_contact(args, book):

    name, old_phone, new_phone = args

    record = book.find(name)

    if not record:
        raise KeyError()

    record.edit_phone(old_phone, new_phone)

    return "Phone updated."


@input_error
def show_phone(args, book):

    name = args[0]

    record = book.find(name)

    if not record:
        raise KeyError()

    return "; ".join(p.value for p in record.phones)


@input_error
def show_all(book):

    if not book.data:
        return "No contacts found."

    return "\n".join(str(record) for record in book.data.values())