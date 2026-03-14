"""CLI entry point for the address book assistant."""

from addressbook.address_book import AddressBook
from handlers.commands_registry import COMMANDS
from services.storage import load_data, save_data
from utils.parser import parse_input


def main():
    """Run the main interactive command loop."""
    book: AddressBook = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        action = COMMANDS.get(command)
        if not action:
            print("Invalid command.")
            continue

        try:
            result = action(args, book)

            if isinstance(result, tuple) and result[0] == "exit":
                print(result[1])
                save_data(book)
                break
            else:
                print(result)
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()