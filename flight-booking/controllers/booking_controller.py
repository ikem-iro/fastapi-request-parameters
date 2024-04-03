from uuid import uuid4
from datetime import datetime, timezone




def create_new_booking(booking_details):
    """
    Create a new booking using the provided booking details.

    Parameters:
    - booking_details: A dictionary containing all the necessary details for the booking.

    Returns:
    - A dictionary with the message "Booking created successfully", the reference ID of the booking, 
      the name of the customer, and the flight details including departure date, class, origin, destination, and booking time.
    """

    cutomer_title = booking_details.contact_details.title
    customer_name = booking_details.contact_details.first_name + " " + booking_details.contact_details.last_name
    customer_age = booking_details.contact_details.age
    customer_email = booking_details.contact_details.email
    customer_gender = booking_details.contact_details.gender
    customer_phone_number = booking_details.contact_details.phone_number
    flight_origin = booking_details.flight_details.origin
    flight_destination = booking_details.flight_details.destination
    flight_departure_date = booking_details.flight_details.departure_date
    flight_class = booking_details.flight_details.flight_class
    seat_preference = booking_details.seatpreference
    details = {
        "_id": uuid4(),
        "reference_id": uuid4(),
        "customer_title": cutomer_title,
        "customer_name": customer_name,
        "customer_age": customer_age,
        "customer_email": customer_email,
        "customer_gender": customer_gender,
        "customer_phone_number": customer_phone_number,
        "flight_origin": flight_origin,
        "flight_destination": flight_destination,
        "flight_departure_date": flight_departure_date,
        "booking_time": {"local_time": datetime.now(), "utc_time": datetime.now(timezone.utc)},
        "flight_class": flight_class,
        "seat_preference": seat_preference
    }
    return {
        "message": "Booking created successfully",
        "details": details["reference_id"],
        "name": details["customer_name"],
        "flight_details": {
            "flight_depature_date": details["flight_departure_date"],
            "flight_class": details["flight_class"],
            "flight_origin": details["flight_origin"],
            "flight_destination": details["flight_destination"],
            "booking_time": details["booking_time"]
        }
    }


