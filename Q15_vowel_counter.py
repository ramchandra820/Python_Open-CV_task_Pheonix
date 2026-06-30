"""
Q15) Vowel Counter
----------------------
Take a string from the user, print it, and count the number of vowels
(a, e, i, o, u — both uppercase and lowercase) present in it.
"""

text = input("Enter a string: ")

vowels = "aeiouAEIOU"  # all vowels, both cases

count = 0
for char in text:
    if char in vowels:
        count += 1

print(f"String entered: {text}")
print(f"Number of vowels present: {count}")
