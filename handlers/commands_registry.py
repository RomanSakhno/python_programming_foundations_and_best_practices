from .contact_handlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all,
    search_contacts,
    delete_contact,
    edit_email,
    edit_name,
    delete_phone
)

from .birthday_handlers import (
    add_birthday,
    show_birthday,
    birthdays,
    birthdays_in,
)

from .notes_handlers import (
    add_note,
    edit_note,
    delete_note,
    show_notes,
    search_notes
)

COMMANDS = {
    "close": lambda args, book: ("exit", "Good bye!"),
    "exit": lambda args, book: ("exit", "Good bye!"),
    "hello": lambda args, book: ("ok", "How can I help you?"),
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
    "birthdays-in": birthdays_in,
    "search": search_contacts,
    "delete": delete_contact,
    "add-note": add_note,
    "edit-note": edit_note,
    "delete-note": delete_note,
    "show-notes": show_notes,
    "search_note": search_notes,
    "edit-email": edit_email,
    "edit-name": edit_name,
    "delete-phone": delete_phone,
}