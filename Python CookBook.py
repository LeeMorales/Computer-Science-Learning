print("数据结构与算法1")
def drop_first_last(grades):
    first = grades
    middle = grades
    last = grades
def avg(middle):
    return avg(middle)

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]
def do_foo(x,y):
    print ('foo', x, y)
def do_bar(s):
    print('bar', s)
def args():
    for tag, *args in records:
        if tag == 'foo':
            do_foo(args)
        elif tag == 'bar':
            do_bar(args)

items = [1, 10, 7, 4, 5, 9]
head, tail = items
print(head),
print('    ')
print(tail)

from collections import deque
def search(lines, pattern , history = 5):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
          yield line, previous_lines
        previous_lines.append(line)
########################################################################################################################################################################
print("数据结构与算法2")
from collections import deque
nums = [1,8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
nums = [1,8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print (heap)
import heapq
class priorityqueue:
    def _init_(self):
      self.queue = []
      self._index = 0
def push(self, item, priority, self_index):
    heapq.heappush(self._queue, (-priority, self._index, item))
    self_index += 1
def pop(self):
    return heapq.heappop(self._queue)[-1]
################################################################################################################################
print("数据结构与算法3")
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])
#####################################################################################################################################
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
cost = int(records[20:32]) * float(records[40:48])

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
##############################################################################################################################
print("第一章完成")
#################################################################################################################################################################################################################################################
print("第二章开始")
print("字符串和文本1")
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http', 'https', 'ftp:')):
        return urlopen(name) .read()
    else:
       with open(name) as f:
            return f.read()
##############################################################################################################################
print("字符串和文本2没有程序，全是shell下完成")
print("字符串与文本3")
def matchcase(word):
    def replace(m):
        text = m.group()
    def text():
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0] .isupper():
            return word.capitalize()
        else:
            return word
        return replace
#######################################################################################################################
print("字符串与文本4")
import sys

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


class SafeSub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'


def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))

def var_str():
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))

    # vars()和format_map
    a = Info('Guido', 37)
    print(s.format_map(vars(a)))

    name = 'Lisi'
    print(s.format_map(SafeSub(vars())))

    name = 'Guido'
    n = 37
    print(sub('Hello {name}'))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))


if __name__ == '__main__':
    var_str()

###################################################################################################################
print("字符串与文本5")
import textwrap
import os


def reformat_width():
    s = "No man is an island, entire it self, Every man is a piece of the continent，a part of the main."

    print(textwrap.fill(s, 70))
    print('*' * 40)
    print(textwrap.fill(s, 40))
    print('*' * 40)
    print(textwrap.fill(s, 40, initial_indent='    '))
    print('*' * 40)
    print(textwrap.fill(s, 40, subsequent_indent='    '))

import html


def html_xml():
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    print(html.escape(s))

    # Disable escaping of quotes
    print(html.escape(s, quote=False))

    s = 'Spicy Jalapeño'
    print(s.encode('ascii', errors='xmlcharrefreplace'))

if __name__ == '__main__':
    html_xml()

import re
from collections import namedtuple


def tokenize_str():
    text = 'foo = 23 + 42 * 10'
    tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
              ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'

    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

    scanner = master_pat.scanner('foo = 42')
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)

    # 实际生成器代码

    # Example use
    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)
    # Produces output
    # Token(type='NAME', value='foo')
    # Token(type='WS', value=' ')
    # Token(type='EQ', value='=')
    # Token(type='WS', value=' ')
    # Token(type='NUM', value='42')
    tokens = (tok for tok in generate_tokens(master_pat, text)
              if tok.type != 'WS')
    for tok in tokens:
        print(tok)

    print('*'*40)

    LT = r'(?P<LT><)'
    LE = r'(?P<LE><=)'
    EQ = r'(?P<EQ>=)'
    master_pat = re.compile('|'.join([LE, LT, EQ])) # Correct
    # master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect




def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


if __name__ == '__main__':
    tokenize_str()
#######################################################################################################################################
