from addressbook.address_book import AddressBook
from handlers.commands_registry import COMMANDS
from services.storage import load_data, save_data
from utils.parser import parse_input
from utils.command_suggester import resolve_command
from utils.nlp_command_parser import detect_command_from_text
from utils.nlp_interpreter import interpret_natural_command


def main():
    book: AddressBook = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = interpret_natural_command(user_input)

        if not command:
            command, args = parse_input(user_input)

        if command not in COMMANDS:
            detected = detect_command_from_text(user_input, COMMANDS.keys())
            if detected:
                command = detected

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