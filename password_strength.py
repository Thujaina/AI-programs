import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*()_+=\-{}:;\"'<>,.?/\\|`~]", password):
        strength += 1

    if strength == 5:
        remarks = "Very Strong"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"

    return remarks

# Example usage
pwd = input("Enter your password: ")
result = check_password_strength(pwd)
print(f"Password Strength: {result}")