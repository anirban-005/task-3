import random
import string

def generate_password(length):
    # Define characters for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Prompt the user for password length
    length = int(input("Enter the desired length of the password: "))

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
