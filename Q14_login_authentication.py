"""
Q14) Drone Login Authentication
------------------------------------
Take a user id and password, convert both to lowercase, and compare
against predefined credentials.
"""

# Predefined (correct) credentials, stored already in lowercase
PREDEFINED_USER_ID = "admin"
PREDEFINED_PASSWORD = "drone123"

# Take user input for id and password
entered_user_id = input("Enter user id: ")
entered_password = input("Enter password: ")

# Convert both entered values to lowercase before comparing
# (this makes the login case-insensitive, e.g. "Admin" == "admin")
entered_user_id_lower = entered_user_id.lower()
entered_password_lower = entered_password.lower()

# Compare with the predefined credentials
if entered_user_id_lower == PREDEFINED_USER_ID and entered_password_lower == PREDEFINED_PASSWORD:
    print("Drone connected successfully")
else:
    print("Connection failed: Invalid user id or password")
