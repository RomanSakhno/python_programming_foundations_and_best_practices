def record_to_html(record):
    """Convert Record object to styled HTML."""
    html = f"<h3>📇 {record.name.value}</h3>"

    # Phones
    if record.phones:
        phones = ", ".join(p.value for p in record.phones)
    else:
        phones = "Not set"
    html += f"<p>📞 Phones: {phones}</p>"

    # Email
    email = record.email or "Not set"
    html += f"<p>✉ Email: {email}</p>"

    # Birthday
    birthday = str(record.birthday) if record.birthday else "Not set"
    html += f"<p>🎂 Birthday: {birthday}</p>"

    # Notes
    if record.notes:
        html += "<h4>📝 Notes:</h4><ul>"
        for i, note in enumerate(record.notes, 1):
            tags = ", ".join(note["tags"]) if note["tags"] else "No tags"
            html += f"<li>{i}. 📄 {note['text']}<br>🔖 Tags: {tags}</li>"
        html += "</ul>"
    else:
        html += "<p>📝 Notes: None</p>"

    return html


def notes_to_html(record, tag=None):
    """Render notes filtered by tag as HTML."""
    notes = record.notes
    if tag:
        notes = [n for n in notes if tag.lower() in [t.lower() for t in n["tags"]]]
    if not notes:
        return f"<p>No notes{' with tag '+tag if tag else ''}.</p>"

    html = f"<h4>📝 Notes{' with tag '+tag if tag else ''} for {record.name.value}</h4><ul>"
    for i, note in enumerate(notes, 1):
        tags = ", ".join(note["tags"]) if note["tags"] else "No tags"
        html += f"<li>{i}. 📄 {note['text']}<br>🔖 Tags: {tags}</li>"
    html += "</ul>"
    return html