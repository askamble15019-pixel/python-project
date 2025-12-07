# Random Password Generator
# Oasis Infobyte Internship Project

import random
import string
import sys

print("------ RANDOM PASSWORD GENERATOR ------\n")

# take password length from user
while True:
    length_input = input("Enter password length (minimum 4): ")
    try:
        length = int(length_input)
        if length < 4:
            print("Length should be at least 4. Try again.\n")
        else:
            break
    except ValueError:
        print("Please enter a valid number.\n")

# ask user what to include
print("\nChoose what to include in password:")
use_lower = input("Include lowercase letters? (y/n): ").strip().lower()
use_upper = input("Include uppercase letters? (y/n): ").strip().lower()
use_digits = input("Include digits? (y/n): ").strip().lower()
use_symbols = input("Include symbols? (y/n): ").strip().lower()

# check at least one type is selected
if use_lower != "y" and use_upper != "y" and use_digits != "y" and use_symbols != "y":
    print("\nError: You must select at least one character type.")
    sys.exit()

# create character set
char_set = ""
password_list = []

if use_lower == "y":
    char_set += string.ascii_lowercase
    password_list.append(random.choice(string.ascii_lowercase))

if use_upper == "y":
    char_set += string.ascii_uppercase
    password_list.append(random.choice(string.ascii_uppercase))

if use_digits == "y":
    char_set += string.digits
    password_list.append(random.choice(string.digits))

if use_symbols == "y":
    char_set += string.punctuation
    password_list.append(random.choice(string.punctuation))

# if user gave very small length (less than selected types), handle that
if length < len(password_list):
    print("\nError: Password length is too small for selected options.")
    print("You selected", len(password_list), "types but length is", length)
    sys.exit()

# fill remaining length with random characters
while len(password_list) < length:
    password_list.append(random.choice(char_set))

# shuffle so that mandatory characters are not always at the start
random.shuffle(password_list)

# join list to make final password string
password = "".join(password_list)

print("\nYour generated password is:")
print(password)
print("\nKeep it safe! :)")
print("---------------------------------------")
