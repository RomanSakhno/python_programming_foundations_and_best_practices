import re

COMMAND_METADATA = {
    "birthdays-in": {
        "aliases": ["birthdays in", "within", "within days"],
        "patterns": [
            r"birthday(?:s)?\s+in\s+(\d+)",
            r"within\s+\w*\s*(\d+)",
            r"birthdays-in\s+(\d+)",
        ],
    },

    "birthdays": {
        "aliases": ["birthdays", "upcoming birthdays"],
        "patterns": [
            r"show birthdays",
            r"get birthdays",
        ],
    },

    "add": {
        "aliases": ["create", "new", "insert"],
        "patterns": [
            r"(?:add|create) contact (\w+) .*?(\d{5,})",
        ],
    },

    "change": {
        "aliases": ["edit", "update", "modify"],
        "patterns": [
            r"(?:change|update) (\w+) phone (\d+)",
        ],
    },

    "phone": {
        "aliases": ["number"],
        "patterns": [
            r"show phone (\w+)",
            r"(\w+) phone",
        ],
    },

    "search": {
        "aliases": ["find", "lookup"],
        "patterns": [
            r"(?:find|search) (\w+)",
        ],
    },

    "delete": {
        "aliases": ["remove"],
        "patterns": [
            r"(?:delete|remove) contact (\w+)",
        ],
    },

    "add-note": {
        "aliases": ["note", "write-note"],
        "patterns": [
            r"add note (.+) for (\w+)",
        ],
    },

    "show-notes": {
        "aliases": ["notes"],
        "patterns": [
            r"(?:show )?notes (\w+)",
        ],
    },

    "delete-note": {
        "aliases": ["remove-note"],
        "patterns": [
            r"delete note (\w+) (\d+)",
        ],
    },

    "edit-note": {
        "aliases": ["change-note", "update-note"],
        "patterns": [
            r"edit note (\w+) (\d+) (.+)",
        ],
    },

    "all": {
        "aliases": ["list", "contacts"],
        "patterns": [
            r"show contacts",
            r"list contacts",
            r"show all contacts",
        ],
    },

    "search-note": {
        "aliases": ["find-note", "search_notes", "tag"],
        "patterns": [
            r"(?:find|search)[-_ ]note (\w+) (\w+)",
        ]
    }
}