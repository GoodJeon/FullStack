import datetime

dt_now = datetime.datetime.now()
current = dt_now.date()
i = 3
re_date = current - datetime.timedelta(days=i)
print(re_date)