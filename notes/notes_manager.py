"""In-memory manager for a simple list of notes."""


class NotesManager:
    """Provide add/delete/search operations on a list of notes."""

    def __init__(self):
        self.notes = []

    def add(self, text):
        """Append a new note."""
        self.notes.append(text)

    def delete(self, index):
        """Delete a note at the given index."""
        self.notes.pop(index)

    def search(self, keyword):
        """Return notes containing the given keyword (case-insensitive)."""
        return [n for n in self.notes if keyword.lower() in n.lower()]