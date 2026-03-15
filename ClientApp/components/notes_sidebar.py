from collections import defaultdict

def render_notes_by_tags(book):
    tags = defaultdict(list)

    for record in book.data.values():
        for note in record.notes:
            for tag in note["tags"]:
                tags[tag].append({
                    "contact": record.name.value,
                    "text": note["text"]
                })

    if not tags:
        return "<h4>📝 Notes</h4>No tagged notes."

    html = "<h4>📝 Notes by tags</h4>"

    for tag, notes in sorted(tags.items()):
        html += f'<div style="border:1px solid #ddd;border-radius:8px;padding:8px;margin-bottom:8px;background:#f9f9f9;"><strong>#{tag}</strong>'

        for note in notes:
            html += f'<div style="margin-top:4px;">📄 {note["text"]}<br><small>👤 {note["contact"]}</small></div>'

        html += '</div>'

    return html