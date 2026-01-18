import secrets
import string
from typing import Optional

def generate_hall_admin_password(
        length: int = 6
)-> str:
    """Generate a random password for hall admin."""
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")
    
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def generate_student_password(
        length: int = 8
)-> str:
    """Generate a random password for student."""
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

