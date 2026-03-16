from handlers.commands_registry import COMMANDS
from utils.command_metadata import COMMAND_METADATA


COMMAND_ALIASES = {
    "add": ["create", "new", "insert"],
    "change": ["edit", "update", "modify"],
    "phone": ["number", "contact-phone"],
    "all": ["list", "contacts"],
    "delete": ["remove", "del"],
    "add-note": ["note", "write-note"],
    "show-notes": ["notes", "list-notes"],
    "search-note": ["find-note", "search_notes", "tag"],
    "edit-note": ["change-note", "update-note"],
    "delete-note": ["remove-note"],
    "search": ["find", "lookup"],
    "exit": ["close", "quit"],
    "birthdays": ["upcoming", "upcoming birthdays"],
    "birthdays-in": ["birthdays in", "within"],
}

def get_command_suggestions(user_input: str, limit: int = 5):
    user_input = user_input.lower().strip()

    suggestions = []

    for command in COMMANDS.keys():
        aliases = COMMAND_ALIASES.get(command, [])
        meta_aliases = COMMAND_METADATA.get(command, {}).get("aliases", [])

        all_names = [command] + aliases + meta_aliases

        for name in all_names:
            if name.startswith(user_input):
                suggestions.append(command)
                break

    return sorted(set(suggestions))[:limit]