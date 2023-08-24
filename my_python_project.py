import random
import string


def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def generate_random_password_with_while(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    count = 0

    while count < length:
        password += random.choice(characters)
        count += 1

    return password


# Specify the desired password length
password_length = 12

# Generate and print a random password using the for loop
random_password_for = generate_random_password(password_length)
print("Random Password (for loop):", random_password_for)

# Generate and print a random password using the while loop
random_password_while = generate_random_password_with_while(password_length)
print("Random Password (while loop):", random_password_while)
