import os
import json


file = "vehicles.json"
folder = "data"

file_path = os.path.join(folder, file)

cars = []


def read_file():
    """
    Reads a file from the specified file path, loads the data as JSON, and returns the products.
    """

    global cars
    global file_path

    with open(file_path, "r") as f:
        data = f.read()
        cars = json.loads(data)
        print("File read successfully")
    return cars