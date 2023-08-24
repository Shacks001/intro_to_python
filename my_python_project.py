import random
import string


def generate_password(length=12):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if length < 12:
        length = 12

    password = "".join(random.choice(all_characters) for _ in range(length))

    return password


password = generate_password(16)
print("Generated Password:", password)
