import requests
from unittest.mock import Mock, patch
from function.get_appointments import get_appointments


def test_get_appointments_success():

    fake_response = Mock()

    fake_response.json.return_value = {
        "appointments": 8
    }

    with patch("function.get_appointments.requests.get") as mock_get:

        mock_get.return_value = fake_response

        result = get_appointments("https://example.com/api")

        assert result == {
        "success": True,
        "data": {"appointments": 8},
        "error":None
        }
def test_get_appointments_timeout():
    with patch("function.get_appointments.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout

        result = get_appointments("https://example.com/api")


        assert result == {
                "success": False,
                "data": None,
                "error":"Request timed out"
                }
def test_get_appointments_connection_error():
    with patch("function.get_appointments.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError

        result = get_appointments("https://example.com/api")

        assert result == {
        "success": False,
        "data": None,
        "error":"ConnectionError"
        }
def test_get_appointments_http_error():
    with patch("function.get_appointments.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        result = get_appointments("https://example.com/api")

        assert result == {
        "success": False,
        "data": None,
        "error":"http error occurred"
        }
