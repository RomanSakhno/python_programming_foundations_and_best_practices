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

def record_card_html(record):
    """Render a contact as a nice HTML card with notes."""
    html = f"""
    <div style="
        border: 2px solid #4CAF50; 
        border-radius: 12px; 
        padding: 12px; 
        margin-bottom: 12px; 
        background-color: #f9fff9;
    ">
        <h3 style="margin:0;">📇 {record.name.value}</h3>
        <p style="margin:2px 0;">📞 Phones: {'; '.join(p.value for p in record.phones) if record.phones else 'Not set'}</p>
        <p style="margin:2px 0;">✉ Email: {record.email if record.email else 'Not set'}</p>
        <p style="margin:2px 0;">🎂 Birthday: {record.birthday if record.birthday else 'Not set'}</p>
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
    """Render notes filtered by tag as HTML card."""
    notes = record.notes
    if tag:
        notes = [n for n in notes if tag.lower() in [t.lower() for t in n["tags"]]]
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
        <h4>📝 Notes{' with tag '+tag if tag else ''} for {record.name.value}</h4>
        <ul>
    """
    for i, note in enumerate(notes, 1):
        tags = ", ".join(note["tags"]) if note["tags"] else "No tags"
        html += f"<li>{i}. 📄 {note['text']}<br>🏷 Tags: {tags}</li>"
    html += "</ul></div>"
    return html