class UserProfile:
    def __init__(self, username):
        self.username = username

# 1. Ask the user for input
name = input("Enter your username: ")

# 2. Pass it into the class
user = UserProfile(name)

print(f"Created profile for: {user.username}")