import datetime

today = datetime.datetime.now()
fivedaysago = today - datetime.timedelta(days=5)

print(fivedaysago)
