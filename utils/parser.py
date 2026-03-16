"""Helpers for parsing user input into commands and arguments."""


def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        return None, []
    cmd, *args = parts
    return cmd.lower(), args