from fastapi import APIRouter, Response
from models.user_model import UserModel
from controllers.user_controller import create_new_user


router = APIRouter(prefix='/api', tags=['User Registration'])


@router.post('/register')
async def register_user(userdata: UserModel, response: Response):
    """
    Register a new user with the provided user data and handle any existing user conflicts.
    
    Parameters:
    - userdata: UserModel object containing user data
    - response: Response object for handling HTTP responses
    
    Returns:
    - Dictionary with an error message if user creation fails, or a success message if user is created successfully
    """
 
    message = create_new_user(userdata)

    if isinstance(message, dict):
        if "error" in message:
            response.status_code = 409  # Conflict: User already exists
            return {"error": message["error"]}
        else:
            response.status_code = 201  # Created: User created successfully
            return {"message": "Successfully created"}