import re


def interpret_natural_command(text: str):
    text = text.lower().strip()

    if text == "notes":
        return "show-notes", []

    m = re.search(r"(find-note|search-note) (\w+) (\w+)", text)
    if m:
        return "search_note", [m.group(2), m.group(3)]

    # -----------------------------
    # ADD CONTACT
    # add contact vasya with phone 123
    # create contact vasya 123
    # -----------------------------
    m = re.search(r"(add|create) contact (\w+) .*?(\d{5,})", text)
    if m:
        return "add", [m.group(2), m.group(3)]

    # -----------------------------
    # CHANGE PHONE
    # change vasya phone 123
    # -----------------------------
    m = re.search(r"(change|update) (\w+) phone (\d+)", text)
    if m:
        return "change", [m.group(2), m.group(3)]

    # -----------------------------
    # SHOW PHONE
    # vasya phone
    # show phone vasya
    # -----------------------------
    m = re.search(r"^show phone (\w+)$", text)
    if m:
        return "phone", [m.group(1)]

    m = re.search(r"^(\w+) phone$", text)
    if m:
        return "phone", [m.group(1)]

    # -----------------------------
    # SEARCH CONTACT
    # find vasya
    # search vasya
    # -----------------------------
    m = re.search(r"(find|search) (\w+)", text)
    if m:
        return "search", [m.group(2)]

    # -----------------------------
    # DELETE CONTACT
    # delete contact vasya
    # -----------------------------
    m = re.search(r"(delete|remove) contact (\w+)", text)
    if m:
        return "delete", [m.group(2)]

    # -----------------------------
    # ADD NOTE
    # add note buy milk for vasya
    # -----------------------------
    m = re.search(r"add note (.+) for (\w+)", text)
    if m:
        return "add-note", [m.group(2), m.group(1)]

    # -----------------------------
    # SHOW NOTES
    # show notes vasya
    # notes vasya
    # -----------------------------
    m = re.search(r"(show )?notes (\w+)", text)
    if m:
        return "show-notes", [m.group(2)]

    # -----------------------------
    # DELETE NOTE
    # delete note vasya 0
    # -----------------------------
    m = re.search(r"delete note (\w+) (\d+)", text)
    if m:
        return "delete-note", [m.group(1), m.group(2)]

    # -----------------------------
    # EDIT NOTE
    # edit note vasya 0 new text
    # -----------------------------
    m = re.search(r"edit note (\w+) (\d+) (.+)", text)
    if m:
        return "edit-note", [m.group(1), m.group(2), m.group(3)]

    # -----------------------------
    # BIRTHDAY
    # when is vasya birthday
    # show birthday vasya
    # -----------------------------
    m = re.search(r"(when is|show) (\w+) birthday", text)
    if m:
        return "show-birthday", [m.group(2)]

    # -----------------------------
    # UPCOMING BIRTHDAYS
    # show birthdays
    # get birthdays
    # -----------------------------
    if "show birthdays" in text or "get birthdays" in text:
        return "birthdays", []

    # -----------------------------
    # SHOW ALL CONTACTS
    # show contacts
    # list contacts
    # show all contacts
    # -----------------------------
    if "show contacts" in text or "list contacts" in text or "show all contacts" in text:
        return "all", []

    return None, None