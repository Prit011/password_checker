def check_password(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*" for char in password):
        strength += 1

    if strength <= 2:
        return "Weak ❌"
    elif strength == 3 or strength == 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"


password = input("Enter your password: ")
print("Strength:", check_password(password))