def record_to_html(record):
    """Render a Record as styled HTML with capitalized name."""
    name = record.name.value.upper()  # полностью заглавные буквы
    html = f"<h3>📇 {name}</h3>"

    # Phones
    phones = ", ".join(p.value for p in record.phones) if record.phones else "Not set"
    html += f"<p>📞 Phones: {phones}</p>"

    # Email
    email = record.email.value if record.email else "Not set"
    html += f"<p>✉ Email: {email}</p>"

    # Birthday
    birthday = record.birthday.value.strftime('%d.%m.%Y') if record.birthday else "Not set"
    html += f"<p>🎂 Birthday: {birthday}</p>"

    # Notes
    if record.notes:
        html += "<h4>📝 Notes:</h4><ul>"
        for i, note in enumerate(record.notes, 1):
            tags = ", ".join(note["tags"]) if note["tags"] else "No tags"
            html += f"<li>{i}. 📄 {note['text']}<br>🏷 Tags: {tags}</li>"
        html += "</ul>"
    else:
        html += "<p>📝 Notes: None</p>"

    return html


def notes_to_html(record, tag=None):
    """Render notes optionally filtered by tag with capitalized name."""
    name = record.name.value.upper()
    notes = record.notes
    if tag:
        tag_lower = tag.lower()
        notes = [n for n in notes if any(t.lower() == tag_lower for t in n["tags"])]
    if not notes:
        return f"<p>No notes{' with tag '+tag if tag else ''}.</p>"

    html = f"<h4>📝 Notes{' with tag '+tag if tag else ''} for {name}</h4><ul>"
    for i, note in enumerate(notes, 1):
        tags = ", ".join(note["tags"]) if note["tags"] else "No tags"
        html += f"<li>{i}. 📄 {note['text']}<br>🏷 Tags: {tags}</li>"
    html += "</ul>"
    return html


def record_card_html(record):
    """Render a contact as a nice HTML card with capitalized name and notes."""
    name = record.name.value.upper()
    phones = "; ".join(p.value for p in record.phones) if record.phones else "Not set"
    email = record.email.value if record.email else "Not set"
    birthday = record.birthday.value.strftime('%d.%m.%Y') if record.birthday else "Not set"

    html = f"""
    <div style="
        border: 2px solid #4CAF50; 
        border-radius: 12px; 
        padding: 12px; 
        margin-bottom: 12px; 
        background-color: #f9fff9;
    ">
        <h3 style="margin:0;">📇 {name}</h3>
        <p style="margin:2px 0;">📞 Phones: {phones}</p>
        <p style="margin:2px 0;">✉ Email: {email}</p>
        <p style="margin:2px 0;">🎂 Birthday: {birthday}</p>
    """

    if record.notes:
        html += "<h4>📝 Notes:</h4><ul>"
        for i, note in enumerate(record.notes, 1):
            tags = ", ".join(note["tags"]) if note["tags"] else "No tags"
            html += f"<li>{i}. 📄 {note['text']}<br>🏷 Tags: {tags}</li>"
        html += "</ul>"
    else:
        html += "<p>📝 Notes: None</p>"

    html += "</div>"
    return html


def notes_card_html(record, tag=None):
    """Render notes card optionally filtered by tag with capitalized name."""
    name = record.name.value.upper()
    notes = record.notes
    if tag:
        tag_lower = tag.lower()
        notes = [n for n in notes if any(t.lower() == tag_lower for t in n["tags"])]

    if not notes:
        return f"<div style='padding:10px; background:#fff3f3; border-radius:8px;'>No notes{' with tag '+tag if tag else ''}.</div>"

    html = f"""
    <div style="
        border: 2px solid #2196F3; 
        border-radius: 12px; 
        padding: 12px; 
        margin-bottom: 12px; 
        background-color: #f0f8ff;
    ">
        <h4>📝 Notes{' with tag '+tag if tag else ''} for {name}</h4>
        <ul>
    """
    for i, note in enumerate(notes, 1):
        tags = ", ".join(note["tags"]) if note["tags"] else "No tags"
        html += f"<li>{i}. 📄 {note['text']}<br>🏷 Tags: {tags}</li>"
    html += "</ul></div>"
    return html