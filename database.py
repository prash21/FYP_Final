# DEVELOPED BY PRASHANT AND TEAM 12 (FIT3164)
# START OF DATABASE CODE FILE (database.py)

# All functions packaged within the class
class DataBase:
    """This is the database class which hols all the functions necessary to
    validate, add and edit users in the local database."""

    def __init__(self, filename):
        """Initialize the class, create the user text file with the filename,
        and load the file."""
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        """Opens the users file, which is essentially the local database,
        and puts the data into the "users" variable."""
        self.file = open(self.filename, "r")
        self.users = {}
        for line in self.file:
            email, password, name = line.strip().split(";")
            self.users[email] = (password, name)
        self.file.close()

    def get_user(self, email):
        """Checks if the user's email exists in the local database."""
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        """Adds a user to the existing data, and saves it to the local database."""
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        """Checks to see if the user's password is correct based on the email and
        password entered."""
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def validate_email(self, email, full_name, new_password):
        """Check if the user's email exists in the database. If exists, check if the
        full name entered matches with the name in the database. If correct, update
        the database with the new password given by the user."""
        # If user's email already exists, continue.
        if self.get_user(email.strip()) != -1:
            # Reset the password only if the Full Name appears to be correct.
            if self.users[email][1].lower() == full_name.lower():
                self.users[email] = (new_password.strip(), self.users[email][1])
                self.save()
                return 1
            else:
                return -1
        else:
            return 0

    def save(self):
        """Saves/writes the data from the users list into the local database file."""
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + "\n")

# END OF FILE
# DEVELOPED BY PRASHANT & TEAM 12 (FIT3164)
