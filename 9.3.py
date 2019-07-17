class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

vedant = User('vedant', 'vajre', 'vvajre', 'vvajre@example.com', 'virginia')
vedant.describe_user()
vedant.greet_user()

anika = User('anika', 'harode', 'aharode', 'aharode@example.com', 'virginia')
anika.describe_user()
anika.greet_user()