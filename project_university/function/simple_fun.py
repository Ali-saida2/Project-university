def add(a,b):
    return a + b
def is_even(n):
    return n % 2 == 0
def find_min(list):
    if not list:
        return None
    min = list[0]
    for item in list:
        if item < min:
            min = item
    return min
def reverse_string(s):
    return s[: : -1]
def is_palindrome(word):
    return word == word[: : -1]
