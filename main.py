from src.items import Book, DVD, Magazine
from src.users import Member
from data.data import load_data, save_all_data

# Global lists to hold objects in memory
library_items = []
members = []


def load_system():
    # Load Items
    raw_items = load_data("library_data.json")
    for item in raw_items:
        if item["type"] == "Book":
            obj = Book(item["title"], item["unique_id"], item["location"], item.get("pages"))
        elif item["type"] == "DVD":
            obj = DVD(item["title"], item["unique_id"], item["location"], item.get("runtime"))
        elif item["type"] == "Magazine":
            obj = Magazine(item["title"], item["unique_id"], item["location"], item.get("issue"))

        obj.is_borrowed = item["is_borrowed"]
        library_items.append(obj)

    # Load Members
    raw_members = load_data("users.json")
    for m in raw_members:
        mem = Member(m["name"], m["user_id"])
        mem.borrowed_items = m["borrowed_items"]
        members.append(mem)


def save_system():
    item_data = [item.to_dict() for item in library_items]
    save_all_data("library_data.json", item_data)

    member_data = [m.to_dict() for m in members]
    save_all_data("users.json", member_data)


def find_item(unique_id):
    for item in library_items:
        if item.unique_id == unique_id:
            return item
    return None


def find_member(user_id):
    for m in members:
        if m.user_id == user_id:
            return m
    return None


def add_item():
    print("\nSelect Type: 1. Book  2. DVD  3. Magazine")
    choice = input("Choice: ")
    title = input("Title: ")
    uid = int(input("Unique ID: "))
    loc = input("Location: ")

    if choice == "1":
        pages = input("Pages: ")
        library_items.append(Book(title, uid, loc, pages))
    elif choice == "2":
        run = input("Runtime: ")
        library_items.append(DVD(title, uid, loc, run))
    elif choice == "3":
        issue = input("Issue Date: ")
        library_items.append(Magazine(title, uid, loc, issue))
    print("Item Added!")


def borrow_process():
    uid = int(input("Enter User ID: "))
    member = find_member(uid)
    if not member:
        print("Member not found.")
        return

    iid = int(input("Enter Item ID: "))
    item = find_item(iid)
    if not item:
        print("Item not found.")
        return

    if item.is_borrowed:
        print("Item is already borrowed.")
    else:
        item.is_borrowed = True
        member.borrow(iid)
        print(f"Successfully borrowed {item.title}")


def return_process():
    uid = int(input("Enter User ID: "))
    member = find_member(uid)
    if not member:
        print("Member not found.")
        return

    iid = int(input("Enter Item ID: "))
    item = find_item(iid)

    if member.return_item(iid):
        item.is_borrowed = False
        days = int(input("How many days was it kept? "))
        fine = item.calculate_fine(days)
        if fine > 0:
            print(f"OVERDUE! Fine Amount: ${fine:.2f}")
        else:
            print("Returned on time. No fine.")
    else:
        print("This user does not have that item.")


def main():
    load_system()
    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add Item")
        print("2. Add Member")
        print("3. Borrow Item")
        print("4. Return Item")
        print("5. View All Items")
        print("6. Exit & Save")

        choice = input("Select: ")

        match choice:
            case "1":
                add_item()
            case "2":
                name = input("Name: ")
                uid = int(input("User ID: "))
                members.append(Member(name, uid))
                print("Member Added!")
            case "3":
                borrow_process()
            case "4":
                return_process()
            case "5":
                for i in library_items:
                    status = "Borrowed" if i.is_borrowed else "Available"
                    print(f"[{i.item_type}] {i.title} (ID: {i.unique_id}) - {status}")
            case "6":
                save_system()
                break
            case _:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()