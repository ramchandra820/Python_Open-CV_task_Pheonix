"""
Q7) Fleet Health Monitor
----------------------------
Manage a dictionary-of-dictionaries representing a drone fleet: add,
remove, filter, find minimum, bulk-update, and summarise.
"""

fleet = {
    "PX4_001": {"battery": 87, "altitude": 120, "status": "active", "payload_kg": 1.2},
    "PX4_002": {"battery": 23, "altitude": 0, "status": "grounded", "payload_kg": 0},
    "PX4_003": {"battery": 56, "altitude": 85, "status": "active", "payload_kg": 0.8},
    "PX4_004": {"battery": 11, "altitude": 30, "status": "returning", "payload_kg": 0.5},
}

# ----------------------------------------------------------------------
# 1. Add "PX4_005" with battery=95, altitude=0, status="standby", payload_kg=0
# ----------------------------------------------------------------------
fleet["PX4_005"] = {"battery": 95, "altitude": 0, "status": "standby", "payload_kg": 0}
print("After adding PX4_005:")
print(fleet, "\n")

# ----------------------------------------------------------------------
# 2. Remove "PX4_002" using .pop() and print its details before removal
# ----------------------------------------------------------------------
# .pop(key) removes the key AND returns its value in one step
removed_drone = fleet.pop("PX4_002")
print(f"Removed PX4_002, its details were: {removed_drone}\n")

# ----------------------------------------------------------------------
# 3. Print all active drones and their battery levels
# ----------------------------------------------------------------------
print("Active drones and battery levels:")
for drone_id, info in fleet.items():
    if info["status"] == "active":
        print(f"{drone_id}: {info['battery']}%")
print()

# ----------------------------------------------------------------------
# 4. Find the drone with the lowest battery among drones currently in the air (altitude > 0)
# ----------------------------------------------------------------------
airborne_drones = {d_id: info for d_id, info in fleet.items() if info["altitude"] > 0}

if airborne_drones:
    # min() with a key function finds the dict entry with the smallest battery value
    lowest_battery_id = min(airborne_drones, key=lambda d_id: airborne_drones[d_id]["battery"])
    print(f"Lowest battery among airborne drones: {lowest_battery_id} "
          f"({airborne_drones[lowest_battery_id]['battery']}%)\n")
else:
    print("No drones currently airborne.\n")

# ----------------------------------------------------------------------
# 5. Update every drone with battery < 30 to status = "critical_low_battery"
# ----------------------------------------------------------------------
for drone_id, info in fleet.items():
    if info["battery"] < 30:
        info["status"] = "critical_low_battery"

print("Fleet after critical battery status update:")
print(fleet, "\n")

# ----------------------------------------------------------------------
# 6. Print a final formatted fleet summary
# ----------------------------------------------------------------------
print("===== FINAL FLEET SUMMARY =====")
for drone_id, info in fleet.items():
    print(f"{drone_id} | Battery: {info['battery']}% | Altitude: {info['altitude']}m | "
          f"Status: {info['status']} | Payload: {info['payload_kg']}kg")
