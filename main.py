from datetime import datetime
import pandas
import random
import smtplib
today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    random_number = random.randint(1,3)
    birthday_person = birthdays_dict[today]
    with open(f'letter_templates/letter_{random_number}.txt') as letter:
        content = letter.read()
        new_letter = content.replace('[NAME]', birthday_person['name'])
from_email = 'test@email.com' # Your Email address
password = 'password'   # Your Password
to_email = birthday_person['email']

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=from_email, password=password)
    connection.sendmail(from_addr=from_email, to_addrs=to_email,msg=f'Subject:Happy Birthday\n\n{new_letter}')



