from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    suggestions = []

    if request.method == "POST":
        password = request.form.get("password", "")

        lo = up = nu = sp = 0

        # 🔥 Better uniqueness check (expanded list)
        common_passwords = [
            "password", "12345678", "abcd1234", "qwerty", "admin123",
            "welcome", "password123", "11111111", "iloveyou"
        ]

        # 1️⃣ Uniqueness check
        if password.lower() in common_passwords:
            result = "Weak password (too common)"
            suggestions.append("Avoid common passwords like 'admin123' or 'qwerty'")

        elif len(password) < 8:
            result = "Weak password"
            suggestions.append("Make your password at least 8 characters long")

        else:
            for i in password:
                if i.islower():
                    lo += 1
                elif i.isupper():
                    up += 1
                elif i.isdigit():
                    nu += 1
                else:
                    sp += 1

            score = 0
            if lo: score += 1
            if up: score += 1
            if nu: score += 1
            if sp: score += 1

            if score == 4:
                result = "Strong Password 💪"
            elif score >= 2:
                result = "Medium Password ⚠️"
                suggestions.append("Add uppercase letters, numbers, and symbols")
            else:
                result = "Weak Password ❌"
                suggestions.append("Mix uppercase, numbers, and special characters")

    return render_template("index.html", result=result, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)