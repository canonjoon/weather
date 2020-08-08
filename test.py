from datetime import date, timedelta 
import time
from time import localtime
from datetime import datetime


now = date.today()
now_str=now.strftime("%H%M%X")


now_time = datetime.now()

time_hour =now_time.strftime('%H:%M')


print(now)
print(time_hour)