import pytest 
from function.password import is_strong_password

def test_strong_password():
    assert is_strong_password("Abcdef12234@") is True

def test_short_password():
    assert is_strong_password("Ad1@") is False

def test_password_without_uppercase():
    assert is_strong_password("abcd12344423&") is False

def test_password_without_lowercase():
    assert is_strong_password("ABCD12234&5") is False

def test_password_without_number():
    assert is_strong_password("ABcdeff&fer") is False

def test_empty_password():
    assert is_strong_password("") is False

def test_none_password():
    assert is_strong_password(None) is False

def test_password_with_space():
    assert is_strong_password("Ali@#1234 5") is False

def test_password_whit_none_english_char():
    assert is_strong_password("Abcsdd@1234بت") is False

@pytest.mark.parametrize("password",[
    None,
    12345678,
    12.5,
    True,
    False,
    [],
    ["Abcdef12"],
    {},
    {"password":"Abcdef12"},
    b"Abcdef",
    ("Abcdef12",),
])

def test_non_string_password(password):
    assert is_strong_password(password) is False

@pytest.mark.parametrize("password",[
"Abc@1234",
"Abc#1234",
"Abc!1234",
"Abc$1234",
"Abc%1234",
"Abc*1234",
"Abc&1234",
"Abc_1234",
"Abc-1234",
"Abc+1234",
])
def test_password_with_special_char(password):
    assert is_strong_password(password) is True

@pytest.mark.parametrize("password",[
    "Ali12345",    
    "Ali123456",    
    "ALIIII3456",    
    "abcdef3456",    
    "Abc        ",    
])
def test_password_without_special_char(password):
    assert is_strong_password(password) is False

@pytest.mark.parametrize("password",[
    "Ali@😁12345",
    "Ali@😊12345",
    "Ali@❤️12345",
    "Ali@👍12345",
])
def test_password_with_emoji(password):
    assert is_strong_password(password) is False

@pytest.mark.parametrize("password",[
    "Ali@12345",
    "Ali@12345",
    "Ali@12345",
    "Ali@12345",
])
def test_password_without_emoji(password):
    assert is_strong_password(password) is True



ollama 