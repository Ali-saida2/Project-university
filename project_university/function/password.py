import string
import emoji

def is_strong_password(password):

    if not isinstance(password,str):
        return False
    
    if (emoji.emoji_list(password)):
        return False
    
    if(len(password)<8):
        return False
    
    if any(char.isspace() for char in password):
        return False

    if not (password.isascii()):
        return False
    
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special_char = any(char in string.punctuation for char in password)
    return has_lowercase and has_uppercase and has_number and has_special_char
