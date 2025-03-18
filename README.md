# 🔐 Password Strength Meter

## 📌 Overview
This is a **Password Strength Meter** built using Python. It evaluates a password based on key security criteria and provides feedback to help users create stronger passwords.

## 🚀 Features
✅ Checks password strength based on:
- **Length** (minimum 8 characters)
- **Uppercase & lowercase letters**
- **At least one digit (0-9)**
- **At least one special character** (!@#$%^&*)

✅ **Rejects common weak passwords**  
✅ **Provides feedback & improvement suggestions**  
✅ **Generates a strong password if the input is weak**  

## 🛠️ Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/daniyalquest/password-strength-meter.git
cd password-strength-meter
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Program**
```bash
python app.py
```

## 📜 Usage
- Run the script and enter a password when prompted.
- The program evaluates the strength and gives feedback.
- If the password is weak, it suggests a strong alternative.

Example:
```bash
Enter your password: Hello123
⚠️ Moderate Password - Consider adding the following security features:
   - Include at least one special character (!@#$%^&*).
```

## 🔧 Future Enhancements
- **GUI Version** using Streamlit  
- **Custom Scoring Weights**  
- **Integration with a Web Application**  

## 👨‍💻 Author
Developed by **Muhammad Daniyal Ashfaq**  
📧 Contact: [daniyal2472@gmail.com](mailto:daniyal2472@gmail.com)