"""
Q6) Waypoint Mission Planner
-------------------------------
Work with a tuple of waypoint tuples: counting, unpacking, finding the
highest altitude waypoint, membership check, and demonstrating tuple
immutability.
"""

waypoints = (
    ("WP1", 23.0225, 72.5714, 50),
    ("WP2", 23.0312, 72.5801, 80),
    ("WP3", 23.0401, 72.5900, 100),
    ("WP4", 23.0225, 72.5714, 0),
)

# ----------------------------------------------------------------------
# 1. Print the total number of waypoints
# ----------------------------------------------------------------------
print(f"Total number of waypoints: {len(waypoints)}\n")

# ----------------------------------------------------------------------
# 2. Use tuple unpacking to print each waypoint's details in a formatted line
# ----------------------------------------------------------------------
print("Waypoint details:")
for wp in waypoints:
    # Unpack the 4 elements of each waypoint tuple directly into named variables
    name, lat, lon, alt = wp
    print(f"{name}: Latitude={lat}, Longitude={lon}, Altitude={alt}m")
print()

# ----------------------------------------------------------------------
# 3. Find the waypoint with the highest altitude using a loop
# ----------------------------------------------------------------------
# Start by assuming the first waypoint has the highest altitude
highest_wp = waypoints[0]

for wp in waypoints:
    # wp[3] is the altitude element of the waypoint tuple
    if wp[3] > highest_wp[3]:
        highest_wp = wp  # found a new highest -> update

print(f"Waypoint with highest altitude: {highest_wp[0]} at {highest_wp[3]}m\n")

# ----------------------------------------------------------------------
# 4. Check if ("WP2", 23.0312, 72.5801, 80) exists in waypoints
# ----------------------------------------------------------------------
target_wp = ("WP2", 23.0312, 72.5801, 80)
exists = target_wp in waypoints  # 'in' checks membership inside the tuple of tuples
print(f"Does {target_wp} exist in waypoints? {exists}\n")

# ----------------------------------------------------------------------
# 5. Try to modify WP1's altitude to 60 -> catch the error (tuples are immutable)
# ----------------------------------------------------------------------
try:
    # Tuples (and the inner waypoint tuples) do NOT support item assignment
    waypoints[0][3] = 60
except TypeError:
    # TypeError is raised because tuples don't allow modification after creation
    print("Waypoint data is immutable — mission integrity protected!")
