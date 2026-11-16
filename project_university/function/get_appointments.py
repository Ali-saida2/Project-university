import requests

def get_appointments(url):
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()

        data = response.json()
        return {
        "success": True,
        "data": {"appointments": 8},
        "error":None
        }

    except requests.exceptions.ConnectionError:
        return{
        "success": False,
        "data": None,
        "error":"ConnectionError"
        }

    except requests.exceptions.Timeout:
        return {
                "success": False,
                "data": None,
                "error":"Request timed out"
                }

    except requests.exceptions.HTTPError:
        return {
        "success": False,
        "data": None,
        "error":"http error occurred"
        }