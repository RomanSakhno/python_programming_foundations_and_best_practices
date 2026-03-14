import streamlit as st
from handlers.commands_registry import COMMANDS
from services.storage import load_data, save_data
from utils.nlp_engine import interpret_command, resolve_command
from utils.parser import parse_input
from utils.html_renderer import record_to_html, notes_to_html

book = load_data()

st.title("📇 Address Book Assistant")

user_input = st.text_input("Enter command")

if user_input:
    command, args = interpret_command(user_input, COMMANDS.keys())

    if not command:
        command, args = parse_input(user_input)

    resolved_command, suggestion = resolve_command(command, COMMANDS.keys())

    if resolved_command:
        command = resolved_command
    else:
        if suggestion:
            st.warning(f"Did you mean '{suggestion}'?")
        else:
            st.error("Invalid command")
        st.stop()

    action = COMMANDS.get(command)
    result = action(args, book)

    if command in ["show-notes", "search-note"]:
        name = args[0]
        tag = args[1] if len(args) > 1 else None
        record = book.find(name)
        if record:
            html = notes_to_html(record, tag)
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.warning("Contact not found")
    elif command in ["phone", "all", "birthdays", "birthdays-in", "show-birthday"]:
        if command == "all":
            html = "".join(record_to_html(r) for r in book.data.values())
            st.markdown(html, unsafe_allow_html=True)
        elif command in ["birthdays", "birthdays-in"]:
            st.text(result)
        else:
            record = book.find(args[0])
            if record:
                st.markdown(record_to_html(record), unsafe_allow_html=True)
            else:
                st.warning("Contact not found")
    else:
        st.write(result)

    save_data(book)