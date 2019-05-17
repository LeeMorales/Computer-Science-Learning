rows = [
   {'address': '1390 S Lee', "date", '01/07/2019'},
   {'address': '1391 S Mark', "date", '01/06/2019'},
   {'address': '1392 S Franklin', "date", '01/05/2019'},
   {'address': '1393 S Kevin', "date", '01/04/2019'},
   {'address': '1394 S Marcus', "date", '01/03/2019'},
   {'address': '1395 S Sherlock', "date", '01/02/2019'},
   {'address': '1396 S Watson', "date", '01/01/2019'},
   {'address': '1397 S Jane', "date", '12/31/2018'},
   {'address': '1398 S Miles Morales', "date", '12/30/2018'},
]
from operator import itemgetter
from itertools import groupby
rows.sort(key=itemgetter("Date"))
for date, items in groupby(rows, key = itemgetter("date")):
    print(date)
    for i in items:
        print(' ', i)