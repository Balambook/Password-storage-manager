from PasswordManager import PasswordManager

# Maximum characters for user ID and name
MAX_CHARACTERS_ID = 5
MAX_CHARACTERS_NAME = 10


def main() -> None:
    """
    The main function orchestrates user interactions, user creation, credential management, and audit history checks.

        It utilizes a PasswordManager class for user authentication, encryption, and storage of credentials.

        Actions:
        1. Create User: Allows users to create an account with a limited ID and name.
        2. Sign In: Enables users to sign in, manage, and display their encrypted credentials.
        3. Check Audit History: Allows users to check their audit history, including login and action timestamps.
        4. Logout: Exits the program.

        The function employs loops for both the main and secondary actions, validating user inputs for better control.

        Modular design principles are followed, promoting code organization and readability.

        :return: None
    """

    # Flags to control the main cycle (user actions) and secondary cycle (sub-actions)
    first_cycle_flag: bool = True
    second_cycle_flag: bool = True

    # Main loop controlled by first_cycle_flag
    while first_cycle_flag:

        # User input for the main menu
        choice: str = input('Please enter 1 or 2 or 3:\n'
                            '(1) - Create User\n'
                            '(2) - Sign in if you have already created an account\n'
                            '(3) - Check the audit history\n'
                            '(4) - Logout\n').strip()

        # Checking if the choice is a digit and equal to '1'
        if choice.isdigit() and choice == '1':

            # User input for ID and name
            input_id: str = input('Please enter your ID (max 5 characters): ').strip()
            input_name: str = input('Please enter your name (maximum 10 characters): ').strip()

            print()  # Adding an empty line for better visual separation in the output

            # Limiting the user ID and name based on MAX_CHARACTERS_ID and MAX_CHARACTERS_NAME
            limited_user_id: str = input_id[:MAX_CHARACTERS_ID]
            limited_user_name: str = input_name[:MAX_CHARACTERS_NAME]

            # Creating an instance of PasswordManager with limited user ID and name
            password_manger_object: PasswordManager = PasswordManager(limited_user_id, limited_user_name)

            # Checking if the user creation was successful
            if password_manger_object.user.create_user(limited_user_id, limited_user_name):

                # Setting second_cycle_flag to True to enter the secondary loop
                second_cycle_flag: bool = True

                # Secondary loop controlled by second_cycle_flag
                while second_cycle_flag:

                    # User input for secondary menu
                    sub_choice: str = input('Please enter 1 or 2 or 3:\n'
                                            '(1) - Save credentials\n'
                                            '(2) - Display credentials\n'
                                            '(3) - "Logout" if you want to proceed to other actions\n').strip()

                    # Checking if the sub_choice is a digit and equal to '1'
                    if sub_choice.isdigit() and sub_choice == '1':

                        # User input for credentials
                        website_input: str = input('Enter the name of the app or website: ')
                        login_input: str = input('Enter your login: ')
                        password_input: str = input('Enter your password: ')

                        print()  # Adding an empty line for better visual separation in the output

                        # Encrypting and saving credentials
                        password_manger_object.encrypt_save_credentials(website_input, login_input, password_input)

                    # Checking if the sub_choice is a digit and equal to '2'
                    elif sub_choice.isdigit() and sub_choice == '2':

                        # User input for ID and name
                        input_id: str = input('Please enter your ID (max 5 characters): ').strip()
                        input_name: str = input('Please enter your name (maximum 10 characters): ').strip()

                        # Limiting the user ID and name based on MAX_CHARACTERS_ID and MAX_CHARACTERS_NAME
                        limited_user_id: str = input_id[:MAX_CHARACTERS_ID]
                        limited_user_name: str = input_name[:MAX_CHARACTERS_NAME]

                        print()  # Adding an empty line for better visual separation in the output

                        # Creating a new PasswordManager instance with limited user ID and name
                        password_manger_object: PasswordManager = PasswordManager(limited_user_id, limited_user_name)

                        # Checking if the user exists and displaying credentials if successful
                        if password_manger_object.user.get_user_name(limited_user_id):
                            password_manger_object.decrypt_display_credentials()

                    # Checking if the sub_choice is a digit and equal to '3'
                    elif sub_choice.isdigit() and sub_choice == '3':

                        # Exiting the secondary loop
                        second_cycle_flag: bool = False

                    else:
                        # Displaying an error message for an incorrect digit
                        print('You entered an incorrect digit\n')

        # Checking if the choice is a digit and equal to '2'
        elif choice.isdigit() and choice == '2':

            # User input for ID and name
            input_id: str = input('Please enter your ID (max 5 characters): ').strip()
            input_name: str = input('Please enter your name (maximum 10 characters): ').strip()

            # Limiting the user ID and name based on MAX_CHARACTERS_ID and MAX_CHARACTERS_NAME
            limited_user_id: str = input_id[:MAX_CHARACTERS_ID]
            limited_user_name: str = input_name[:MAX_CHARACTERS_NAME]

            print()  # Adding an empty line for better visual separation in the output

            # Creating an instance of PasswordManager with limited user ID and name
            password_manger_object: PasswordManager = PasswordManager(limited_user_id, limited_user_name)

            # Checking if the user exists
            if password_manger_object.user.get_user_name(limited_user_id):

                # Setting second_cycle_flag to True to enter the secondary loop
                second_cycle_flag: bool = True

                # Secondary loop controlled by second_cycle_flag
                while second_cycle_flag:

                    # User input for secondary menu
                    sub_choice: str = input('Please enter 1 or 2 or 3:\n'
                                            '(1) - Save credentials\n'
                                            '(2) - Display credentials\n'
                                            '(3) - "Logout" if you want to proceed to other actions\n').strip()

                    # Checking if the sub_choice is a digit and equal to '1'
                    if sub_choice.isdigit() and sub_choice == '1':

                        # User input for credentials
                        website_input: str = input('Enter the name of the app or website: ')
                        login_input: str = input('Enter your login: ')
                        password_input: str = input('Enter your password: ')

                        print()  # Adding an empty line for better visual separation in the output

                        # Encrypting and saving credentials
                        password_manger_object.encrypt_save_credentials(website_input, login_input, password_input)

                    # Checking if the sub_choice is a digit and equal to '2'
                    elif sub_choice.isdigit() and sub_choice == '2':

                        # User input for ID and name
                        input_id: str = input('Please enter your ID (max 5 characters): ').strip()
                        input_name: str = input('Please enter your name (maximum 10 characters): ').strip()

                        # Limiting the user ID and name based on MAX_CHARACTERS_ID and MAX_CHARACTERS_NAME
                        limited_user_id: str = input_id[:MAX_CHARACTERS_ID]
                        limited_user_name: str = input_name[:MAX_CHARACTERS_NAME]

                        print()  # Adding an empty line for better visual separation in the output

                        # Creating a new PasswordManager instance with limited user ID and name
                        password_manger_object: PasswordManager = PasswordManager(limited_user_id, limited_user_name)

                        # Checking if the user exists and displaying credentials if successful
                        if password_manger_object.user.get_user_name(limited_user_id):
                            password_manger_object.decrypt_display_credentials()

                    # Checking if the sub_choice is a digit and equal to '3'
                    elif sub_choice.isdigit() and sub_choice == '3':

                        # Exiting the secondary loop
                        second_cycle_flag: bool = False

                    else:
                        # Displaying an error message for an incorrect digit
                        print('You entered an incorrect digit\n')

        # Checking if the choice is a digit and equal to '3'
        elif choice.isdigit() and choice == '3':

            # User input for ID and name
            input_id: str = input('Please enter your ID (max 5 characters): ').strip()
            input_name: str = input('Please enter your name (maximum 10 characters): ').strip()

            # Limiting the user ID and name based on MAX_CHARACTERS_ID and MAX_CHARACTERS_NAME
            limited_user_id: str = input_id[:MAX_CHARACTERS_ID]
            limited_user_name: str = input_name[:MAX_CHARACTERS_NAME]

            print()  # Adding an empty line for better visual separation in the output

            # Creating a new PasswordManager instance with limited user ID and name
            password_manger_object: PasswordManager = PasswordManager(limited_user_id, limited_user_name)

            # If the user exists, display the audit history
            if password_manger_object.user.get_user_name(limited_user_id):
                print(password_manger_object.show_audit_history())

        # Checking if the choice is a digit and equal to '4'
        elif choice.isdigit() and choice == '4':

            # Exit from the first loop
            first_cycle_flag: bool = False

        else:
            # Displaying an error message for an incorrect digit
            print('You entered an incorrect digit\n')


if __name__ == "__main__":
    main()
