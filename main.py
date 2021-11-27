import random
import smtplib
import datetime as dt
import pandas
data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
today = (now.month, now.day)
MY_EMAIL = "kodmuromkar@gmail.com"
MY_PASSWORD = "abcde@1234"

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL
                            , to_addrs=birthday_person["email"]
                            , msg=f"Subject:HAPPY BIRTHDAY!\n\n {contents}")
