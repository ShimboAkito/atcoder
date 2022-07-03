import datetime

k = int(input())

calc_source = datetime.datetime(2017, 11, 12, 21, 00, 00)
print((calc_source + datetime.timedelta(minutes=k)).strftime("%H:%M"))