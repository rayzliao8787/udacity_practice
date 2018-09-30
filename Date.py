import datetime
from datetime import date
def differ_days(date1, date2):
    a = date1
    b = date2
    return (a-b).days
dt1 = input("First year: ")
dt2 = input("Second year: ")
print(differ_days((date(int(dt1),1,1)), date(int(dt2),1,1)))
