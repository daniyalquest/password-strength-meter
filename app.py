import re
import random
import string
import streamlit as st

COMMON_PASSWORDS = {
    "password", "123456", "password123", "qwerty", "admin", "letmein", "12345678", "abc123"
}

def generate_strong_password(length=12):
    if length < 8:
        length = 8

    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    rest = [random.choice(all_chars) for _ in range(remaining_length)]

    password_list = list(upper + lower + digit + special + "".join(rest))
    random.shuffle(password_list)
    return "".join(password_list)

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        st.error("❌ This password is too common and insecure. Please choose a more unique password.")
        return

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding the following security features:")
        for f in feedback:
            st.write("   -", f)
    else:
        st.error("❌ Weak Password - Please improve it by:")
        for f in feedback:
            st.write("   -", f)
        suggestion = generate_strong_password()
        st.info("💡 Consider using a strong password like: " + suggestion)

if __name__ == "__main__":
    st.title("Password Strength Meter")
    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Password Strength"):
        check_password_strength(password)