from pydantic import BaseModel, Field, EmailStr, field_validator
from enum import Enum
from datetime import date
from pydantic_extra_types.phone_numbers import PhoneNumber
   
class Gender(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"

class Title(str, Enum):
    mr = "Mr"
    mrs = "Mrs"
    miss = "Miss"
    dr = "Doctor"
    prof = "Professor"

class FlightClass(str, Enum):
    economy = "Economy"
    business = "Business"
    first = "First"



class ContactDetails(BaseModel):
    title: Title = None
    first_name: str = Field(title="Customer First Name", description="First name of the customer", examples=["Seyi"], pattern="^[a-zA-Z]+$", min_length=3, max_length=50)
    last_name: str = Field(title="Customer Last Name", description="Last name of the customer", examples=["Oyewunmi"], pattern="^[a-zA-Z]+$", min_length=3, max_length=50)
    age: int = Field(title="Customer Age", description="Age of the customer", examples=[25], gt=0, lt=100)
    gender: Gender = None
    email: EmailStr
    phone_number: PhoneNumber = Field(title="Customer Phone Number", description="Phone number of the customer", examples=["+2348012345678"])

class FlightDetails(BaseModel):
    origin: str = Field(title="Flight Origin", description="Origin of the flight", examples=["Lagos"], min_length=3, max_length=50)
    destination: str = Field(title="Flight Destination", description="Destination of the flight", examples=["Abuja"], min_length=3, max_length=50)
    departure_date: date = Field(title="Flight Departure Date", description="Date of departure of the flight", examples=["2025-01-01"])
    flight_class: FlightClass

    @field_validator("departure_date")
    def validate_departure_date(cls, value):
        """
        Validate the departure date and raise a ValueError if it is in the past. 

        Args:
            cls: The class reference.
            value: The departure date to be validated.

        Returns:
            The validated departure date.
        """
        if value < date.today():
            raise ValueError("Departure date cannot be in the past")
        return value



class FlightBooking(BaseModel):
    contact_details: ContactDetails
    flight_details: FlightDetails
    seatpreference: str = Field(min_length=2, max_length=2, description="Seat preference of the passenger", examples=["A1"], title="Seat Preference",pattern="^[A-L][1-10]$")