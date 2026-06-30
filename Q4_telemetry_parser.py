"""
Q4) Drone Telemetry Log Parser
---------------------------------
Parse a pipe-separated telemetry string, extract individual fields,
check status, replace a value, and print a formatted summary.
"""

telemetry = "DRONE_ID:PX4_001|ALT:120.5m|SPEED:18.3kmph|BATT:67%|STATUS:HOVERING|GPS:23.0225N,72.5714E"

# ----------------------------------------------------------------------
# 1. Extract Drone ID, Altitude (float), Speed (float), Battery (int), GPS
# ----------------------------------------------------------------------
# Split the whole string on "|" to get each "KEY:VALUE" field as a list
fields = telemetry.split("|")
# fields = ['DRONE_ID:PX4_001', 'ALT:120.5m', 'SPEED:18.3kmph', 'BATT:67%', 'STATUS:HOVERING', 'GPS:23.0225N,72.5714E']

# Build a dictionary {KEY: VALUE} by splitting each field on the first ":"
data = {}
for field in fields:
    key, value = field.split(":", 1)  # split only on the first colon
    data[key] = value

# Drone ID is already a plain string, no cleanup needed
drone_id = data["DRONE_ID"]

# Altitude has a trailing "m" -> strip it and convert to float
altitude = float(data["ALT"].rstrip("m"))

# Speed has a trailing "kmph" -> strip it and convert to float
speed = float(data["SPEED"].rstrip("kmph"))

# Battery has a trailing "%" -> strip it and convert to int
battery = int(data["BATT"].rstrip("%"))

# GPS coordinates are already in "lat,long" form, e.g. "23.0225N,72.5714E"
gps_coords = data["GPS"]

status = data["STATUS"]

print("Extracted Telemetry Data:")
print(f"Drone ID : {drone_id}")
print(f"Altitude : {altitude} (type: {type(altitude)})")
print(f"Speed    : {speed} (type: {type(speed)})")
print(f"Battery  : {battery} (type: {type(battery)})")
print(f"GPS      : {gps_coords}\n")

# ----------------------------------------------------------------------
# 2. Check if status contains "HOVER" (case-insensitive)
# ----------------------------------------------------------------------
# .upper() normalises both sides so the comparison ignores letter case
is_hovering = "HOVER" in status.upper()
print(f"Is the drone hovering? {is_hovering}\n")

# ----------------------------------------------------------------------
# 3. Replace "HOVERING" with "RETURNING_HOME"
# ----------------------------------------------------------------------
# .replace() works on the original telemetry string and returns a NEW string
updated_telemetry = telemetry.replace("HOVERING", "RETURNING_HOME")
print("Updated telemetry string:")
print(updated_telemetry)
print()

# ----------------------------------------------------------------------
# 4. Print a formatted summary using f-strings
# ----------------------------------------------------------------------
summary = f"[{drone_id}] Alt: {altitude}m | Batt: {battery}% | Coords: {gps_coords.replace(',', ', ')}"
print("Formatted Summary:")
print(summary)
