from fastapi.testclient import TestClient
from main import app


client = TestClient(app=app)


def test_register_user():
    """
    Test case to verify the successful registration of a new user.

    Sends a POST request to '/v1/api/register' with a JSON payload containing
    the user's username, email, and password. Asserts that the response status
    code is 201 and the response JSON matches the expected format.
    """

    # Send a POST request to the '/v1/api/register' endpoint with the user data
    response = client.post(
        "/v1/api/register",
        json={
            "username": "West Lif",
            "email": "wlif@example.com",
            "password": "Welcome2$",
        },
    )

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Assert that the response JSON matches the expected format
    assert response.json() == {"message": "Successfully created"}


def test_user_exists():
    """
    Test case to verify the response when trying to register a user
    that already exists.

    Sends a POST request to '/v1/api/register' with a JSON payload containing
    the user's username, email, and password. Asserts that the response JSON
    matches the expected format and the response status code is 409 (Conflict).
    """

    # Send a POST request to the '/v1/api/register' endpoint with the user data
    # to test the case of trying to register a user that already exists
    response = client.post(
        "/v1/api/register",
        json={
            "username": "Desmond Idiot",
            "email": "didiot@example.com",
            "password": "Welcome2$",
        },
    )

    # Assert that the response JSON matches the expected format
    # with the error message indicating that the user already exists
    assert response.json() == {"error": "User already exists"}  # expected error message

    # Assert that the response status code is 409 (Conflict)
    assert response.status_code == 409


def test_register_user_invalid_password():
    response = client.post(
        "/v1/api/register",
        json={
            "username": "West Lif",
            "email": "wlif@example.com",
            "password": "Welcome2",
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "value_error",
                "loc": ["body", "password"],
                "msg": "Value error, Password does not meet stipulated criteria",
                "input": "Welcome2",
                "ctx": {"error": {}},
                "url": "https://errors.pydantic.dev/2.6/v/value_error",
            }
        ]
    }


def test_register_user_same_name():
    response = client.post(
        "/v1/api/register",
        json={
            "username": "Desmond Idiot",
            "email": "deidiot@example.com",
            "password": "Welcome2$",
        },
    )
    # Assert that the response status code is 409 (Conflict)
    assert response.status_code == 409

    assert response.json() == {"error": "User already exists"}  # expected error message
