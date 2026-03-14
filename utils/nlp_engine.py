import re
import difflib
from utils.command_metadata import COMMAND_METADATA


def interpret_command(text: str, available_commands):
    text = text.lower().strip()
    parts = text.split()

    # 1️⃣ прямой CLI
    if parts and parts[0] in available_commands:
        return parts[0], parts[1:]

    # 2️⃣ NLP regex extraction
    for command, meta in COMMAND_METADATA.items():
        if command not in available_commands:
            continue
        for pattern in meta.get("patterns", []):
            m = re.search(pattern, text)
            if m:
                return command, list(m.groups())

    # 3️⃣ alias detection
    for command, meta in COMMAND_METADATA.items():
        if command not in available_commands:
            continue
        for alias in meta.get("aliases", []):
            if parts and parts[0] == alias:
                return command, parts[1:]

    return None, []


def resolve_command(user_command: str, available_commands: list[str]):
    user_command = user_command.lower()

    if user_command in available_commands:
        return user_command, None

    available_set = set(available_commands)

    for command, aliases in COMMAND_METADATA.items():
        if command not in available_set:
            continue

        if user_command in aliases:
            return command, None

    matches = difflib.get_close_matches(
        user_command,
        available_commands,
        n=1,
        cutoff=0.6
    )

    if matches:
        return matches[0], None

    return None, None