import smtplib


# my_email = "muhammadhamdazam@gmail.com"
# password = "rdjzhbibpbvnfpnh"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user= my_email, password= password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="hamdazam1@gmail.com", 
#         msg= "Subject:Hello\n\nHi"
#     )
    
import datetime as dt

date_of_birth = dt.datetime(year= 2004, month= 8, day= 14, hour= 6)
print(date_of_birth)