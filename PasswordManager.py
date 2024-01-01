import json
from User import User
from typing import Dict, Optional


class PasswordManager:
    """
       The PasswordManager class facilitates the secure management of user credentials,
       providing methods to encrypt and save credentials, decrypt and display stored data,
       and maintain an audit log for user actions. It leverages the User class for encryption
       and includes functionality to save audit logs and display audit history.

       Attributes:
           - user: User
               An instance of the User class associated with the PasswordManager.
           - user_id: str
               The unique identifier of the user.
           - user_name: str
               The name of the user.

       Methods:
           - __init__(user_id: str, user_name: str) -> None
               Initializes a PasswordManager instance with the associated User instance.

           - encrypt_save_credentials(website: str, login: str, password: str) -> None
               Encrypts and saves user credentials for a specified website.

           - decrypt_display_credentials() -> None
               Decrypts and displays stored user credentials.

           - save_audit_log(action: str) -> None
               Saves an audit log entry for a specified user action.

           - show_audit_history() -> Optional[str]
               Displays the audit history of user actions or returns None if no history is found.
       """
    def __init__(self, user_id: str, user_name: str):
        """
            Initialize the PasswordManager instance.

            Args:
                user_id (str): User ID.
                user_name (str): User's name.
        """
        # Create a User instance associated with the PasswordManager
        self.user: User = User(user_id, user_name)
        self.user_id: str = user_id
        self.user_name: str = user_name

    def encrypt_save_credentials(self, website: str, login: str, password: str) -> None:
        """
            Encrypt and save user credentials.

            Args:
                website (str): Website name.
                login (str): User login.
                password (str): User password.
        """
        # Create a dictionary with user credentials
        data: Dict[str, str] = {'website': website, 'login': login, 'password': password}

        # Encrypt the credentials data using the User's encryption method
        encrypted_data: bytes = self.user.encrypt_data(json.dumps(data))

        # Append the encrypted data to the user's data file
        with open(self.user.users_data_file, 'ab') as data_file:
            data_file.write(encrypted_data + b'\n')

        # Save an audit log entry indicating the action
        self.save_audit_log(f'- Saved credentials for {website}')

        # Print a success message
        print('Data saved successfully\n')

    def decrypt_display_credentials(self) -> None:
        """
            Decrypt and display user credentials.

            Attempts to read the user's data file, decrypts each line, and prints the decrypted JSON data.
            If the decryption key is not found (TypeError), it prints an error message.
            If the data file is not found (FileNotFoundError), it informs the user to save credentials first.

            Raises:
                TypeError: If the decryption key is not found.
                FileNotFoundError: If the data file is not found.

        """
        try:
            # Attempt to open the user's data file for reading
            with open(self.user.users_data_file, 'r') as data_file:
                encrypted_data: list[str] = data_file.readlines()
            decrypted_data_json_line: list[str] = [self.user.decrypt_data(line.strip()) for line in encrypted_data]

            # Decrypt each line in the data file and print the decrypted JSON data
            for line in decrypted_data_json_line:
                for key, val in json.loads(line).items():
                    print(f'{key}: {val}')
                print()

        except TypeError:
            # Handle the case where the decryption key is not found
            print('Key is not found\n')

        except FileNotFoundError:
            # Handle the case where the data file is not found
            print('No such file or directory. To create a file, you need to save any credentials.\n')

        # Save an audit log entry indicating the action
        self.save_audit_log(f'- Deciphered the data')

    def save_audit_log(self, action: str) -> None:
        """
            Save audit log entry.

            Logs a user action with a timestamp by invoking the log_action method of the associated User instance.

            Args:
                action (str): The action to be logged.

        """
        self.user.log_action(action)

    def show_audit_history(self) -> Optional[str]:
        """
            Show user audit history.

            Retrieves and returns the audit history of user actions using the get_audit_history method
            of the associated User instance. Additionally, logs the action of checking credentials in the audit log.

            Returns:
                Optional[str]: Audit history as a string or None if no history is found.

        """
        # Save an audit log entry indicating the action of checking credentials
        self.save_audit_log(f'- Checked the credentials')

        # Retrieve and return the audit history using the get_audit_history method
        return self.user.get_audit_history()
