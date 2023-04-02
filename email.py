import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, message):
    # Create a MIMEText object with the message
    email_message = MIMEText(message)

    # Set the email parameters
    email_message['Subject'] = subject
    email_message['From'] = 'Your Name <eemasul303@gmail.com>'
    email_message['To'] = to_address

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            # Start the TLS encryption
            smtp.starttls()

            # Login to the SMTP server
            smtp.login('eemasul303@gmail.com', 'Sameeis123')

            # Send the email
            smtp.send_message(email_message)

        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Error sending email: {e}")

def contact():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    message = input("Enter your message: ")

    # Send the email
    send_email(email, f"New message from {name}", message)

contact()
