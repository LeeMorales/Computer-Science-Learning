print("数据结构与算法4")
def dedupe(items, key = None):
    seen = set()
    for item in items:
      if item not in seen:
         yield item
         seen.add(item)
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
           yield item
           seen.add(val)

SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost = str(records[20:32]) * float(records[40:48])

def most_freqency():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    from collections import Counter
    word_counts = Counter(words)
    # 出现频率最高的3个单词
    top_three = word_counts.most_common(3)
    print(top_three)
    # Outputs [('eyes', 8), ('the', 5), ('look', 4)]

if __name__ == '__main__':
    most_freqency()
#############################################################################################################################################
print("数据结构与算法5")
class User:
        def _init_(self, user_id):
            self.user_id = user_id
        def _repr_(self):
            return 'User({})'.format(self.user_id)
            users = [User(23). User(3), User(99)]
            sorted(User, key = lambda u: u.user_id)
rows = [
    {"'address': '1390 S Lee', 'date', '01/07/2019'"},
    {"'address': '1391 S Mark', 'date', '01/06/2019'"},
    {"'address': '1392 S ranklin', 'date' , '01/05/2019'"},
    {"'address': '1393 S Kevin', 'date' , '01/04/2019'"},
    {"'address': '1394 S Marcus', 'date' , '01/03/2019'"},
    {"'address': '1395 S Sherlock', 'date' , '01/02/2019'"},
    {"'address': '1396 S Watson', 'date' , '01/01/2019'"},
    {"'address': '1397 S Jane', 'date' , '12/31/2018'"},
    {"'address': '1398 S Miles Morales', 'date' , '12/30/2018'"}
]

from operator import itemgetter
from itertools import groupby
from collections import defaultdict
rows_by_date = defaultdict(list)
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key = itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
        for row in rows:
            rows_by_date[row['date']].append(rows)
            valuse = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(value):
    try:
       x = int(value)
       return True
    except ValueError:
       return False
def value():
    ivals = list(filter(is_int, value)) 
    print(ivals)

########################################################################################################################
print("数据结构与算法6")
prices = ("ACME:45.23", "AAPL: 612.78", "IBM: 205.55", "HPQ: 37.20", "FB: 10.75")
def tech_names():
    p1 = { key:value for key, value in prices.items() if value > 200}
    p2 = { key:value for key, value in prices.items() if key in tech_names}

from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
        return total

from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price','date', 'time'])
#创建原型元组
stock_prototype = Stock(' ', 0, 0.0, None, None)
#用来替换的函数
def dict_to_stock(s):
    return stock_prototype._replace(**s)

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
#############################################################################################################################
print("数据结构与算法7")
from collections import ChainMap
c = ChainMap('a,b')
print(c['x'])  #输出a
print(c['y'])  #输出b
print(c['z'])  #输出a