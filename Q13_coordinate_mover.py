"""
Q13) Drone Coordinate Mover
-------------------------------
Take starting (x, y) coordinates, a movement direction, and number of
steps. Print the updated coordinate after EACH single-unit move.
"""

# Take both coordinates together on one line, e.g. "5,3" or "5 3"
raw_coords = input("Enter the starting coordinates as x,y: ")

# Split on comma (and strip spaces) to support "5,3" or "5, 3"
x_str, y_str = raw_coords.replace(" ", "").split(",")
x, y = int(x_str), int(y_str)

# Ask for movement direction
direction = input("Enter movement (horizontal or vertical): ").strip().lower()

# Ask for number of steps to move
steps = int(input("Enter the number of steps: "))

print("Output:", end=" ")

# Move one unit at a time, printing the coordinate after each single move
for _ in range(steps):
    if direction == "horizontal":
        x += 1  # horizontal movement changes the x-coordinate
    elif direction == "vertical":
        y += 1  # vertical movement changes the y-coordinate
    else:
        print("\nInvalid direction! Please enter 'horizontal' or 'vertical'.")
        break

    # Print the coordinate after this single-unit move (no newline, like sample output)
    print(f"({x},{y})", end=" ")

print()  # final newline for clean formatting
