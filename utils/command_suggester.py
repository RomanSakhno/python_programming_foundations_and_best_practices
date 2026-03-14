import difflib

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