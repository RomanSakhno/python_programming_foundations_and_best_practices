import streamlit as st
from handlers.commands_registry import COMMANDS
from services.storage import load_data, save_data
from utils.nlp_engine import interpret_command, resolve_command
from utils.parser import parse_input
from ClientApp.components.html_renderer import record_card_html, notes_card_html
from ClientApp.components.birthday_calendar import render_birthday_calendar
from ClientApp.components.notes_sidebar import render_notes_by_tags
from ClientApp.components.weather_widget import render_weather
from utils.command_suggester import get_command_suggestions
from ClientApp.components.command_helper import render_command_helper
from collections import defaultdict

st.set_page_config(layout="wide")
main, right_spacer = st.columns([4, 1])

book = load_data()

# ---- Sidebar ----
st.sidebar.markdown(render_birthday_calendar(book), unsafe_allow_html=True)
st.sidebar.markdown(render_notes_by_tags(book), unsafe_allow_html=True)

with right_spacer:
    latitude = 36.7213
    longitude = -4.4217
    weather_html = render_weather(latitude, longitude)
    st.markdown(weather_html, unsafe_allow_html=True)

with main:
    st.title("📇 Address Book Assistant")

    if "show_suggestions" not in st.session_state:
        st.session_state.show_suggestions = False
    if "last_input" not in st.session_state:
        st.session_state.last_input = ""

    user_input = st.text_input("Enter command", key="user_input")

    if user_input != st.session_state.last_input:
        st.session_state.show_suggestions = False
        st.session_state.last_input = user_input

    tab_pressed = st.button("Tab", key="show_tab_suggestions")
    if tab_pressed and user_input:
        st.session_state.show_suggestions = True

    if st.session_state.show_suggestions:
        suggestions = get_command_suggestions(user_input)
        if suggestions:
            st.markdown(render_command_helper(suggestions), unsafe_allow_html=True)
        st.stop()

    command, args = interpret_command(user_input, COMMANDS.keys())
    if not command:
        command, args = parse_input(user_input)

    if command is None:
        st.info("⏳ Enter a command")
        st.stop()


    action = COMMANDS.get(command)
    if not action:
        st.warning(f"Command '{command}' not implemented")
    else:
        try:
            result = action(args, book)
        except IndexError:
            result = "Error: missing arguments"

        if command in ["show-notes", "search-note"]:
            if len(args) < 1:
                st.info("⏳ Enter name (and optionally tag) to show notes")
            else:
                name = args[0]
                tag = args[1] if len(args) > 1 else None
                record = book.find(name)
                if record:
                    html = notes_card_html(record, tag)
                    st.markdown(html, unsafe_allow_html=True)
                else:
                    st.warning("Contact not found")

        elif command in ["phone", "show-birthday"]:
            if len(args) < 1:
                st.info("⏳ Enter name to show info")
            else:
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
            if len(args) < 1:
                st.info("⏳ Enter name to search")
            else:
                record = book.find(args[0])
                if record:
                    html = record_card_html(record)
                    st.markdown(html, unsafe_allow_html=True)
                else:
                    st.warning("Contact not found")

        elif command in ["all"]:
            contacts_by_letter = defaultdict(list)
            for record in book.data.values():
                first_letter = record.name.value[0].upper()
                contacts_by_letter[first_letter].append(record)

            html = ""
            for letter in sorted(contacts_by_letter.keys()):
                html += f'<h2 style="margin-top:20px; border-bottom:1px solid #ccc;">{letter}</h2>'
                for record in sorted(contacts_by_letter[letter], key=lambda r: r.name.value.lower()):
                    html += record_card_html(record)

            st.markdown(html, unsafe_allow_html=True)

        elif command in ["birthdays", "birthdays-in"]:
            st.text(result)

        elif isinstance(result, tuple) and result[0] == "exit":
            st.write(result[1])
        else:
            st.write(result)

    save_data(book)