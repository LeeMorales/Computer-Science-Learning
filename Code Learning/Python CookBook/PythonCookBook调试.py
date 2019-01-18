print("数据结构与算法4")
def dedupe(items):
    """元素都是hashable"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    """元素不是hashable的时候"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def remove_dup():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe2(a, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe2(a, key=lambda d: d['x'])))


if __name__ == '__main__':
    remove_dup()

def name_slice():
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)
    print(SHARES.start)
    print(SHARES.stop)
    print(SHARES.step)

    a = slice(5, 50, 2)
    s = 'HelloWorld'
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])


if __name__ == '__main__':
    name_slice()


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
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))

    from operator import attrgetter
    print(sorted(users, key=attrgetter('user_id')))

    # print(sorted(users, key=attrgetter('last_name', 'first_name')))

    print(min(users, key=attrgetter('user_id')))
    print(max(users, key=attrgetter('user_id')))
if __name__ == '__main__':
    sort_notcompare()

def sort_dictlist():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print(rows_by_uid)

    rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
    print(rows_by_lfname)

if __name__ == '__main__':
    sort_dictlist()

from operator import itemgetter
from itertools import groupby


def group_iter():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))
    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)

    # defaultdict使用
    from collections import defaultdict
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

if __name__ == '__main__':
    group_iter()
from itertools import compress


def cb_filter():
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print([n for n in mylist if n > 0])
    print([n for n in mylist if n < 0])

    pos = (n for n in mylist if n > 0)
    print(pos)
    for x in pos:
        print(x, end=',')
    print()

    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    def values():
        try:
            x = (val)
            return True
        except ValueError:
            return False
    ivals = list(filter(is_int, values))
    print(ivals)
    # Outputs ['1', '2', '-3', '4', '5']

    # 条件过滤
    clip_neg = [n if n > 0 else 0 for n in mylist]
    print(clip_neg)

    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [n > 5 for n in counts]
    print(list(compress(addresses, more5)))


if __name__ == '__main__':
    cb_filter()
########################################################################################################################
print("数据结构与算法6")
def sub_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}

if __name__ == '__main__':
    sub_dict()
from collections import namedtuple


def name_seq():
    subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = subscriber('jonesy@example.com', '2012-10-19')
    print(sub)
    print(sub.addr, sub.joined)

    print(len(sub))
    addr, joined = sub
    print(addr, joined)


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


def compute_cost2(records):
    Stock = namedtuple('SSS', ['name', 'shares', 'price'])
    total = 0.0
    for rec in records:
        st = Stock(*rec)
        total += st.shares * st.price
    s = Stock('ACME', 100, 123.45)
    # 更新命名元组
    s = s._replace(shares=75)
    print(s)
    return total

Stock1 = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock1('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

def default_stock():
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(dict_to_stock(a))
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(b))

if __name__ == '__main__':
    name_seq()
    # rs = [('aa', 12, 33)]
    rs = [['aa', 12, 33]]  # 元组和序列都可以
    print(compute_cost2(rs))
    default_stock()

#############################################################################################################################
print("数据结构与算法7")
import os
def trans_reduce():
    def path():
        nums = [1, 2, 3, 4, 5]
        s = sum(x * x for x in nums)
        print(s)
        files = os.listdir(path)
        if any(name.endswith('.py') for name in files):
            print('There be python!')
        else:
            print('Sorry, no python.')
        # Output a tuple as CSV
        s = ('ACME', 50, 123.45)
        print(','.join(str(x) for x in s))
        # Data reduction across fields of a data structure
        portfolio = [
            {'name':'GOOG', 'shares': 50},
            {'name':'YHOO', 'shares': 75},
            {'name':'AOL', 'shares': 20},
            {'name':'SCOX', 'shares': 65}
        ]
        min_shares = min(s['shares'] for s in portfolio)

        # Original: Returns 20
        min_shares = min(s['shares'] for s in portfolio)
        # Alternative: Returns {'name': 'AOL', 'shares': 20}
        min_shares = min(portfolio, key=lambda s: s['shares'])

    if __name__ == '__main__':
        trans_reduce()

    from collections import ChainMap


    def combine_map():
        a = {'x': 1, 'z': 3 }
        b = {'y': 2, 'z': 4 }
        c = ChainMap(a,b)
        print(c['x']) # Outputs 1 (from a)
        print(c['y']) # Outputs 2 (from b)
        print(c['z']) # Outputs 3 (from a)

        print(len(c))
        print(list(c.keys()))
        print(list(c.values()))

        c['z'] = 10
        c['w'] = 40
        del c['x']
        print(a)
        # del c['y']

        values = ChainMap()
        values['x'] = 1
        # Add a new mapping
        values = values.new_child()
        values['x'] = 2
        # Add a new mapping
        values = values.new_child()
        values['x'] = 3
        print(values)
        print(values['x'])
        # Discard last mapping
        values = values.parents
        print(values['x'])
        # Discard last mapping
        values = values.parents
        print(values['x'])
        print(values)


    if __name__ == '__main__':
        combine_map()