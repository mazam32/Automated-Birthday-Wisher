import smtplib
import datetime as dt
import random

quote = ""
my_email = "muhammadhamdazam@gmail.com"
password = "rdjzhbibpbvnfpnh"
now = dt.datetime.now()
if now.weekday() == 4:
    with open(file= "/Users/muhammadhamdazam/Documents/Python Programs/Day 32/quotes.txt", mode= "r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user= my_email, password= password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="hamdazam1@gmail.com", 
                msg= f"Subject:Friday Motivation\n\n{quote}"
            )
