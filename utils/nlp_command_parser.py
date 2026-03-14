def detect_command_from_text(text: str, commands: list[str]) -> str | None:

    text = text.lower()

    keywords_map = {
        "add": ["add", "create", "new", "insert"],
        "change": ["change", "edit", "update", "modify"],
        "delete": ["delete", "remove"],
        "search": ["search", "find", "lookup"],
        "phone": ["phone", "number"],
        "all": ["all", "list", "contacts", "show"],
        "add-note": ["note", "write-note"],
        "show-notes": ["notes", "list-notes"],
        "search_note": ["find-note", "search-notes", "tag"],
        "delete-note": ["remove-note"],
    }

    for command, keywords in keywords_map.items():
        for word in keywords:
            if word in text and command in commands:
                return command

    return None