class LibraryItem:
    def __init__(self, title, unique_id, location):
        self.title = title
        self._unique_id = unique_id  # Encapsulation: Protected attribute
        self.location = location

    def get_details(self):
        return f"{self.title} (ID: {self._unique_id})"

    def to_dict(self):
        return {
            "title": self.title,
            "unique_id": self._unique_id,
            "location": self.location,
            "type": "Generic"
        }

class Book(LibraryItem):
    def __init__(self, title, unique_id, location, pages):
        super().__init__(title, unique_id, location) # Inheritance
        self.pages = pages

    def to_dict(self):
        data = super().to_dict()
        data["pages"] = self.pages
        data["type"] = "Book"
        return data