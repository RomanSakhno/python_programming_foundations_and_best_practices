def render_command_helper(commands):
    if not commands:
        return ""

    html = """
    <div style="
        border:1px solid #ddd;
        border-radius:8px;
        padding:10px;
        margin-top:6px;
        background:#fafafa;
        font-size:14px;
    ">
    <strong>Suggestions:</strong><br>
    """

    for cmd in commands:
        html += f"• <code>{cmd}</code><br>"

    html += "</div>"

    return html