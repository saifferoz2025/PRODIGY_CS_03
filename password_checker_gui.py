import tkinter as tk
import re

def check_password_strength(password):
    length_error = len(password) < 8
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, upper_error, lower_error, digit_error, special_error])

    if score == 5:
        return "Strong 💪"
    elif 3 <= score < 5:
        return "Moderate 🙂"
    else:
        return "Weak ❌"

def evaluate_password():
    password = entry_password.get()
    strength = check_password_strength(password)
    label_result.config(text=f"Password Strength: {strength}")

# GUI Setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x200")
root.config(bg="#1e1e2e")

label_title = tk.Label(root, text="🔑 Password Strength Checker", font=("Arial", 14, "bold"), fg="white", bg="#1e1e2e")
label_title.pack(pady=10)

label_instruction = tk.Label(root, text="Enter your password:", fg="white", bg="#1e1e2e")
label_instruction.pack()

entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

btn_check = tk.Button(root, text="Check Strength", command=evaluate_password, bg="#4CAF50", fg="white", width=15)
btn_check.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="yellow", bg="#1e1e2e")
label_result.pack(pady=10)

root.mainloop()
