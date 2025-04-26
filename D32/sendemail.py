import smtplib

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
        print(f"Email sent successfully to {to}!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()


# Mail Server Settings
MAILUSR = "chuckbelcherdev@gmail.com"
MAILPWD = "dwpi tfkf lqsw rulu"
MAILSVR = "smtp.gmail.com"
MAILPORT = "587"

mail_recipient = input("Enter the email address to send the quote to: ")
mail_body = input("What would you like to say?")

send_email("test from python", mail_body, mail_recipient)