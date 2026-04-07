#!/usr/bin/env python3
# =======================================
# Password Strength Checker by SHIVAMxCSA
# For educational purposes only
# =======================================

import re

def check_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("  [!] Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("  [!] Add uppercase letters (A-Z)")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("  [!] Add lowercase letters (a-z)")

    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("  [!] Add numbers (0-9)")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("  [!] Add special characters (!@#$%^&*)")

    # Common passwords check
    common = ["password", "123456", "qwerty", "abc123", "password123"]
    if password.lower() in common:
        score = 0
        feedback.append("  [!] This is a very common password — change it!")

    # Result
    print("\n==================================================")
    if score <= 2:
        print("  Strength : WEAK ❌")
    elif score <= 4:
        print("  Strength : MODERATE ⚠️")
    else:
        print("  Strength : STRONG ✅")

    print(f"  Score    : {score}/6")
    print("==================================================")

    if feedback:
        print("  Suggestions to improve:")
        for tip in feedback:
            print(tip)
    else:
        print("  Great password! No suggestions.")

    print("==================================================\n")

if __name__ == "__main__":
    print("==================================================")
    print("     Password Strength Checker by SHIVAMxCSA")
    print("==================================================")
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        if password.lower() == 'quit':
            print("  Goodbye!")
            break
        check_password(password)