import os
import json



MOCKDB = []
file_directory = "data"
file = "users.json"
file_path = os.path.join(file_directory, file)


def create_file(): #pragma no cover
    """
    A function that creates a file if it does not exist and initializes it with MOCKDB data. 
    If the file exists but is empty, it populates it with MOCKDB data. 
    Reads the file and loads data into the global MOCKDB variable. 
    """
    global MOCKDB
    global file_directory

     
    if not os.path.exists(file_directory):
        os.mkdir(file_directory)

    if not os.path.exists(file_path):
        open(file_path, "x")

    if os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            f.write(json.dumps(MOCKDB))
            print("Successfully created file")

    with open(file_path, "r") as f:
        data = f.read()
        MOCKDB = json.loads(data)
        print("File read successfully")



def read_from_file(): #pragma no cover
    """
    Read data from the JSON file
    It uses the global variables 'file' and 'fakeusersDB'
    """
    # Read data from the JSON file
    # It uses the global variables 'file' and 'fakeusersDB'

    # Open the file in read mode
    with open(file_path, "r") as f:
        # Read the contents of the file
        data = f.read()
        # Parse the contents as a JSON object
        # and assign it to the global variable 'fakeusersDB'
        MOCKDB = json.loads(data)

    # Return the contents of the JSON file as a dictionary
    return MOCKDB


def write_to_file(data): #pragma no cover
    """
    write_to_file function writes data to a file.

    Parameters:
        data (any): The data to be written to the file.

    Returns:
        dict: A dictionary with a message indicating the writing operation status.
    """

    MOCKDB = data

    with open(file_path, "w") as f:
        f.write(json.dumps(MOCKDB, indent=4))
        return {"message": "Successfully written to file"}
    
