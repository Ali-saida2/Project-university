

import pytest
from function.simple_fun import is_palindrome , is_even , add , find_min , reverse_string
@pytest.mark.parametrize("word, expected", [
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("A man a plan a canal Panama", False),
    ("12321", True)
])
def test_is_palindrome(word, expected):
    assert is_palindrome(word) == expected
@pytest.mark.parametrize("s,expected", [
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("", ""),
    ("a", "a")
])    
def test_reverse_string(s, expected):
    assert reverse_string(s) == expected
@pytest.mark.parametrize("list, expected", [
    ([3, 1, 4, 1, 5, 9], 1),
    ([10, 20, 30], 10),
    ([-1, -5, -3], -5),
    ([], None)
])
def test_find_min(list, expected):
    assert find_min(list) == expected
@pytest.mark.parametrize("a,b, expected", [ 
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
@pytest.mark.parametrize("n, expected", [
    (1, False),
    (2, True),
    (3, False),
    (4, True),
    (5, False)
])
def test_is_even(n, expected):
    assert is_even(n) == expected
