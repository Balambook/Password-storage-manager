import json
from typing import Dict


class UserManager:
    """
        A class for managing users.

        This class provides functionality for loading, saving, creating, and retrieving user data.

        Attributes:
        - users_file (str): File path for user data in JSON format.

        Methods:
            - __init__(users_file='users.json') -> None
                Initializes the UserManager instance with the specified or default user data file.
                Calls the load_users method to load or create the user data file.

            - load_users() -> None
                Load or create the user data file.
                Tries to load user data from the file; creates a new file if not found.

            - save_users() -> None
                Save user data to the file.

            - create_user(user_id: str, user_name: str) -> bool
                Create a new user and save it.
                Args:
                    user_id (str): User ID.
                    user_name (str): User's name.
                Returns:
                    bool: True if the user was created and saved successfully, False otherwise.

            - get_user_name(user_id: str) -> bool
                Get the username associated with the provided user ID.
                Returns:
                    bool: True if the username is found and logged in, False otherwise.

    """

    def __init__(self, users_file='users.json'):
        self.users_file: str = users_file  # users_file: str - file path for user data in JSON format
        self.load_users()  # Load or create user data file

    def load_users(self) -> None:
        """
        Load or create user data file.

        Tries to load user data from the file, creates a new file if not found.
        """
        try:
            # Attempt to open the specified file for reading
            with open(self.users_file, 'r', encoding='utf-8') as file:
                # Load user data from the file
                self.users: Dict[str, str] = json.load(file)

        except FileNotFoundError:
            # Print a message indicating that the specified file does not exist
            # and inform that a new file is being created with the given filename
            print(f"File '{self.users_file}' does not exist. Creating a new file.")

            # If the file is not found, create a new file and initialize an empty user dictionary
            with open(self.users_file, 'w', encoding='utf-8') as new_file:
                # Initialize an empty user dictionary and save it to the new file
                json.dump({}, new_file)
            self.users: Dict[str, str] = {}

    def save_users(self) -> None:
        """
        Save user data to the file.
        """
        # Open the file for writing and save the user data in JSON format
        with open(self.users_file, 'w', encoding='utf-8') as file:
            json.dump(self.users, file)

    def create_user(self, user_id: str, user_name: str) -> bool:
        """
        Create a new user and save it.

        Args:
            user_id (str): User ID.
            user_name (str): User's name.

        Returns:
            bool: True if the user was created and saved successfully, False otherwise.
        """
        # Check if the user ID already exists
        if user_id not in self.users:

            # If not, add the user to the dictionary, save the updated data
            self.users[user_id]: str = user_name
            self.save_users()  # Save the updated user data to the file

            # print a success message; then, return True
            print(f'User "{user_name}" with ID {user_id} has been created and saved.\n')
            return True

        else:
            # If the user ID already exists, print a message and return False
            print(f'User with ID {user_id} already exists.\n')
            return False

    def get_user_name(self, user_id: str) -> bool:
        """
                Get the username associated with the provided user ID.

                Args:
                    user_id (str): User ID.

                Returns:
                    bool: True if the username is found and logged in, False otherwise.
                """
        # Get the username associated with the provided user ID
        user_name: str = self.users.get(user_id)

        # Check if the username exists
        if user_name:
            # If yes, print a message indicating that the user is logged in and return True
            print(f'User with ID {user_id} - {user_name} is logged in.\n')
            return True

        else:
            # If no username is found, print a message and return False
            print(f'No user found with ID {user_id}.\n')
            return False

