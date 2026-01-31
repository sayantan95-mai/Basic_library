class Member:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_items = [] # Stores Item IDs

    def borrow(self, item_id):
        if item_id not in self.borrowed_items:
            self.borrowed_items.append(item_id)
            return True
        return False

    def return_item(self, item_id):
        if item_id in self.borrowed_items:
            self.borrowed_items.remove(item_id)
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "borrowed_items": self.borrowed_items,
            "type": "Member"
        }