"""
Q9) Auto Return-to-Home (RTH) System
----------------------------------------
Check independent safety trigger rules and simulate a stepped descent
that drains battery as the drone descends.
"""

drone_state = {
    "battery": 18,
    "altitude": 95,
    "signal_strength": 40,   # percent
    "distance_from_home": 850,  # metres
    "wind_speed": 38,        # km/h
    "obstacle_detected": True
}

# ----------------------------------------------------------------------
# 1. Check ALL RTH trigger rules INDEPENDENTLY (each its own 'if', not elif)
#    so that more than one warning can fire at the same time.
# ----------------------------------------------------------------------
triggered_any = False  # tracks whether at least one rule fired

if drone_state["battery"] < 20:
    print("CRITICAL: RTH triggered — Low Battery")
    triggered_any = True

if drone_state["signal_strength"] < 30:
    print("WARNING: RTH triggered — Signal Lost")
    triggered_any = True

if drone_state["wind_speed"] > 35:
    print("WARNING: RTH triggered — High Wind")
    triggered_any = True

if drone_state["obstacle_detected"] is True:
    print("CAUTION: Obstacle detected — Rerouting")
    triggered_any = True

# If none of the rules above triggered anything, everything is fine
if not triggered_any:
    print("All systems nominal")

print()  # blank line separator before the descent simulation

# ----------------------------------------------------------------------
# 2 & 3. While loop: simulate descent from current altitude to 0 in steps
#         of 15m, draining 1% battery per 15m descended, printing each step.
# ----------------------------------------------------------------------
current_altitude = drone_state["altitude"]
current_battery = drone_state["battery"]

print("Starting descent simulation...")
while current_altitude > 0:
    # Decide how much to descend this step: 15m, but not below 0
    step = min(15, current_altitude)
    current_altitude -= step      # descend by the step amount
    current_battery -= 1          # drain 1% battery for this descent step

    # Guard so displayed battery never goes negative even in edge cases
    display_battery = max(current_battery, 0)

    print(f"Altitude: {current_altitude}m | Battery: {display_battery}%")

print("Descent complete. Drone has landed.")
