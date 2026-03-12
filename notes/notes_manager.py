class NotesManager:

    def __init__(self):
        self.notes = []

    def add(self, text):
        self.notes.append(text)

    def delete(self, index):
        self.notes.pop(index)

    def search(self, keyword):
        return [n for n in self.notes if keyword.lower() in n.lower()]