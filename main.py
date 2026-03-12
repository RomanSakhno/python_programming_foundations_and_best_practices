from addressbook.address_book import AddressBook
from handlers.notes_handlers import add_note
from notes import notes_manager
from services.storage import load_data, save_data
from utils.parser import parse_input

from handlers.contact_handlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all, search_contacts, delete_contact, edit_email, edit_name, delete_phone
)

from handlers.birthday_handlers import (
    add_birthday,
    show_birthday,
    birthdays
)


def main():
    book: AddressBook = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "search":
            print(search_contacts(args, book))

        elif command == "delete":
            print(delete_contact(args, book))

        elif command == "add-note":
            print(add_note(args, notes_manager))

        elif command == "edit-email":
            print(edit_email(args, book))

        elif command == "edit-name":
            print(edit_name(args, book))

        elif command == "delete-phone":
            print(delete_phone(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()