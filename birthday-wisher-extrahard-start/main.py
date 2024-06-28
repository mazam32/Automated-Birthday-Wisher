import pandas as pd
import datetime as dt
import random
import smtplib
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "birthdays.csv")

my_email = "muhammadhamdazam@gmail.com"
password = "rdjzhbibpbvnfpnh"

now = dt.datetime.now()
todays_day = now.day
todays_month = now.month

info = pd.read_csv(path)
email_list = info[(info.month == todays_month) & (info.day == todays_day)].email.tolist()
name_list = info[(info.month == todays_month) & (info.day == todays_day)].name.tolist()
index = 0

for name in name_list:
    letter_number = random.randint(1,3)
    letter_path = os.path.join(base_dir, f"letter_templates/letter_{letter_number}.txt")
    with open(letter_path, mode= "r") as file:
        default_text = file.read()
        new_text = default_text.replace("[NAME]", name)
        new_text = new_text.replace("Angela", "Muhammad Hamd")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user= my_email, password= password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=email_list[index], 
                msg= f"Subject:Happy Birthday!\n\n{new_text}"
            )
    index += 1



