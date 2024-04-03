from fastapi import Response, APIRouter
from models.event_booking_model import BookingRequest
from controllers.event_booking_controller import process_booking




router = APIRouter(prefix="/api", tags=["Event Booking"])


@router.post("/booking")
async def book_event(booking_data: BookingRequest, response: Response):
    """
    A POST endpoint to book an event.

    Parameters:
    - response: Response object for handling HTTP responses

    Returns:
    - Dictionary with an error message if booking fails, or a success message if booking is successful
    """
    data = process_booking(booking_data)

    if "error" in data:
        response.status_code = 400
        return data
    response.status_code = 201
    return data