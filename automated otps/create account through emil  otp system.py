import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import os
from dotenv import load_dotenv

# Ask for a single receiver email
while True: 
    receiver_email = input("Enter your Gmail: ").strip()
    if receiver_email.endswith('@gmail.com') and " " not in receiver_email:
        print("✅ Done, Wait for second ")
        break
    else:
        print("❌ Error: Please enter a valid Gmail ending with @gmail.com")

# Load environment variables (optional)
# load_dotenv(r"c:\Users\)     user your own 

load_dotenv

# Gmail credentials
sender_email = "own email"
password = "own app password"  # App password

# Function to send email + OTP verification
def send_email():
    try:
        # Generate a random 4-digit OTP
        rand_number = random.randint(1000, 9999)
       
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Email Verification OTP"
        body = f"Hello, I am Amit. Your OTP is: {rand_number}"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail and send
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("📨 OTP sent successfully!")

        print(f"for developer {rand_number}")

        # Ask user to verify OTP
        for i in range(1, 4):
            otp = input(f" -({i})- Enter OTP (You have {3-i} chances left): ")
            if otp.isdigit() and int(otp) == rand_number:
                print("✅ Your email has been confirmed!")
                return
            else:
                print("❌ Wrong OTP!")

        print("⛔ Access Denied! Too many failed attempts.")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")

send_email()

