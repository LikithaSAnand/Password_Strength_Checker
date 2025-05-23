import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letter check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Lowercase letter check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    # Special character check
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|,.<>\/?]', password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Evaluate strength
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Strong"
    elif score == 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check strength: ")
    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}\n")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f" - {suggestion}")
