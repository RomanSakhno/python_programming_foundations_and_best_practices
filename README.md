# 📇 Address Book Assistant

Address Book Assistant is an interactive application for managing contacts and notes, built with **Python** and **Streamlit**.

The app allows you to manage contacts using text commands, store notes with tags, track birthdays, and display current weather.
# 📁 Project Structure
````
address-book-assistant/
├── ClientApp/ # Main Streamlit app
│ ├── app.py # Entry point for the Streamlit app
│ ├── main.py # Layout and app initialization
│ └── components/ # Reusable UI components
│ ├── html_renderer.py # Render contact & note cards
│ ├── birthday_calendar.py# Birthday calendar
│ ├── notes_sidebar.py # Notes sidebar
│ └── weather_widget.py # Weather widget
├── handlers/ # Command handlers & registry
├── services/ # Data storage and business logic
├── utils/ # Helper utilities (parsing, NLP, HTML)
├── data/ # Stored contacts data
├── notes/ # Stored notes data
├── pyproject.toml # Build configuration
└── README.md # Project documentation
````

---

# 🚀 Features

- 📇 Contact management
- 📞 Multiple phone numbers per contact
- 🎂 Birthday calendar
- 📝 Notes with tags
- 🔎 Search contacts
- 🌤 Weather by current geolocation
- 🤖 Natural language support for commands
- 📚 Alphabetical sorting of contacts (like a real phone book)

---

# 🖥 Interface

The app has three main sections:

### Main panel
The main interface for entering commands and displaying contacts.

### Sidebar
- Birthday calendar
- Notes by tags

### Right panel
- Compact weather widget

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/address-book-assistant.git
cd address-book-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:
Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install the project:

```bash
pip install -e .
```

# ▶️ Run Application

After installation, you can run the app from any folder:

```bash
# Activate virtual environment (if not already active)
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

# Run the Address Book Assistant
address-book
```