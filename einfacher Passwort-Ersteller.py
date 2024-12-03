import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*()-_+=<>?/"

length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_special = input("Include special characters? (y/n): ").lower() == "y"

character_pool = lowercase
if include_uppercase:
    character_pool += uppercase
if include_numbers:
    character_pool += numbers
if include_special:
    character_pool += special_characters
    password = "".join(random.choice(character_pool) for _ in range(length))
    
    print("Your generated password is:", password)