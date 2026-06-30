"""
Q16) Lowercase to Uppercase using ord() and chr()
------------------------------------------------------
Convert a single lowercase letter to uppercase using ONLY ord() and
chr() — no built-in string methods like .upper() allowed.

Background (ASCII):
- Lowercase letters 'a' to 'z' occupy ASCII codes 97 to 122.
- Uppercase letters 'A' to 'Z' occupy ASCII codes 65 to 90.
- The gap between a lowercase letter and its uppercase version is
  always exactly 32 (e.g. ord('a')=97, ord('A')=65, 97-65=32).
- So subtracting 32 from a lowercase letter's ASCII code gives the
  ASCII code of its uppercase equivalent.
"""

letter = input("Enter the letter: ")

# Get the ASCII (numeric) code of the entered character
ascii_code = ord(letter)

# Subtract 32 to shift from lowercase range (97-122) to uppercase range (65-90)
uppercase_ascii_code = ascii_code - 32

# Convert the new ASCII code back into a character
uppercase_letter = chr(uppercase_ascii_code)

print(f"Output: {uppercase_letter}")
