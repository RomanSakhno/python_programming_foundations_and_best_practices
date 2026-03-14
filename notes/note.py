"""Simple note object used by example notes manager."""


class Note:
    """Represents a single plain-text note."""

    def __init__(self, text):
        self.text = text