
# No Vowels
# Demonstrates creating new strings with a for loop


message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("A new string has been created: ", new_message)

print("\nYour message without vowels: ", new_message)



