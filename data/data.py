import json
import os

def get_file_path(filename):
    return os.path.join(os.getcwd(), "data", filename)

def load_data(filename):
    path = get_file_path(filename)
    if os.path.exists(path):
        with open(path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_all_data(filename, data_list):
    path = get_file_path(filename)
    with open(path, 'w') as file:
        json.dump(data_list, file, indent=4)
    print(f"Data saved to {filename}")