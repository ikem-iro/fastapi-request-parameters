


def process_booking(booking_data):
    booking_data = {
        "name": booking_data.attendee.name,
        "email": booking_data.attendee.email,
        "phone_number": booking_data.attendee.phone_number,
        "ticket_type": booking_data.ticket_type,
        "event_date": booking_data.date.event_date,
        "booking_date": booking_data.date.booking_date
    }

    return booking_data