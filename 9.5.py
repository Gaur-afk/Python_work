class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


anika = User('anika', 'harode', 'aharode', 'aharode@example.com', 'virginia')
anika.describe_user()
anika.greet_user()

print("\nMaking 3 login attempts...")
anika.increment_login_attempts()
anika.increment_login_attempts()
anika.increment_login_attempts()
print("  Login attempts: " + str(anika.login_attempts))

print("Resetting login attempts...")
anika.reset_login_attempts()
print("  Login attempts: " + str(anika.login_attempts))