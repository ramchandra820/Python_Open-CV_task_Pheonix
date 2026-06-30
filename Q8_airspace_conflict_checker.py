"""
Q8) Restricted Airspace Conflict Checker
--------------------------------------------
Use set operations to check planned flight zones against restricted and
cleared zones.
"""

planned_zones = {"Z1", "Z2", "Z3", "Z5", "Z7"}
restricted_zones = {"Z3", "Z5", "Z6", "Z8"}
cleared_zones = {"Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8"}

# ----------------------------------------------------------------------
# 1. Find which planned zones are restricted (intersection)
# ----------------------------------------------------------------------
# '&' (or .intersection()) returns elements common to BOTH sets
conflicting_zones = planned_zones & restricted_zones
print(f"Planned zones that are restricted (conflicts): {conflicting_zones}\n")

# ----------------------------------------------------------------------
# 2. Find zones that are planned but NOT restricted (safe zones)
# ----------------------------------------------------------------------
# '-' (or .difference()) returns elements in the first set but not the second
safe_zones = planned_zones - restricted_zones
print(f"Safe planned zones (not restricted): {safe_zones}\n")

# ----------------------------------------------------------------------
# 3. Zones in either planned or restricted, but NOT both (symmetric difference)
# ----------------------------------------------------------------------
# '^' (or .symmetric_difference()) returns elements in exactly one of the two sets
sym_diff_zones = planned_zones ^ restricted_zones
print(f"Zones in planned OR restricted but not both: {sym_diff_zones}\n")

# ----------------------------------------------------------------------
# 4. Check if planned_zones is a subset of cleared_zones
# ----------------------------------------------------------------------
is_subset = planned_zones.issubset(cleared_zones)
if is_subset:
    print(f"All planned zones ({planned_zones}) are cleared for flight. Mission approved.\n")
else:
    print(f"WARNING: Not all planned zones are cleared! Mission needs review.\n")

# ----------------------------------------------------------------------
# 5. Add "Z9" to planned_zones and remove "Z7" (added by mistake)
# ----------------------------------------------------------------------
planned_zones.add("Z9")     # .add() inserts a single new element into the set
planned_zones.discard("Z7")  # .discard() removes an element safely (no error if missing)
print(f"Updated planned zones: {planned_zones}\n")

# ----------------------------------------------------------------------
# 6. Print the count of unique zones across all three sets combined
# ----------------------------------------------------------------------
# '|' (or .union()) combines all sets, automatically removing duplicates
all_unique_zones = planned_zones | restricted_zones | cleared_zones
print(f"All unique zones combined: {all_unique_zones}")
print(f"Count of unique zones across all three sets: {len(all_unique_zones)}")
