#!/usr/bin/env python3

password = input("Enter your password: ")

def check_password_strength(password):

    if len(password) < 8:
        print("Password is too short — it must be at least 8 characters.")
        return False

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
        return False
    
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
        return False
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        print("Password must contain at least one digit (0–9).")
        return False

    has_special_char = False
    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|"
    for char in password:
        if char in special_characters:
            has_special_char = True
            break
    if not has_special_char:
        print("Password must contain at least one special character (e.g., !, @, #, $, %).")
        return False
        
    return True


result = check_password_strength(password)

if result:
    print("Strong password!")
else:
    print("Please try again.")
