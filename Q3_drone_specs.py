"""
Q3) Drone Specifications Analyzer
-----------------------------------
Given the drone specs below, calculate max payload, print variable types,
check if it can carry a camera, and convert takeoff weight to grams (int).
"""

# ----- Given drone specifications -----
max_takeoff_weight = 4.5     # kg, float -> heaviest the drone can weigh fully loaded
frame_weight = 1.2           # kg, float -> weight of the bare frame
battery_weight = 0.8         # kg, float -> weight of the battery
num_propellers = 4           # int       -> number of propellers fitted
motor_weight = 0.075         # kg per motor, float
is_gps_enabled = True         # bool      -> whether GPS module is fitted
gps_module_weight = 0.05     # kg, float -> weight of the GPS module

# ----------------------------------------------------------------------
# 1. Calculate the maximum payload the drone can carry
# ----------------------------------------------------------------------
# Total weight of all motors = weight per motor * number of propellers/motors
total_motor_weight = motor_weight * num_propellers

# Start with the structural (non-payload) weight: frame + battery + motors
structural_weight = frame_weight + battery_weight + total_motor_weight

# Add GPS module weight only if GPS is actually enabled/fitted
if is_gps_enabled:
    structural_weight += gps_module_weight

# Max payload = max takeoff weight - everything that isn't payload
max_payload = max_takeoff_weight - structural_weight

print(f"Total motor weight: {total_motor_weight} kg")
print(f"Total structural weight (frame+battery+motors+gps): {round(structural_weight, 3)} kg")
print(f"Maximum payload the drone can carry: {round(max_payload, 3)} kg\n")

# ----------------------------------------------------------------------
# 2. Print the type() of each variable
# ----------------------------------------------------------------------
print("Variable types:")
print(f"max_takeoff_weight -> {type(max_takeoff_weight)}")
print(f"frame_weight        -> {type(frame_weight)}")
print(f"battery_weight       -> {type(battery_weight)}")
print(f"num_propellers       -> {type(num_propellers)}")
print(f"motor_weight         -> {type(motor_weight)}")
print(f"is_gps_enabled       -> {type(is_gps_enabled)}")
print(f"gps_module_weight    -> {type(gps_module_weight)}\n")

# ----------------------------------------------------------------------
# 3. Check whether payload is enough to carry a 1.8 kg camera
# ----------------------------------------------------------------------
camera_weight = 1.8  # kg
can_carry_camera = max_payload >= camera_weight  # boolean comparison
print(f"Can the drone carry a {camera_weight} kg camera? {can_carry_camera}\n")

# ----------------------------------------------------------------------
# 4. Convert max_takeoff_weight to grams and store as an int
# ----------------------------------------------------------------------
# 1 kg = 1000 g; int() truncates any decimal part after conversion
max_takeoff_weight_grams = int(max_takeoff_weight * 1000)
print(f"Max takeoff weight in grams (int): {max_takeoff_weight_grams} -> type: {type(max_takeoff_weight_grams)}")
