import bcrypt
from uuid import uuid4
from datetime import datetime, timezone
from config.file_config import read_from_file, write_to_file


def create_new_user(user):
    """
    Create a new user and store their information in the database. 
    Params:
        user: User object containing username, email, and password
    Returns:
        If the user already exists, return an error message. Otherwise, return a success message.
    """

    username = user.username
    email = user.email
    unhashed_password = user.password

    # Generate a salt for password hashing
    salt_round = 15
    salt = bcrypt.gensalt(salt_round)

    # Hash the password using the generated salt
    hashedpassword = bcrypt.hashpw(unhashed_password.encode(), salt)
    password = hashedpassword.decode()

    users_db = read_from_file()
    new_user = {
        "_id": str(uuid4()),
        "username": username,
        "email": email,
        "password": password,
        "timestamps": {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat()
        }
    }

    
    if any(user["username"] == new_user["username"] or user["email"] == new_user["email"] for user in users_db):
        return{"error":"User already exists"}

    users_db.append(new_user)
    message = write_to_file(users_db)
    return {"message": message}




