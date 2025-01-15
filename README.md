#Password Manager


# Simple Password Manager

Welcome to your **Simple Password Manager**! This tool helps you securely store and retrieve passwords for different services, using encryption to keep your data safe. All you need is a master password to unlock your password vault.

## Features

- **Secure Storage**: Passwords are encrypted before being saved, ensuring they stay protected.
- **Easy Retrieval**: Retrieve your stored passwords whenever you need them.
- **Simple Interface**: A straightforward, easy-to-use terminal interface for managing your passwords.

## Installation

### Step 1: Install the Required Dependencies

You’ll need the `cryptography` library to handle encryption. You can install it using pip:

pip install cryptography


### Step 2: Download the Script

Download the password manager script (e.g., `password_manager.py`) to your local machine.

## How to Use

### Running the Password Manager

1. Open a terminal and navigate to the folder where the script is saved.
2. Run the script with Python:


python password_manager.py
or
python3 password_manager.py


### Setting Your Master Password

The script will ask you to enter a master password. This password will be used to generate an encryption key that will secure and unlock your password vault. **Make sure you remember it**, as it’s the key to accessing all of your saved passwords.

### Adding a New Password

To store a new password:
1. Choose option `1` from the menu: "Add a new password".
2. Enter the name of the service (e.g., "Gmail", "Facebook").
3. Enter the password you want to store.

Your password will be encrypted and securely saved.

### Retrieving a Password

To retrieve an existing password:
1. Choose option `2` from the menu: "Retrieve an existing password".
2. Enter the name of the service you want to retrieve the password for.
3. If the service exists in your vault, your password will be decrypted and displayed.

### Exiting the Program

To exit the password manager, choose option `3` from the menu: "Exit the Password Manager".

## Important Notes

- **Master Password**: The master password is crucial. It’s the only key to your stored passwords. Be sure to choose one you can remember and keep it secure.
- **Storage Format**: Passwords are stored in an encrypted format inside a JSON file (`passwords.json`), ensuring that even if someone accesses the file, they cannot read your passwords without the master password.


