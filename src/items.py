class LibraryItem:
    def __init__(self, title, unique_id, location, item_type):
        self.title = title
        self.unique_id = unique_id
        self.location = location
        self.item_type = item_type
        self.is_borrowed = False

    def calculate_fine(self, days_kept):
        return 0

    def to_dict(self):
        return {
            "title": self.title,
            "unique_id": self.unique_id,
            "location": self.location,
            "type": self.item_type,
            "is_borrowed": self.is_borrowed
        }


class Book(LibraryItem):
    def __init__(self, title, unique_id, location, pages):
        super().__init__(title, unique_id, location, "Book")
        self.pages = pages
        self.loan_period = 21
        self.daily_fine = 0.50

    def calculate_fine(self, days_kept):
        if days_kept > self.loan_period:
            return (days_kept - self.loan_period) * self.daily_fine
        return 0

    def to_dict(self):
        data = super().to_dict()
        data["pages"] = self.pages
        return data


class DVD(LibraryItem):
    def __init__(self, title, unique_id, location, runtime):
        super().__init__(title, unique_id, location, "DVD")
        self.runtime = runtime
        self.loan_period = 7
        self.daily_fine = 2.00

    def calculate_fine(self, days_kept):
        if days_kept > self.loan_period:
            return (days_kept - self.loan_period) * self.daily_fine
        return 0

    def to_dict(self):
        data = super().to_dict()
        data["runtime"] = self.runtime
        return data


class Magazine(LibraryItem):
    def __init__(self, title, unique_id, location, issue):
        super().__init__(title, unique_id, location, "Magazine")
        self.issue = issue
        self.loan_period = 7
        self.daily_fine = 1.00

    def calculate_fine(self, days_kept):
        if days_kept > self.loan_period:
            return (days_kept - self.loan_period) * self.daily_fine
        return 0

    def to_dict(self):
        data = super().to_dict()
        data["issue"] = self.issue
        return data