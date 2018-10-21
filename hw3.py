import datetime
from datetime import date
def differ_days(date1, date2):
    a = date1
    b = date2
    return ((a-b).days) + 1
dt1 = input("First year: ")
mt1= input("First month: ")
dy1 = input("First day: ")
dt2 = input("Second year: ")
mt2 = input("Second month: ")
dy2 = input("Second day: ")
print(differ_days((date(int(dt1),int(mt1),int(dy1))), date(int(dt2),int(mt2),int(dy2))))
