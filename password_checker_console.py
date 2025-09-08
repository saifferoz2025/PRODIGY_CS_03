import re

def check_password_strength(password):
    # Criteria checks
    length_error = len(password) < 8
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Calculate strength score
    score = 5 - sum([length_error, upper_error, lower_error, digit_error, special_error])

    # Feedback
    if score == 5:
        return "Strong 💪"
    elif 3 <= score < 5:
        return "Moderate 🙂"
    else:
        return "Weak ❌"

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print("\nPassword Strength:", result)

if __name__ == "__main__":
    main()