"""
Q2) Drone Weight Checker
-------------------------
Take the drone's body weight and payload weight as input, output the
total weight, and print whether the total is greater than 2 kg.

Creative twist: the user is asked to choose the unit (kg or grams) for
each input. If grams are chosen, the value is converted to kg before
adding, since 1 kg = 1000 g.
"""


def get_weight_in_kg(label):
    """
    Helper function that asks the user for a weight value and the unit
    it is given in, then returns the equivalent weight in kilograms.
    'label' is just a description (e.g. 'Body weight') used in the prompt.
    """
    # Ask which unit the user wants to enter the weight in
    unit = input(f"Enter unit for {label} (kg/g): ").strip().lower()

    # Ask for the numeric value; float() allows decimal weights
    value = float(input(f"Enter {label} (in {unit}): "))

    # Convert to kg depending on the chosen unit
    if unit == "g":
        return value / 1000  # 1000 grams = 1 kg
    else:
        return value  # already in kg (default assumption)


# Step 1: Get body weight in kg (handles both kg and gram input)
body_weight = get_weight_in_kg("Body weight")

# Step 2: Get payload weight in kg (handles both kg and gram input)
payload_weight = get_weight_in_kg("Payload weight")

# Step 3: Calculate total weight by simple addition
total_weight = body_weight + payload_weight

# Step 4: Print the total weight, rounded to 2 decimal places for neatness
print(f"\nOutput: {round(total_weight, 2)} kg")

# Step 5: Compare total weight against the 2 kg threshold and print result
if total_weight > 2:
    print("Total weight is greater than 2 kg")
elif total_weight == 2:
    print("Total weight is exactly 2 kg")
else:
    print("Total weight is less than 2 kg")
