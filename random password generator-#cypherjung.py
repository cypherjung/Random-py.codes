#random password generator
import random
import string

def generate_random_password(length=8):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def generate_strong_password(length=12):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure that the password meets the strength criteria
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (
            any(char.isdigit() for char in password)
            and any(char.isupper() for char in password)
            and any(char.islower() for char in password)
            and any(char in string.punctuation for char in password)
        ):
            break

    return password

# Example usage:
length = int(input("Enter the desired password length: "))
password = generate_random_password(length)
print("Random Password:", password)

strong_password = generate_strong_password()
print("Strong Password:", strong_password)
