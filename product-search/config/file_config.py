import os
import json


file = "products.json"
folder = "data"

file_path = os.path.join(folder, file)

products = []


def read_file():
    """
    Reads a file from the specified file path, loads the data as JSON, and returns the products.
    """

    global products
    global file_path

    with open(file_path, "r") as f:
        data = f.read()
        products = json.loads(data)
        print("File read successfully")
    return products