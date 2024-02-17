import datetime

today = datetime.datetime.now()

today_without_micro_seconds = today.replace(microsecond = 0)

print(today_without_micro_seconds)