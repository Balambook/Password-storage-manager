import datetime
from cryptography.fernet import Fernet
from UserManager import UserManager


class User(UserManager):
    """
        A class representing a user with additional functionality for logging actions,
        managing encryption keys, and handling user data.
    """
    def __init__(self, user_id: str, user_name: str):
        super().__init__()   # Call the constructor of the base class (UserManager)
        self.user_name: str = user_name
        self.user_id: str = user_id

        # The name of the file where specific user actions will be stored.
        # The file will be created when the user performs certain actions, such as saving a password.
        # The file format will be txt
        self.audit_file: str = f'{user_id}_audit.txt'

        # The name of the file where the specific user's key for encryption and decryption of data will be stored
        self.key_file: str = f'{user_id}_key.txt'

        # The name of the file for a specific user where data (site, login, password) will be stored
        self.users_data_file: str = f'{user_id}_data.json'

        # We create or load a saved user key
        self.load_or_create_key()

    def __str__(self) -> str:
        """
            String representation of the User.

            Returns:
                str: A string containing the user's name and ID.
        """
        return f'User: {self.user_name}, ID: {self.user_id}'

    def load_or_create_key(self) -> None:
        """
            Load or create the encryption key for the user.

            Tries to load the key from the file, creates a new key if not found.
        """
        try:
            # Attempt to open the key file for reading in binary mode
            with open(self.key_file, 'rb') as key_file:
                # Read the key from the file
                self.key: bytes = key_file.read()

        except FileNotFoundError:
            # If the key file is not found, generate a new key
            self.key: bytes = Fernet.generate_key()

            # Save the new key to the key file in binary mode
            with open(self.key_file, 'wb') as key_file:
                key_file.write(self.key)

    def log_action(self, action: str) -> None:
        """
            Log a user action with a timestamp.

            Args:
                action (str): The action to be logged.
        """
        # Get the current timestamp in the specified format
        timestamp: str = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        # Create a log entry containing timestamp, user information, and the action
        log_entry: str = f'{timestamp} - {str(self)} - {action}\n'

        # Open the audit file in append mode and write the log entry
        with open(self.audit_file, 'a') as audit_file:
            audit_file.write(log_entry)

    def get_audit_history(self) -> str:
        """
            Retrieve the audit history of user actions.

            Returns:
                str: A string containing the audit history or a message if no history is found.
        """
        try:
            # Attempt to open the audit file for reading
            with open(self.audit_file, 'r') as audit_file:
                print()  # Adding an empty line for better visual separation in the output
                return audit_file.read()  # Read and return the contents of the audit file

        except FileNotFoundError:
            # If the audit file is not found, return a message indicating no audit history
            return 'No audit history.\n'

    def encrypt_data(self, data: str) -> bytes:
        """
            Encrypt user data using the user's key.

            Args:
                data (str): The data to be encrypted.

            Returns:
                bytes: The encrypted data.
        """
        # Create a Fernet cipher object using the user's key
        cipher: Fernet = Fernet(self.key)

        # Encrypt the input data by encoding it and then encrypting with the cipher
        encrypted_data: bytes = cipher.encrypt(data.encode())

        # Return the resulting encrypted data
        return encrypted_data

    def decrypt_data(self, encrypted_data: str) -> str:  # TODO: ЗРОБИТИ ЩОБ КОРИСТУВАЧ ВВОДИВ СВІЙ КЛЮЧ
        """
            Decrypt user data using the user's key.

            Args:
                encrypted_data (bytes): The encrypted data to be decrypted.

            Returns:
                str: The decrypted data or a message if no decryption key is found."""
        try:
            # Create a Fernet cipher object using the user's key
            cipher: Fernet = Fernet(self.key)

            # Decrypt the encrypted data, decode it to a string, and return the result
            decrypted_data: str = cipher.decrypt(encrypted_data).decode()
            return decrypted_data

        # If a ValueError occurs (e.g., due to a missing or invalid key),
        # print a message and return an empty string or handle the exception accordingly
        except ValueError:
            print(f'No decryption key found in the file {self.key_file}\n')
