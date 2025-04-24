import re

def check_password_strength(password):
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check for digits
    if re.search(r"[0-9]", password):
        score += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Evaluate strength
    if score <= 2:
        return "Weak"
    elif 3 <= score <= 4:
        return "Moderate"
    else:
        return "Strong"

# Example usage
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
