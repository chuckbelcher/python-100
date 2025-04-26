import datetime as dt

now = dt.datetime.now()
dayofweek = now.weekday()

if dayofweek == 0:
    print("lets send a message")
else:
    print(f"today is not the correct day, today is {dayofweek}")