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

@input_error
def search_contacts(args, book):

    query = args[0]

    results = book.search(query)

    if not results:
        return "No contacts found."

    return "\n".join(str(r) for r in results)

@input_error
def delete_contact(args, book):

    name = args[0]

    record = book.delete(name)

    if not record:
        raise KeyError()

    return "Contact deleted."

@input_error
def edit_email(args, book):

    name, new_email = args

    record = book.find(name)

    if not record:
        raise KeyError()

    record.add_email(new_email)

    return "Email updated."

@input_error
def edit_name(args, book):

    old_name, new_name = args

    record = book.rename(old_name, new_name)

    if not record:
        raise KeyError()

    return "Contact renamed."

@input_error
def delete_phone(args, book):

    name, phone = args

    record = book.find(name)

    if not record:
        raise KeyError()

    record.remove_phone(phone)

    return "Phone deleted."