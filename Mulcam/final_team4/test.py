import datetime
from socket import timeout
from sqlite3 import Time

dt_now = datetime.datetime.now()
i = 14
re_date = (dt_now - datetime.timedelta(hours=i)).date()
print(re_date)