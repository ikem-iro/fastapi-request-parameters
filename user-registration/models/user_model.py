from pydantic import BaseModel, EmailStr, Field, field_validator
import re

class UserModel(BaseModel):
    username: str = Field(description="Username must be between 3 and 20 characters long", min_length=3, max_length=50, pattern="^[a-zA-Z ]+$")
    email: EmailStr
    password: str = Field(description="Password must be at least 8 characters long and contain at least one capital letter, one number and one special character", min_length=8, max_length=20)

    @field_validator("password")
    def validate_password(cls, value):
        """
        Validates the password input based on a specified regex pattern.
        
        Parameters:
            cls (class): The class object.
            value (str): The password string to be validated.
        
        Returns:
            str: The validated password if it meets the criteria.
        
        Raises:
            ValueError: If the password does not meet the stipulated criteria.
        """
     
        password_regex = r"((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,20})"
        if not re.match(password_regex, value):
            raise ValueError("Password does not meet stipulated criteria")
        return value

