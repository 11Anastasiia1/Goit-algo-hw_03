# 1. Варіант рішення


from datetime import datetime, date
now = datetime.today()
current_date = now.date()
year = int(input("Enter the year:"))
month = int(input("Enter the month:"))
day = int(input("Enter the day:"))
specific_date = date(year, month, day)
print(specific_date)
Dif = current_date - specific_date
print (f" Today is {current_date}, {Dif} have passed since {specific_date}.")


# 2. Варіант рішення

from datetime import datetime

# Вводимо рядок дати з клавіатури у форматі 'РРРР-ММ-ДД'
date_str = input("Введіть дату у форматі РРРР-ММ-ДД: ")

# Перетворюємо рядок дати в об'єкт datetime
given_date = datetime.strptime(date_str, '%Y-%m-%d')

# Отримуємо поточну дату
current_date = datetime.today()

# Розраховуємо різницю між поточною датою та заданою датою
difference = current_date - given_date

# Виводимо різницю в днях як ціле число
print(f"Різниця в днях: {difference.days}")

