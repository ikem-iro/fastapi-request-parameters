from fastapi import APIRouter, Response
from models.booking_model import FlightBooking
from controllers.booking_controller import create_new_booking



router = APIRouter(prefix='/api', tags=['Flight Booking'])

@router.post('/flights/bookings')
async def book_flight(booking_details: FlightBooking, response: Response):
    """
    Create a new flight booking.

    This function is an asynchronous endpoint that handles the POST request to '/flights/bookings'. It takes in a `booking_details` object of type `FlightBooking` and a `response` object of type `Response`. The `booking_details` object contains the details of the flight booking, such as the passenger information, flight details, and any additional notes. The `response` object is used to set the status code of the HTTP response.

    The function calls the `create_new_booking` function to create a new booking using the provided `booking_details`. It then sets the status code of the response to 201 (indicating a successful creation) and returns a dictionary with the details of the booking.

    Parameters:
        - booking_details (FlightBooking): The details of the flight booking.
        - response (Response): The HTTP response object.

    Returns:
        - dict: A dictionary containing the details of the booking.

    """
    data = create_new_booking(booking_details)
    response.status_code = 201
    return data