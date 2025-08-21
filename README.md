# 📧 Automated Email OTP Verification System

A simple and secure Python-based email verification system that sends and validates OTP (One-Time Password) through Gmail.

## 🌟 Features

- ✉️ Automated OTP generation and email delivery
- 🔒 Secure email verification process
- 🔄 3 attempts for OTP verification
- ⚡ Real-time validation
- 🛡️ Input validation for email addresses

## 🛠️ Technologies Used

- Python 3.x
- `smtplib` for email operations
- `email.mime` for email content formatting
- `python-dotenv` for environment variables

## 📋 Prerequisites

- Python 3.x installed
- Gmail account
- Gmail App Password (for secure authentication)
- Required Python packages:
  ```
  python-dotenv
  ```

## 🚀 Setup & Usage

1. Clone the repository
2. Install required packages:
   ```
   pip install python-dotenv
   ```
3. Set up your environment variables in a `.env` file:
   ```
   SENDER_EMAIL=your-email@gmail.com
   APP_PASSWORD=your-app-password
   ```
4. Run the script:
   ```
   python "create account through emil  otp system.py"
   ```

## 🔑 How It Works

1. 📝 User enters their Gmail address
2. 🎲 System generates a random 4-digit OTP
3. 📨 OTP is sent to the provided email
4. ✅ User gets 3 attempts to enter the correct OTP
5. 🎉 Email is verified upon correct OTP entry

## ⚠️ Security Notes

- Always use App Passwords instead of your main Gmail password
- Keep your `.env` file secure and never commit it to version control
- OTP expires after 3 failed attempts

## 👥 Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## 📄 License

This project is open source and available under the MIT License.

## 📞 Contact

kadamamit462@gmail.com
7829396954
Created by [Amit kadam] - feel free to contact me!
