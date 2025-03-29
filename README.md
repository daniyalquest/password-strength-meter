# 🔒 Password Strength Checker & Generator

This is a **Streamlit-based web application** that provides two main functionalities: checking the strength of a password and generating secure passwords. It is designed to help users create and evaluate strong passwords to enhance their online security.

---

## 🚀 Features

### 1. Password Strength Checker
- Evaluates the strength of a password based on the following criteria:
  - Minimum length of 8 characters.
  - Contains both uppercase and lowercase letters.
  - Includes at least one numeric digit (0-9).
  - Contains at least one special character (`!@#$%^&*`).
- Provides feedback messages:
  - **Error**: For missing criteria.
  - **Warning**: For moderate passwords.
  - **Success**: For strong passwords.

### 2. Password Generator
- Generates strong, random passwords with:
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one digit.
  - At least one special character.
- Allows users to customize the password length (minimum 8 characters, maximum 32 characters).

---

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-repo/password-checker-generator.git]
   cd password-checker-generator
