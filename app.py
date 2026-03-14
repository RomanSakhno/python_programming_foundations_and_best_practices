import streamlit as st
from handlers.commands_registry import COMMANDS
from services.storage import load_data, save_data
from utils.nlp_engine import interpret_command, resolve_command
from utils.parser import parse_input
from utils.html_renderer import record_card_html, notes_card_html

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
    if not action:
        st.warning(f"Command '{command}' not implemented")
        st.stop()

    result = action(args, book)

    if command in ["show-notes", "search-note"]:
        name = args[0]
        tag = args[1] if len(args) > 1 else None
        record = book.find(name)
        if record:
            html = notes_card_html(record, tag)
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.warning("Contact not found")

    elif command in ["phone", "show-birthday"]:
        html = f"""
                    <div style="
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        padding: 10px;
                        margin-top: 10px;
                        background-color: #f9f9f9;
                        font-size: 16px;
                    ">
                        <strong>{result}</strong>
                    </div>
                    """
        st.markdown(html, unsafe_allow_html=True)

    elif command in ["find", "search"]:
        record = book.find(args[0])
        if record:
            html = record_card_html(record)
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.warning("Contact not found")

    elif command in ["all"]:
        html = "".join(record_card_html(r) for r in book.data.values())
        st.markdown(html, unsafe_allow_html=True)

    elif command in ["birthdays", "birthdays-in"]:
        st.text(result)

    elif isinstance(result, tuple) and result[0] == "exit":
        st.write(result[1])
    else:
        st.write(result)

    save_data(book)