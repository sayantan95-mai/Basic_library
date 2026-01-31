# data/data.py
import json
import os


def save_record(record_dict):
    filename = os.path.join(os.getcwd(), "data", "library_data.json")

    # Load existing data
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                library_list = json.load(file)
            except json.JSONDecodeError:
                library_list = []
    else:
        library_list = []

    # Check for duplicates using the ID passed in the dictionary
    duplicate_found = any(
        item.get("unique_id") == record_dict["unique_id"]
        for item in library_list
    )

    if duplicate_found:
        return False, "Error: Item with this ID already exists."

    library_list.append(record_dict)
    with open(filename, 'w') as file:
        json.dump(library_list, file, indent=4)

    return True, "Item saved successfully!"