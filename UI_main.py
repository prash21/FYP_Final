# DEVELOPED BY PRASHANT AND TEAM 12 (FIT3164)
# START OF UI LOGIC FILE (UI_main.py)

# THIS FILE CONTAINS CODE FOR THE USER INTERFACE'S LOGIC AND DEPENDENCIES. INPUT
# VALIDATION AND OTHER ERROR HANDLING ARE ALSO DONE IN THIS FILE.

# The following packages are imported for the user interface.
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import StringProperty
# Import the DataBase class from database.py file
from database import DataBase
# Import from the main file
import main

# First, set the default background color for the UI. Kivy takes each
# color value and divides it by 255.
# Set the background color
Window.clearcolor = (242/255.0, 212/255.0, 194/255.0, 1)


# Class for create account window
class CreateAccountWindow(Screen):
    """This class is the logic behind the interface for the window that allows the users
    to create a new account"""

    # Variable to hold the user's full name
    full_name = ObjectProperty(None)
    # Variable to hold the user's email
    email = ObjectProperty(None)
    # Variable to hold the user's password
    password = ObjectProperty(None)

    # Action after submit button is pressed
    def submit(self):
        """This function is called when the submit button is pressed from the create account
        window. The function will check the user's input, and if valid, the account credentials
        will be stored in the database, else an error will show"""
        # Validate password and email format
        if self.full_name.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and \
                self.email.text.count(".") > 0 and self.password.text != "":
            if self.password != "":
                # Add users' login data to the local database
                if db.add_user(self.email.text, self.password.text, self.full_name.text) == 1:
                    # Popup to show successful account creation
                    account_created()
                    # Clear any inputs made by the user
                    self.reset()
                    # Go back to the login page
                    sm.current = "login"
                else:
                    # Popup to show unsuccessful account creation
                    create_account_failed()
            # Pop up window if input data is invalid
            else:
                invalid_form()
        else:
            invalid_form()

    # Leads to the login page
    def login(self):
        """This function is called when the user clicks to go back to the login
        page from the create account window. It clears any inputs and moves to
        the login window."""
        self.reset()
        sm.current = "login"

    # Clears all text inputs
    def reset(self):
        """Clears inputs from all 3 fields in the create account window."""
        self.email.text = ""
        self.password.text = ""
        self.full_name.text = ""


# Class for the login window
class LoginWindow(Screen):
    """This class is the logic behind the interface for the window that takes in
    the user's credentials to login in to an account."""

    # Variable to hold the user's email
    email = ObjectProperty(None)
    # Variable to hold the user's password
    password = ObjectProperty(None)

    # Check if login credentials match values in local db
    def login_btn(self):
        """Checks the user's input if it matches with credentials in the local
        database. If valid, program enters into the main page, else an error
        popup will show"""
        # Validate the input with the account details in the local database
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            # Go to the main menu if valid
            sm.current = "main"
        else:
            # Else a popup will show
            invalid_login()

    # Leads to the page to create an account
    def create_btn(self):
        """When clicked, it clears any inputs in the current page and moves
        to the create account window."""
        self.reset()
        sm.current = "create"

    # Clears all text inputs
    def reset(self):
        """Clears both email and password inputs from the text fields."""
        self.email.text = ""
        self.password.text = ""


# Class for the "forgot password" window
class ForgotPasswordWindow(Screen):
    """Class for the logic behind the "forgot password" window."""

    # Variable to hold the user's email
    email = ObjectProperty(None)
    # Variable to hold the user's full name
    full_name = ObjectProperty(None)
    # Variable to hold the user's new password
    new_passw = ObjectProperty(None)

    # Action after submit button for changing password is pressed
    def submit(self):
        """Function to ensure input format is correct, followed by validating the user's credentials,
        before finally changing the password."""

        # Validate password and email format
        if self.email.text != "" and self.full_name.text != "" and self.new_passw.text != "":
            if self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
                # Check if the email exists, and the correct name is verified
                if db.validate_email(self.email.text, self.full_name.text, self.new_passw.text) == 1:
                    # Show a prompt to show that password has been changed
                    password_changed()
                    # Add users' updated login data to the local database
                    # Clear any inputs made by the user
                    self.reset()
                    # Go back to the login page
                    sm.current = "login"
                # If the full name entered does not match, a prompt is displayed and the name and password
                # fields are cleared.
                elif db.validate_email(self.email.text, self.full_name.text, self.new_passw.text) == -1:
                    # Display prompt
                    validation_failed()
                    # Clear fields
                    self.full_name.text = ""
                    self.new_passw.text = ""
                # If email does not exist in local database, a prompt is displayed and all inputs are
                # cleared from the text fields.
                elif db.validate_email(self.email.text, self.full_name.text, self.new_passw.text) == 0:
                    # Display prompt
                    email_not_found()
                    # Clear all fields
                    self.reset()
            # If the format of the email is wrong, a prompt is displayed and all fields are reset
            else:
                # Display prompt
                invalid_email()
                # Clear all fields
                self.reset()
        # If the fields are incorrectly entered, a prompt is displayed
        else:
            # Display prompt
            invalid_form()

    # Clears all text inputs
    def reset(self):
        """Clears the email, full name, and password text input fields."""
        self.email.text = ""
        self.full_name.text = ""
        self.new_passw.text = ""


# Class for the main window
class MainWindow(Screen):
    """This class contains the logic behind the actions that take place in the
    Main Menu window. As there are only three buttons which simply redirects to
    different pages, the page redirection for each button is specified in the kv
    file itself"""
    pass


class InfoWindow(Screen):
    """This class contains the logic behind the actions that take place in the
    Software Info page. The information and button-page redirection are done
    in the kv file itself."""
    pass


class PredictionWindow1(Screen):
    """This class contains the logic for the first prediction window that takes
    the first 10 inputs from the user."""

    # Declare all the variables as a string property.
    # These variables are taken from the main.py file, and will be passed on to
    # the UI for display. Changing the variable values in the main.py file directly
    # changes the variable values here and in the kv file.
    # First 10 feature variables declared below.
    feature1 = StringProperty('')
    feature1 = main.feature1

    feature2 = StringProperty('')
    feature2 = main.feature2

    feature3 = StringProperty('')
    feature3 = main.feature3

    feature4 = StringProperty('')
    feature4 = main.feature4

    feature5 = StringProperty('')
    feature5 = main.feature5

    feature6 = StringProperty('')
    feature6 = main.feature6

    feature7 = StringProperty('')
    feature7 = main.feature7

    feature8 = StringProperty('')
    feature8 = main.feature8

    feature9 = StringProperty('')
    feature9 = main.feature9

    feature10 = StringProperty('')
    feature10 = main.feature10

    # Next, declare the input boxes from the UI.
    userinput1 = ObjectProperty(None)
    userinput2 = ObjectProperty(None)
    userinput3 = ObjectProperty(None)
    userinput4 = ObjectProperty(None)
    userinput5 = ObjectProperty(None)
    userinput6 = ObjectProperty(None)
    userinput7 = ObjectProperty(None)
    userinput8 = ObjectProperty(None)
    userinput9 = ObjectProperty(None)
    userinput10 = ObjectProperty(None)

    def validate_input_window1(self):
        """This function is called when the "Next" button is pressed from the first prediction
        input page. It validates the first 10 inputs and ensures that input data are properly
        checked and exceptions are handled properly. (Robustness)"""

        # The valid variable will count how many out of 10 inputs are valid. If less than
        # 10 inputs are valid, the program will require the user to re-enter appropriate values.
        valid = 0
        # Validate the first input
        userinput1 = self.userinput1.text
        # Check if the input is within the accepted range
        try:
            if 1.0 <= float(userinput1) <= 125.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature1),
                      content=Label(text='Enter an Age between 1 and 125 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # The input field is then cleared
                self.userinput1.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid '+str(main.feature1),
                        content=Label(text='Enter an Age between 1 and 125 inclusive'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput1.text = ""

        # Next validation
        # Validate the second input
        userinput2 = self.userinput2.text
        # Check if the input is within the accepted range
        try:
            if 1.0 <= float(userinput2) <= 450.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature2),
                      content=Label(text='Enter a Weight between 1kg and 450kg inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput2.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid '+str(main.feature2),
                        content=Label(text='Enter a Weight between 1kg and 450kg inclusive'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput2.text = ""

        # Next validation
        # Validate the third input
        userinput3 = self.userinput3.text
        # Check if the input is within the accepted range
        try:
            if 50.0 <= float(userinput3) <= 300.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature3),
                      content=Label(text='Enter a Height between 50cm and 300cm inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput3.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature3),
                        content=Label(text='Enter a Height between 50cm and 300cm inclusive'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput3.text = ""

        # Next validation
        # Validate the fourth input
        userinput4 = self.userinput4.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput4) <= 50.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature4),
                      content=Label(text='Enter a BMI between 0 and 50 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput4.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature4),
                        content=Label(text='Enter a BMI between 0 and 50 inclusive'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput4.text = ""

        # Next validation
        # Validate the fifth input
        userinput5 = self.userinput5.text
        # Check if the input is within the accepted range
        try:
            if str(userinput5) == "1" or str(userinput5) == "0":
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature5),
                      content=Label(text='Enter a HTN value of either 0 or 1'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput5.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature5),
                        content=Label(text='Enter a HTN value of either 0 or 1'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput5.text = ""

        # Next validation
        # Validate the sixth input
        userinput6 = self.userinput6.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput6) <= 150.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature6),
                      content=Label(text='Enter a PR between 0 and 150 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput6.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature6),
                        content=Label(text='Enter a PR between 0 and 150 inclusive'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput6.text = ""

        # Next validation
        # Validate the seventh input
        userinput7 = self.userinput7.text
        # Check if the input is within the accepted range
        try:
            if str(userinput7) == "1" or str(userinput7) == "0":
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature7),
                      content=Label(text='Systolic Murmur must be either 0 or 1'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput7.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature7),
                        content=Label(text='Systolic Murmur must be either 0 or 1'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput7.text = ""

        # Next validation
        # Validate the eighth input
        userinput8 = self.userinput8.text
        # Check if the input is within the accepted range
        try:
            if str(userinput8) == "1" or str(userinput8) == "0":
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature8),
                      content=Label(text='Diastolic Murmur must be either 0 or 1'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput8.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature8),
                        content=Label(text='Diastolic Murmur must be either 0 or 1'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput8.text = ""

        # Next validation
        # Validate the ninth input
        userinput9 = self.userinput9.text
        # Check if the input is within the accepted range
        try:
            if str(userinput9) == "1" or str(userinput9) == "0":
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature9),
                      content=Label(text='Typical Chest Pain must be either 0 or 1'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput9.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature9),
                        content=Label(text='Typical Chest Pain must be either 0 or 1'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput9.text = ""

        # Last validation for first input page
        # Validate the tenth input
        userinput10 = self.userinput10.text
        # Check if the input is within the accepted range
        try:
            if str(userinput10) == "1" or str(userinput10) == "0":
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature10),
                      content=Label(text='St Depression must be either 0 or 1'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput10.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature10),
                        content=Label(text='St Depression must be either 0 or 1'),
                        size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput10.text = ""

        # Now, check if all inputs are valid
        if valid == 10:
            # If valid, call the submit_input1 function to store the inputs
            # in the main.py file.
            self.submit_input1()
            # Then, move to the next prediction input page and clear all previous
            # inputs from the first input page.
            sm.current = "prediction2"
            self.reset()
        else:
            return False

    # Get the user's input and pass into the get_input1 function from main.py
    def submit_input1(self):
        """This function takes all the user's input from the first prediction input
        page, and stores it in the main.py file by calling the get_input1 function from
        main.py."""

        # Get the user's input. Note that all the inputs would have been validated at
        # this point.
        userinput1 = self.userinput1.text
        userinput2 = self.userinput2.text
        userinput3 = self.userinput3.text
        userinput4 = self.userinput4.text
        userinput5 = self.userinput5.text
        userinput6 = self.userinput6.text
        userinput7 = self.userinput7.text
        userinput8 = self.userinput8.text
        userinput9 = self.userinput9.text
        userinput10 = self.userinput10.text

        # Pass the values into the function in the main.py file. The values will be stored there and used
        # later for predictive modelling.
        main.get_input1(userinput1, userinput2, userinput3, userinput4, userinput5, userinput6, userinput7,
                        userinput8, userinput9, userinput10)

        # Reset all the input boxes from the first prediction input page if it has not been cleared yet
        self.reset()

    # Function to reset all input boxes.
    def reset(self):
        """This function clears all inputs from the first 10 input fields on the first prediction
        input page."""
        self.userinput1.text = ""
        self.userinput2.text = ""
        self.userinput3.text = ""
        self.userinput4.text = ""
        self.userinput5.text = ""
        self.userinput6.text = ""
        self.userinput7.text = ""
        self.userinput8.text = ""
        self.userinput9.text = ""
        self.userinput10.text = ""


class PredictionWindow2(Screen):
    """Similar to the first prediction window class, this class contains the logic
     for the second prediction window that takes the next 10 inputs from the user."""

    # Declare all the variables as a string property.
    # These variables are taken from the main.py file, and will be passed on to
    # the UI for display. Changing the variable values in the main.py file directly
    # changes the variable values here and in the kv file.
    # Next 10 feature variables declared below.
    feature11 = StringProperty('')
    feature11 = main.feature11

    feature12 = StringProperty('')
    feature12 = main.feature12

    feature13 = StringProperty('')
    feature13 = main.feature13

    feature14 = StringProperty('')
    feature14 = main.feature14

    feature15 = StringProperty('')
    feature15 = main.feature15

    feature16 = StringProperty('')
    feature16 = main.feature16

    feature17 = StringProperty('')
    feature17 = main.feature17

    feature18 = StringProperty('')
    feature18 = main.feature18

    feature19 = StringProperty('')
    feature19 = main.feature19

    feature20 = StringProperty('')
    feature20 = main.feature20

    # Next, declare the input boxes from the UI.
    userinput11 = ObjectProperty(None)
    userinput12 = ObjectProperty(None)
    userinput13 = ObjectProperty(None)
    userinput14 = ObjectProperty(None)
    userinput15 = ObjectProperty(None)
    userinput16 = ObjectProperty(None)
    userinput17 = ObjectProperty(None)
    userinput18 = ObjectProperty(None)
    userinput19 = ObjectProperty(None)
    userinput20 = ObjectProperty(None)

    def validate_input_window2(self):
        """This function is called when the "Submit" button is pressed from the second prediction
        input page. It validates the second 10 inputs and ensures that input data are properly
        checked and exceptions are handled properly. (Robustness)"""

        # The valid variable will count how many out of 10 inputs are valid. If less than
        # 10 inputs are valid, the program will require the user to re-enter appropriate values.
        valid = 0
        # Validate the 11th input
        userinput11 = self.userinput11.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput11) <= 5.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature11),
                      content=Label(text='CR value has to be between 0 and 5 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # The input field is then cleared
                self.userinput11.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            Popup(title='Invalid ' + str(main.feature11),
                  content=Label(text='CR value has to be between 0 and 5 inclusive'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput11.text = ""

        # Next validation
        # Validate the 12th input
        userinput12 = self.userinput12.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput12) <= 100.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature12),
                      content=Label(text='BUN value must be between 0 and 100 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput12.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature12),
                  content=Label(text='BUN value must be between 0 and 100 inclusive'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput12.text = ""

        # Next validation
        # Validate the 13th input
        userinput13 = self.userinput13.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput13) <= 100.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature13),
                      content=Label(text='ESR value must be between 0 and 100 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput13.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature13),
                  content=Label(text='ESR value must be between 0 and 100 inclusive'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput13.text = ""

        # Next validation
        # Validate the 14th input
        userinput14 = self.userinput14.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput14) <= 20.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature14),
                      content=Label(text='HB value must be between 0 and 20 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput14.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature14),
                  content=Label(text='HB value must be between 0 and 20 inclusive'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput14.text = ""

        # Next validation
        # Validate the 15th input
        userinput15 = self.userinput15.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput15) <= 10.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature15),
                      content=Label(text='K value must be between 0 and 10 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput15.text = ""
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature15),
                  content=Label(text='K value must be between 0 and 10 inclusive'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput15.text = ""

        # Next validation
        # Validate the 16th input
        userinput16 = self.userinput16.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput16) <= 100.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature16),
                      content=Label(text='Lymph value must be between 0 and 100 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput16.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature16),
                  content=Label(text='Lymph value must be between 0 and 100 inclusive'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput16.text = ""

        # Next validation
        # Validate the 17th input
        userinput17 = self.userinput17.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput17) <= 1000.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature17),
                      content=Label(text='PLT value must be between 0 and 1000 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput17.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature17),
                  content=Label(text='PLT value must be between 0 and 1000 inclusive'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput17.text = ""

        # Next validation
        # Validate the 18th input
        userinput18 = self.userinput18.text
        # Check if the input is within the accepted range
        try:
            if 0.0 <= float(userinput18) <= 100.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature18),
                      content=Label(text='EF-TTE value must be between 0 and 100 inclusive'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput18.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature18),
                  content=Label(text='EF-TTE value must be between 0 and 100 inclusive'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput18.text = ""

        # Next validation
        # Validate the 19th input
        userinput19 = self.userinput19.text
        # Check if the input is within the accepted set of values
        try:
            if float(userinput19) == 0.0 or float(userinput19) == 1.0 or float(userinput19) == 2.0 \
                    or float(userinput19) == 3.0 or float(userinput19) == 4.0:
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature19),
                      content=Label(text='Region RWMA has to be 0, 1, 2, 3 or 4'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput19.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            # Display a prompt if any other value is entered
            Popup(title='Invalid ' + str(main.feature19),
                  content=Label(text='Region RWMA has to be 0, 1, 2, 3 or 4'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Clear the input field
            self.userinput19.text = ""

        # Last validation for second input page
        # Validate the 20th input
        userinput20 = self.userinput20.text
        # Check if the input is within the accepted set of values
        try:
            if str(userinput20).lower() == "no" or str(userinput20).lower() == "mild" or \
                    str(userinput20).lower() == "moderate" or str(userinput20).lower() == "severe":
                # If accepted, valid counter add by 1
                valid += 1
            # Else, a prompt would be displayed regarding the error
            else:
                Popup(title='Invalid ' + str(main.feature20),
                      content=Label(text='VHD must either be "No", "Mild", "Moderate" or "Severe"'),
                      size_hint=(None, None), size=(400, 400)).open()
                # Clear the input field
                self.userinput20.text = ""
        # Broad exception clause to handle any possible errors (Robustness)
        except:
            Popup(title='Invalid ' + str(main.feature20),
                  content=Label(text='VHD must either be "No", "Mild", "Moderate" or "Severe"'),
                  size_hint=(None, None), size=(400, 400)).open()
            # Display a prompt if any other value is entered
            self.userinput20.text = ""

        # Now, check if all inputs are valid
        if valid == 10:
            # If valid, call the submit_input2 function to store the inputs
            # in the main.py file.
            self.submit_input2()
            # Then, move to the results page and clear all previous
            # inputs from the second input page.
            sm.current = "results"
            self.reset()
        else:
            return False

    def submit_input2(self):
        """This function takes all the user's input from the second prediction input
        page, and stores it in the main.py file by calling the get_input2 function from
        main.py."""

        # Get the user's input. Note that all the inputs would have been validated at
        # this point.
        userinput11 = self.userinput11.text
        userinput12 = self.userinput12.text
        userinput13 = self.userinput13.text
        userinput14 = self.userinput14.text
        userinput15 = self.userinput15.text
        userinput16 = self.userinput16.text
        userinput17 = self.userinput17.text
        userinput18 = self.userinput18.text
        userinput19 = self.userinput19.text
        userinput20 = self.userinput20.text

        # Pass the values into the function in the main.py file. The values will be stored there and used
        # later for predictive modelling.
        main.get_input2(userinput11, userinput12, userinput13, userinput14, userinput15, userinput16, userinput17,
                        userinput18, userinput19, userinput20)

        # Reset all the input boxes from the second prediction input page if it has not been cleared yet
        self.reset()

    # Function to reset all input boxes.
    def reset(self):
        """This function clears all inputs from the second 10 input fields on the second prediction
        input page."""
        self.userinput11.text = ""
        self.userinput12.text = ""
        self.userinput13.text = ""
        self.userinput14.text = ""
        self.userinput15.text = ""
        self.userinput16.text = ""
        self.userinput17.text = ""
        self.userinput18.text = ""
        self.userinput19.text = ""
        self.userinput20.text = ""


# Class for the results screen
class ResultsWindow(Screen):
    """This class holds the logic for the Results page."""

    def get_result(self):
        """This function calls the a popup box which contains the result that is stored
        by the classifier model function in the main.py file."""
        show_result()


# The WindowManager class for all screens
class WindowManager(ScreenManager):
    """Class dedicated to manage multiple screens for the application."""
    pass


# The following are popup prompt boxes that are used throughout the file.
def invalid_login():
    """Popup prompt when the user's email or password entered do not match
    the credentials in the local database."""
    # Add the text message in the prompt box
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def show_result():
    """Popup prompt when the user clicks on "Show Result" to view the result
    of the prediction. This function also fetches the result from a list in
    the main.py file."""
    # Print the result stored in the result_list from main.py, along with some text
    pop = Popup(title='Prediction Result',
                content=Label(text="Diagnosis:  "+str(main.result_list[0])+"\n"
                "Probability of diagnosis occurrence:  "+str(round(main.result_list[1], 2))),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalid_form():
    """Popup prompt when the user does not complete the input fields or values
    in the input fields were incorrectly entered."""
    # Add the text message in the prompt box
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def email_not_found():
    """Popup prompt when the user keys in an email to login, but the email
    does not exist in the local database."""
    # Add the text message in the prompt box
    pop = Popup(title='Email Not Found',
                content=Label(text='Email not found. Please try again.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalid_email():
    """Popup prompt when the user keys in an email in the invalid format."""
    # Add the text message in the prompt box
    pop = Popup(title='Invalid Email',
                content=Label(text='Please enter a valid email address.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def validation_failed():
    """Popup prompt when the name does not match with the name in the database
    when the user is trying to change the account password."""
    # Add the text message in the prompt box
    pop = Popup(title='Validation Failed',
                content=Label(text='Validation Failed: Name did not match.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def password_changed():
    """Popup prompt when the user successfully changes the account password
    from the "forgot password" page."""
    # Add the text message in the prompt box
    pop = Popup(title='Password Successfully Changed',
                content=Label(text='Password Successfully Changed!'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def account_created():
    """Popup prompt when an account is successfully created from the create
    account page."""
    # Add the text message in the prompt box
    pop = Popup(title='Account Successfully Created',
                content=Label(text='Account Successfully Created!'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def create_account_failed():
    """Popup prompt when email already exists when user tries to create a new
    account with the same email."""
    # Add the text message in the prompt box
    pop = Popup(title='Email already exists',
                content=Label(text='An account already exists with this email.\n'
                                   'Try using another email, or recover the password from\n'
                                   'an existing email.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


# Load the kv file and screen manager which has the code that interprets the design of the UI
kv = Builder.load_file("UI.kv")
sm = WindowManager()
# Initiate the local database file
db = DataBase("users.txt")
# Initialize all screens/windows
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"),
           InfoWindow(name="info"), PredictionWindow1(name="prediction"), PredictionWindow2(name="prediction2"),
           ResultsWindow(name="results"), ForgotPasswordWindow(name="forgotpassw")]
# Add all screens to the screen manager
for screen in screens:
    sm.add_widget(screen)

# Start at the login screen
sm.current = "login"


# Run the app
class MyMainApp(App):
    """The base class for creating Kivy applications"""

    def build(self):
        """This function returns the widget instance."""
        return sm


# To be executed since the UI needs to run asynchronously with the main.py file
if __name__ == "__main__":
    MyMainApp().run()

# END OF FILE
# DEVELOPED BY PRASHANT & TEAM 12 (FIT3164)
