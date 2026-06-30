"""
Q1) Drone Movement Selector
----------------------------
Take the number (index of the option) as input from the user and perform
the corresponding drone movement (Roll / Pitch / Yaw).
"""

# Step 1: Display the available movement options to the user
print("Drone Movement Options:")
print("1. Roll")
print("2. Pitch")
print("3. Yaw")

# Step 2: Take the option number as input from the user
# int() converts the string input into an integer for comparison
choice = int(input("Enter the index of the movement option (1/2/3): "))

# Step 3: Use if-elif-else to decide which movement to perform based on choice
if choice == 1:
    # Roll -> rotation about the front-to-back (longitudinal) axis
    # To roll, the drone slows down motors on one side and speeds up the other
    print("Output: Slow down left motors for left roll OR slow down right motors for right roll")

elif choice == 2:
    # Pitch -> rotation about the side-to-side (lateral) axis
    # To pitch, the drone slows down front motors (move forward) or back motors (move backward)
    print("Output: Slow down front motors to pitch forward OR slow down rear motors to pitch backward")

elif choice == 3:
    # Yaw -> rotation about the vertical axis (drone spins/rotates in place)
    # To yaw, the drone changes the speed of diagonally opposite motor pairs
    print("Output: Increase speed of clockwise motors to yaw left OR increase speed of counter-clockwise motors to yaw right")

else:
    # Handles any input that is not 1, 2, or 3
    print("Invalid choice! Please enter 1 (Roll), 2 (Pitch), or 3 (Yaw).")
