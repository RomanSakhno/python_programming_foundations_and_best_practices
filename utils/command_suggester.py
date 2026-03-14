import difflib

COMMAND_ALIASES = {
    "add": ["create", "new", "insert"],
    "change": ["edit", "update", "modify"],
    "phone": ["number", "contact-phone"],
    "all": ["list", "contacts"],
    "delete": ["remove", "del"],
    "add-note": ["note", "write-note"],
    "show-notes": ["notes", "list-notes"],
    "search_note": ["find-note", "search-notes", "tag"],
    "edit-note": ["change-note", "update-note"],
    "delete-note": ["remove-note"],
    "search": ["find", "lookup"],
    "exit": ["close", "quit"]
}

def resolve_command(user_command: str, available_commands: list[str]):
    user_command = user_command.lower()

    if user_command in available_commands:
        return user_command, None

    for command, aliases in COMMAND_ALIASES.items():
        if user_command in aliases:
            return command, None

    matches = difflib.get_close_matches(
        user_command,
        available_commands,
        n=1,
        cutoff=0.6
    )

    if matches:
        return None, matches[0]

    return None, None