# Send a random quote if the day is Tuesday
import smtplib
import datetime as dt
from random import choice

def get_quotes():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    return [quote.strip() for quote in quotes]

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

mail_recipient = input("Enter the email address to send the quote to: ") or "cfbelcher@me.com"


now = dt.datetime.now()
dayofweek = now.weekday()

guotes = get_quotes()
mail_body = choice(guotes)

if dayofweek == 4:
    print("lets send a message")
    send_email("test from python", mail_body, mail_recipient)
else:
    print(f"today is not the correct day, today is {dayofweek} no message will be sent")

# write a function to send an email to olivia@someemail.com
