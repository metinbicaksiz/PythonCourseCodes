import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "metinbicaksiz@gmail.com"
password = ""

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Done!

# 2. Check if today matches a birthday in the birthdays.csv
now = (dt.datetime.now().month, dt.datetime.now().day)
data = pd.read_csv('birthdays.csv')
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows() }

if now in birthday_dict:
    birthday_person = birthday_dict[now]
    file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file) as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




