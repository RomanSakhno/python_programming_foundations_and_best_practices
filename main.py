"""CLI entry point for the address book assistant."""

from addressbook.address_book import AddressBook
from handlers.commands_registry import COMMANDS
from services.storage import load_data, save_data
from utils.parser import parse_input
from utils.nlp_engine import interpret_command, resolve_command


def main():
    """Run the main interactive command loop."""
    book: AddressBook = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = interpret_command(user_input, COMMANDS.keys())

        if not command:
            command, args = parse_input(user_input)

        resolved_command, suggestion = resolve_command(command, COMMANDS.keys())

        if resolved_command:
            command = resolved_command
        else:
            if suggestion:
                print(f"Unknown command '{command}'. Did you mean '{suggestion}'?")
            else:
                print("Invalid command.")
            continue

        action = COMMANDS.get(command)

        if not action:
            print(f"Command '{command}' not implemented.")
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