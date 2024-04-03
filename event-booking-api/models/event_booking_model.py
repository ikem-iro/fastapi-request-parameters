from pydantic import BaseModel, Field, EmailStr, validator
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import timedelta, datetime
from enum import Enum

class TicketType(str, Enum):
    vip = "VIP"
    regular = "Regular"

class Attendee(BaseModel):
    name: str = Field(title="Attendee Name", description="Name of the attendee", examples=["Seyi Oyewunmi"], min_length=3, max_length=50, pattern="^[a-zA-Z\s]+$")
    email: EmailStr
    phone_number: PhoneNumber = Field(title="Attendee Phone Number", description="Phone number of the attendee", examples=["+2348012345678"])

class Date(BaseModel):
    event_date: str = Field(title="Event Date", description="Date of the event", examples=["2024-01-01"])
    booking_date: str = Field(title="Booking Date", description="Date of booking of the event", examples=["2025-01-01"])

    @validator('booking_date', pre=True)
    def validate_booking_date(cls, value, values, **kwargs):
        """
        Validate the booking date against the event date and raise ValueErrors for invalid dates. 

        Args:
            cls: The class instance
            value: The booking date to be validated
            values: The values of all fields in the model
            **kwargs: Additional keyword arguments

        Returns:
            The validated booking date

        Raises:
            ValueError: If the booking date is after event date or within a week of the event
        """
        event_date = datetime.strptime(values["event_date"], "%Y-%m-%d")
        booking_date = datetime.strptime(value, "%Y-%m-%d")

        if booking_date > event_date:
            raise ValueError("Booking date cannot be after event date")

        difference = abs(booking_date - event_date)
        if difference <= timedelta(days=7):
            raise ValueError("Booking date cannot be within a week of the event")

        return value

class BookingRequest(BaseModel):
    attendee: Attendee
    ticket_type: TicketType
    date: Date

