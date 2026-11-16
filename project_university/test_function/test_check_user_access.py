import pytest
from unittest.mock import MagicMock
from function.check_user_access import check_user_access
@pytest.fixture
def mock_collection():
    collection = MagicMock()
    collection.find_one.return_value = {
        "username": "ali", 
        "password": "secure123", 
        "role": "admin"
    }
    return collection

@pytest.mark.parametrize(
    "username_in, password_in, role_in, expected_output",
    [
        # باسوورد صح
        ("ali", "secure123", None, "Authenticated successfully"), 
        # باسوورد غلط
        ("ali", "wrong_pwd", None, "Invalid password"), 
        # دور صح
        ("ali", None, "admin", "Authorized as admin"),
        # دور غلط
        ("ali", None, "user", "Role mismatch"), 
        # ناقص
        ("ali", None, None, "Missing password or role") 
    ]
)
def test_check_user_access_cases(mock_collection, username_in, password_in, role_in, expected_output):
    
    result = check_user_access(mock_collection, username_in, password=password_in, role=role_in)
    assert result == expected_output

def test_user_not_found():
    no_user_collection = MagicMock()
    no_user_collection.find_one.return_value = None 
    
    result = check_user_access(no_user_collection, "unknown_user", password="123")
    assert result == "User not found"