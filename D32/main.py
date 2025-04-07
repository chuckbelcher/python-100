import smtplib
import datetime

# Mail Server Settings
MAILUSR = "chuckbelcherdev@gmail.com"
MAILPWD = "Add Password Here"
MAILSVR = "smtp.gmail.com"
MAILPORT = "587"


# Create a function to send an email
def send_email(subject, body, to):
    try:
        # Connect to the mail server
        server = smtplib.SMTP(MAILSVR, MAILPORT)
        server.starttls()
        server.login(MAILUSR, MAILPWD)

        # Create the email
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(MAILUSR, to, message)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()

mailrecipient = "cfbelcher@me.com"
mailbody = "This is a test email from python"
send_email("test from python", mailbody, mailrecipient)