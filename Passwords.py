import random
import string

def generate_password():
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password has at least one special character
    password = []
    password.append(random.choice(special_characters))  # Add at least one special character

    # Fill the rest of the password with random characters
    for _ in range(12):  # 12 because we already added one special character
        password.append(random.choice(all_characters))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and truncate to 13 characters
    password = ''.join(password)[:13]

    return password

# Example usage
password = generate_password()
print("Generated Password:", password)