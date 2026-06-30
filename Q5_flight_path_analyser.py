"""
Q5) Flight Path Analyser
---------------------------
Analyse a list of altitude readings: find max altitude, average,
climb rates, steepest climb/descent, and trim zero-altitude entries.
"""

altitudes = [0, 15, 42, 78, 120, 118, 115, 50, 20, 0]

# ----------------------------------------------------------------------
# 1. Find the maximum altitude and the index ("second") it occurred at
# ----------------------------------------------------------------------
max_altitude = max(altitudes)          # highest value in the list
max_index = altitudes.index(max_altitude)  # first index where it occurs (acts as the "second")
print(f"Maximum altitude: {max_altitude}m, occurred at second/index: {max_index}")

# ----------------------------------------------------------------------
# 2. Calculate the average altitude (rounded to 2 decimal places)
# ----------------------------------------------------------------------
average_altitude = round(sum(altitudes) / len(altitudes), 2)
print(f"Average altitude: {average_altitude}m")

# ----------------------------------------------------------------------
# 3. Create climb_rates list: climb_rates[i] = altitudes[i+1] - altitudes[i]
# ----------------------------------------------------------------------
# range(len(altitudes) - 1) stops one short so we never read past the list end
climb_rates = [altitudes[i + 1] - altitudes[i] for i in range(len(altitudes) - 1)]
print(f"Climb rates between consecutive readings: {climb_rates}")

# ----------------------------------------------------------------------
# 4. Find the steepest climb (max positive rate) and steepest descent (min/most negative rate)
# ----------------------------------------------------------------------
steepest_climb = max(climb_rates)     # largest positive change = fastest ascent
steepest_descent = min(climb_rates)   # most negative change = fastest descent
print(f"Steepest climb: {steepest_climb}m/step")
print(f"Steepest descent: {steepest_descent}m/step")

# ----------------------------------------------------------------------
# 5. Remove all zero-altitude entries and print the trimmed path
# ----------------------------------------------------------------------
# List comprehension keeps only values that are NOT equal to 0
trimmed_path = [alt for alt in altitudes if alt != 0]
print(f"Trimmed flight path (zero-altitude entries removed): {trimmed_path}")
