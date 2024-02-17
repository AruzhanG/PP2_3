from datetime import datetime

start_time = "2:13:57"
end_time = "16:35:07"

t1 =  datetime.strptime(start_time, "%H:%M:%S")
t2 = datetime.strptime(end_time, "%H:%M:%S")

difference = t2 - t1

print(difference.total_seconds())

