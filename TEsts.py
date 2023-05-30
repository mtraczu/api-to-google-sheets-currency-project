from datetime import datetime
import pytz
import time

datetime.now(pytz.timezone('GMT')).strftime("%Y-%m-%d-%H:%M:%S")

while True:
    date_time = datetime.now(pytz.timezone('GMT')).strftime("%Y-%m-%d-%H:%M:%S")
    #formatted_date_time = date_time.strftime("%Y-%m-%d-%H:%M:%S")
    print(date_time)
    time.sleep(5)



