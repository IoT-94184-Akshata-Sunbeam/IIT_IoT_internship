import datetime

now=datetime.datetime.now()
print(f"date and time:{now}")

day=now.strftime("%A")
print(f"day:{day}")
