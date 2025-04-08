import smtplib
import datetime
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
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()

quotes = get_quotes()
selected_quote = choice(quotes)

# Mail Server Settings
MAILUSR = "chuckbelcherdev@gmail.com"
MAILPWD = "Add Password Here"
MAILSVR = "smtp.gmail.com"
MAILPORT = "587"
mail_recipient = input("Enter the email address to send the quote to: ")

now = datetime.datetime.now()
weekday = now.weekday()

mail_body = selected_quote
if weekday == 0:
    print(f"Sending email to {mail_recipient} with quote: \n{mail_body}")
else:
    print(f"Today is not the correct day, no email will be sent.")



# send_email("test from python", mailbody, mailrecipient)