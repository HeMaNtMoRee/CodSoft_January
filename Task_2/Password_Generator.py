import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        # Prompt the user for the desired password length
        password_length = int(input("Enter the desired password length: "))
        
        if password_length <= 0:
            print("Please enter a valid positive password length.")
            return

        # Generate the password
        generated_password = generate_password(password_length)

        # Display the generated password
        print("Generated Password:", generated_password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
