from collections import defaultdict

def render_notes_by_tags(book):
    """Render all notes grouped by tags as styled HTML."""
    tags = defaultdict(list)

    for record in book.data.values():
        for note in record.notes:
            for tag in note["tags"]:
                tags[tag].append({
                    "contact": record.name.value.title(),  # Title Case вместо ВСЕХ БУКВ
                    "text": note["text"]
                })

    if not tags:
        return "<h4>📝 Notes</h4>No tagged notes."

    html = "<h4>📝 Notes by tags</h4>"

    for tag, notes in sorted(tags.items()):
        html += (
            '<div style="border:2px solid #ccc;border-radius:8px;'
            'padding:8px;margin-bottom:12px;background-color:#f9f9f9;">'
            f'<strong>#{tag.upper()}</strong>'
        )

        for note in notes:
            html += (
                '<div style="margin-top:6px;padding-left:6px;">'
                f'📄 {note["text"]}<br>'
                f'<small>👤 {note["contact"]}</small>'
                '</div>'
            )

        html += '</div>'

    return html