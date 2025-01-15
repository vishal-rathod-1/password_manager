from cryptography.fernet import Fernet
import os
import json

# Generate a key from the master password
def generate_key(master_password: str):
    return Fernet(Fernet.generate_key())

# Encrypt the password
def encrypt_password(password: str, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

# Decrypt the password
def decrypt_password(encrypted_password: bytes, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted

# Save passwords to a JSON file (encrypted)
def save_passwords(data: dict, filename='passwords.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Load passwords from a JSON file
def load_passwords(filename='passwords.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def main():
    print("Welcome to your Password Manager!")
    print("Please remember that your master password will unlock all your stored passwords.")

    # Prompt for the master password
    master_password = input("\nFirst, please enter your master password: ")

    # Generate the key from the master password
    key = generate_key(master_password)

    # Load existing passwords if available
    passwords = load_passwords()

    print("\nYour password vault is ready!")
    while True:
        print("\nWhat would you like to do today?")
        print("1. Add a new password")
        print("2. Retrieve an existing password")
        print("3. Exit the Password Manager")

        choice = input("\nEnter the number of your choice: ")

        if choice == '1':
            # Add a password
            service = input("\nWhich service or website is this password for? (e.g., Gmail, Facebook): ")
            password = input("Now, please enter the password you want to store: ")
            encrypted_password = encrypt_password(password, key)
            passwords[service] = encrypted_password
            save_passwords(passwords)
            print(f"\nGreat! Your password for {service} has been securely stored.")

        elif choice == '2':
            # Retrieve a password
            service = input("\nWhich service or website's password would you like to retrieve? (e.g., Gmail, Facebook): ")
            if service in passwords:
                decrypted_password = decrypt_password(passwords[service], key)
                print(f"\nHere is your password for {service}: {decrypted_password}")
            else:
                print("\nSorry, I couldn't find a password for that service in your vault.")

        elif choice == '3':
            # Exit the program
            print("\nThanks for using the Password Manager! Stay safe and secure!")
            break
        else:
            print("\nOops! That's not a valid option. Please try again.")

if __name__ == "__main__":
    main()
