from src.items import Book
from data.data import save_record


def main():
    print("--- Add a New Book ---")
    title = input("Enter book title: ")
    try:
        unique_id = int(input("Enter unique ID: "))
    except ValueError:
        print("ID must be a number.")
        return

    location = input("Enter location: ")
    pages = input("Enter page count: ")

    # Create the object (Logic Layer)
    new_book = Book(title, unique_id, location, pages)

    # Convert to dictionary and save (Data Layer)
    success, message = save_record(new_book.to_dict())
    print(message)


if __name__ == "__main__":
    main()