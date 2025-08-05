import smtplib
import datetime as dt
import random
from shlex import quote

my_email = "metinbicaksiz@gmail.com"
password = ""


subject = "Quote of the day"
message = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        message = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="metinfatuation@gmail.com",
            msg=f"Subject: {subject}\n\n{message}"
        )