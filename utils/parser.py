"""Helpers for parsing user input into commands and arguments."""


def parse_input(user_input: str):
    """Split raw input into a lowercase command and list of arguments."""

    cmd, *args = user_input.strip().split()

    return cmd.lower(), args