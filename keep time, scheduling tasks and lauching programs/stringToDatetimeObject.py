import datetime

dt1 = datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
print(dt1)

dt2 = datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(dt2)

dt3 = datetime.datetime.strptime("October of '19", "%B of '%y")
print(dt3)

dt4 = datetime.datetime.strptime("November of '63", "%B of '%y")
print(dt4)
