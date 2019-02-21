#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

items = [1, 10, 7]
head, middle, tail = items
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
def heapq():
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
    tokens = [
        ('NAME', 'foo'), 
        ('EQ', '='), 
        ('NUM', '23'), 
        ('PLUS', '+'),
        ('NUM', '42'), 
        ('TIMES', '*'), 
        ('NUM', '10')
]
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
print("字符串与文本6")
import re
import collections

# 表述规范化
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))
# 生成器
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


# 分析器
class ExpressionEvaluator:
    '''
    Implementation of a recursive descent parser. Each method
    implements a single grammar rule. Use the ._accept() method
    to test and accept the current lookahead token. Use the ._expect()
    method to exactly match and discard the next token on on the input
    (or raise a SyntaxError if it doesn't match).
    '''

    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None  # Last symbol consumed
        self.nexttok = None  # Next symbol tokenized
        self._advance()  # Load first lookahead token
        return self.expr()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # 需要使用的语法规则
    def expr(self):
        "expression ::= term { ('+'|'-') term }*"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }*"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | ( expr )"
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


def descent_parser():
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2 + 3'))
    print(e.parse('2 + 3 * 4'))
    print(e.parse('2 + (3 + 4) * 5'))
    if __name__ == '__main__':
        descent_parser()
###########################################################################################################################
print("字符串与文本7")
import re


def byte_str():
    data = b'Hello World'
    print(data[0:5])
    print(data.startswith(b'Hello'))
    print(data.split())
    print(data.replace(b'Hello', b'Hello Cruel'))

    # 字节数组
    data = bytearray(b'Hello World')
    print(data[0:5])
    print(data.startswith(b'Hello'))
    print(data.split())
    print(data.replace(b'Hello', b'Hello Cruel'))

    # 正则式
    data = b'FOO:BAR,SPAM'
    print(re.split(b'[:,]',data))

    # 字节字符串打印不美观
    s = b'Hello World'
    print(s)
    print(s.decode('utf-8'))

    print('{:10s} {:10d} {:10.2f}'.format   ('ACME', 100, 490.1).encode('ascii'))


if __name__ == '__main__':
    byte_str()
###############################################################################################################################
print("第二章完结！")
##############################################################################################################################
print("数字，日期与时间1")
def round_num():
    print(round(1.23, 1))
    print(round(1.27, 1))
    print(round(-1.27, 1))
    print(round(1.25361,3))

    # 舍入数为负数
    a = 1627731
    print(round(a, -1))
    print(round(a, -2))
    print(round(a, -3))

    # 格式化输出
    x = 1.23456
    print(format(x, '0.2f'))
    print(format(x, '0.3f'))
    print('value is {:0.3f}'.format(x))

    # 不要自以为是的用round去修正一些精度问题
    a = 2.1
    b = 4.2
    c = a + b
    print(c)
    c = round(c, 2)  # "Fix" result (???)
    print(c)

if __name__ == '__main__':
    round_num()

from decimal import Decimal
from decimal import localcontext
import math


def acc_deciamal():
    a = 4.2
    b = 2.1
    print(a + b)
    print((a + b) == 6.3)

    # 使用decimal模块
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b)
    print((a + b) == Decimal('6.3'))

    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

    nums = [1.23e+18, 1, -1.23e+18]
    print(sum(nums))
    print(math.fsum(nums))


if __name__ == '__main__':
    acc_deciamal()

def format_number():
    x = 1234.56789
    # Two decimal places of accuracy
    print(format(x, '0.2f'))

    # Right justified in 10 chars, one-digit accuracy
    print(format(x, '>10.1f'))

    # Left justified
    print(format(x, '<10.1f'))

    # Centered
    print(format(x, '^10.1f'))

    # Inclusion of thousands separator
    print(format(x, ','))
    print(format(x, '0,.1f'))

    print(format(x, 'e'))
    print(format(x, '0.2E'))

    # strings
    print('The value is {:0,.2f}'.format(x))

    print(format(x, '0.1f'))
    print(format(-x, '0.1f'))

    swap_separators = {ord('.'): ',', ord(','): '.'}
    print(format(x, ',').translate(swap_separators))


if __name__ == '__main__':
    format_number()
###########################################################################################################################
print("数字，日期与时间2")
def bin_octal():
    x = 1234
    print(type(bin(x)))
    print(bin(x), oct(x), hex(x))

    # format() function
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    print(int('4d2', 16))
    print(int('10011010010', 2))


if __name__ == '__main__':
    bin_octal()

def int_bytes():
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))
    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))

    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))
    print(x.to_bytes(20, 'big'))


    # bit_length真有用
    x = 523 ** 23
    print(x)
    print(x.bit_length())
    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1
    print(x.to_bytes(nbytes, 'little'))

if __name__ == '__main__':
    int_bytes()

import cmath


def complex_math():
    a = complex(2, 4)
    b = 3 - 5j
    print(a.conjugate())

    # 正弦 余弦 平方根等
    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.sqrt(a))



if __name__ == '__main__':
    complex_math()
##########################################################################################################################
print("数字，日期与时间3")
def inf_nan():
    a = float('inf')
    b = float('-inf')
    c = float('nan')

    print(a + 45)
    print(a + 45 == a)
    print(a * 10 == a)
    print(10 / a)

    # undifined
    print(a / a)
    print(a + b)

    print(c + 23)
    print(c / 2 == c)  # False ?


if __name__ == '__main__':
    inf_nan()

from fractions import Fraction


def frac():
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(print(a + b))
    print(a.numerator, a.denominator)

    c = a + b
    print(float(c))
    print(type(c.limit_denominator(8)))
    print(c.limit_denominator(8))


if __name__ == '__main__':
    frac()

import numpy as np


def array_numpy():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2)
    print(x + y)

    # Numpy arrays
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)
    print(ax + ay)
    print(ax * ay)

    print(f(ax))
    print(np.sqrt(ax))
    print(np.cos(ax))

    # 大数组
    grid = np.zeros(shape=(10000, 10000), dtype=float)
    grid += 10
    print(grid)
    print(np.sin(grid))

    # 二维数组的索引操作
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    print(a[1])  # Select row 1
    print(a[:, 1])  # Select column 1
    # Select a subregion and change it
    print(a[1:3, 1:3])
    a[1:3, 1:3] += 10
    print(a)

    # Broadcast a row vector across an operation on all rows
    print(a + [100, 101, 102, 103])
    # Conditional assignment on an array
    print(np.where(a < 10, a, 10))



def f(x):
    return 3 * x ** 2 - 2 * x + 7


if __name__ == '__main__':
    array_numpy()
#########################################################################################################################
print("数字，日期和时间4")
import numpy as np


def array_numpy():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2)
    print(x + y)

    # Numpy arrays
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)
    print(ax + ay)
    print(ax * ay)

    print(f(ax))
    print(np.sqrt(ax))
    print(np.cos(ax))

    # 大数组
    grid = np.zeros(shape=(10000, 10000), dtype=float)
    grid += 10
    print(grid)
    print(np.sin(grid))

    # 二维数组的索引操作
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    print(a[1])  # Select row 1
    print(a[:, 1])  # Select column 1
    # Select a subregion and change it
    print(a[1:3, 1:3])
    a[1:3, 1:3] += 10
    print(a)

    # Broadcast a row vector across an operation on all rows
    print(a + [100, 101, 102, 103])
    # Conditional assignment on an array
    print(np.where(a < 10, a, 10))



def f(x):
    return 3 * x ** 2 - 2 * x + 7


if __name__ == '__main__':
    array_numpy()

import numpy as np
import numpy.linalg


def matrix_linear():
    m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
    print(m)

    # Return transpose  转置矩阵
    print(m.T)

    # Return inverse  # 逆矩阵
    print(m.I)


    # Create a vector and multiply
    v = np.matrix([[2],[3],[4]])
    print(v)
    print(m * v)

    # Determinant 行列式
    print(numpy.linalg.det(m))

    # Eigenvalues 特征值
    print(numpy.linalg.eigvals(m))

    # Solve for x in m*x = v
    x = numpy.linalg.solve(m, v)
    print(x)
    print(m * x)
    print(v)



if __name__ == '__main__':
    matrix_linear()

from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta


def date_time():
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    # 具体的日期
    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)
    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

    # 标准库中datetime模块
    a = datetime(2012, 9, 23)
    # a + timedelta(months=1)  # 这个会报错

    # 使用dateutil模块解决这个问题
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))

    # Time between two dates
    b = datetime(2012, 12, 21)
    d = b - a
    print(d)
    d = relativedelta(b, a)
    print(d)
    print(d.months, d.days)



if __name__ == '__main__':
    date_time()
######################################################################
print("数字，日期和时间5")
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
#创建一周的列表
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

#初始化
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


def last_friday():
    print(datetime.today())
    print(get_previous_byday('Monday'))
    print(get_previous_byday('Tuesday'))
    print(get_previous_byday('Friday'))
    print(get_previous_byday('Saturday'))
    # 显式的传递开始日期
    print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

    # 使用dateutil模块
    d = datetime.now()
    # 下一个周五
    print(d + relativedelta(weekday=FR))
    # 上一个周五
    print(d + relativedelta(weekday=FR(-1)))
    # 下一个周六， 为什么如果今天是周六，下一个/上一个都返回今天的日期？？
    print(d + relativedelta(weekday=SA))
    # 上一个周六
    print(d + relativedelta(weekday=SA(-1)))


if __name__ == '__main__':
    last_friday()

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)
    def date_range(start, stop, step):
        while start < stop:
            yield start
        start += step
        def month_range():
            a_day = timedelta(days=1)
            first_day, last_day = get_month_range()
            while first_day < last_day:
                print(first_day)
                first_day += a_day
            # 使用生成器
            for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1),
                                timedelta(hours=6)):
                print(d)
        if __name__ == '__main__':
            month_range()

from datetime import datetime, timedelta
from pytz import timezone
import pytz


def tz_local():
    d = datetime(2012, 12, 21, 9, 30, 0)
    print(d)

    # Localize the date for Chicago
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print(loc_d)

    # Convert to Bangalore time
    bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
    print(bang_d)


    # 夏令时
    d = datetime(2013, 3, 10, 1, 45)
    loc_d = central.localize(d)
    print(loc_d)
    later = loc_d + timedelta(minutes=30)
    print(later)
    # 使用normalize修正这个问题
    later = central.normalize(loc_d + timedelta(minutes=30))
    print(later)

    # 一个普遍策略是先转换为UTC时间，使用UTC时间来进行计算
    print(loc_d)
    utc_d = loc_d.astimezone(pytz.utc)
    print(utc_d)

    later_utc = utc_d + timedelta(minutes=30)
    # 转回到本地时间
    print(later_utc.astimezone(central))

    # 根据ISO 3166国家代码查找时区名称
    print(pytz.country_timezones['IN'])

if __name__ == '__main__':
    tz_local()
#####################################################################################################

##########################################################################################
print("迭代器和生成器2")
#建立树结构
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
#产生自身
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
#添加子类
    def add_child(self, node):
        self._children.append(node)
#迭代自己
    def __iter__(self):
        return iter(self._children)
#深度优先搜索来产生其它元素
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

class Node2:
    #迭代
    def __init__(self, value):
        self._value = value
        self._children = []
#产生自身
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
#添加子类
    def add_child(self, node):
        self._children.append(node)
#迭代子类
    def __iter__(self):
        return iter(self._children)
#深度优先搜索产生其它元素
    def depth_first(self):
        return DepthFirstIterator(self)

#深度优先搜索遍历所有节点
class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        #为子结点创建迭代器
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # 前进到下一个子节点并开始迭代
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

def reverse_iterate():
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)
        
class Countdown:
    def __init__(self, start):
        self.start = start

    # 正向迭代器
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # 反向迭代器
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


if __name__ == '__main__':
    reverse_iterate()

from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

def gen_extrastate():
    with open('D/CodeHackProject/Examples/1.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

if __name__ == '__main__':
    gen_extrastate()
################################################################################################

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


def iter_permutation():
    """排列组合"""

    items = ['a', 'b', 'c']

    # 全排列
    for p in permutations(items):
        print(p)

    # 指定长度
    for p in permutations(items, 2):
        print(p)

    # 组合
    for c in combinations(items, 3):
        print(c)

    # 可重复组合
    for c in combinations_with_replacement(items, 3):
        print(c)

if __name__ == '__main__':
    iter_permutation()
###################################################################################################################
print("生成器和迭代器4")
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


def iter_permutation():
    """排列组合"""

    items = ['a', 'b', 'c']

    # 全排列
    for p in permutations(items):
        print(p)

    # 指定长度
    for p in permutations(items, 2):
        print(p)

    # 组合
    for c in combinations(items, 3):
        print(c)

    # 可重复组合
    for c in combinations_with_replacement(items, 3):
        print(c)

if __name__ == '__main__':
    iter_permutation()

from collections import defaultdict


def iterate_index():
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)
    # 索引从1开始
    for idx, val in enumerate(my_list, 1):
        print(idx, val)

    # 序列中含有元组的解压
    data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
    for n, (x, y) in enumerate(data):
        print(n)
        print(x, y)


def parse_data(filename):
        with open(filename, 'rt') as f:
            for lineno, line in enumerate(f, 1):
                fields = line.split()
                try:
                    count = int(fields[1])
                    # ...
                except ValueError as e:
                    print('Line {}: Parse error: {}'.format(lineno, e))


def word_lines():
    word_summary = defaultdict(list)
    with open('myfile.txt', 'r') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        # Create a list of words in current line
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)

if __name__ == '__main__':
    iterate_index()

from itertools import zip_longest


def iterate_simul():
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)

    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a,b):
        print(i)  # 默认是按最短长度
    for i in zip_longest(a,b):
        print(i)
    for i in zip_longest(a, b, fillvalue=0):
        print(i)

    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    s = dict(zip(headers,values))

    for name, val in zip(headers, values):
        print(name, '=', val)


if __name__ == '__main__':
    iterate_simul()
###################################################################################################################################
print("生成器和迭代器5")
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

def process_pipline():
    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
    bytes = (int(x) for x in bytecolumn if x != '-')
    print('Total', sum(bytes))
    if __name__ == '__main__':
        process_pipline()

    from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    def iterable():
        for x in items:
            if isinstance(x, iterable) and not isinstance(x, ignore_types):
                yield from flatten(x)
            else:
                yield x


def flatten_seq():
    items = [1, 2, [3, 4, [5, 6], 7], 8]  
    for x in flatten(items):
        print(x)
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)

    if __name__ == '__main__':
        flatten_seq()

    import heapq


    def merge_sorted():
        a = [1, 4, 7, 10]
        b = [2, 5, 6, 11]
        for c in heapq.merge(a, b):
            print(c)

        # 合并排序文件
        with open('sorted_file_1', 'rt') as file1, \
                open('sorted_file_2', 'rt') as file2, \
                open('merged_file', 'wt') as outf:

                for line in heapq.merge(file1, file2):
                    outf.write(line)


    if __name__ == '__main__':
        merge_sorted()

    import sys

    def process_data():
        print(data)


    def reader(s, size):
        while True:
            data = s.recv(size)
            if data == b'':
                break
                # process_data(data)
    def reader2(s, size):
        for data in iter(lambda: s.recv(size), b''):
            process_data(data)
    def iterate_while():
        CHUNKSIZE = 8192
        with open('/etc/passwd') as f:
            for chunk in iter(lambda: f.read(10), ''):
                n = sys.stdout.write(chunk)


    if __name__ == '__main__':
        iterate_while()
########################################################################################################################
print("文件和I/O")
def rw_text():
    # Iterate over the lines of the file
    with open('1.txt', 'rt') as f:
        for line in f:
            # process line
            print(line)

    # Write chunks of text data
    with open('1.txt', 'wt') as f:
        f.write('text1')
        f.write('text2')

if __name__ == '__main__':
    rw_text()

def print_tofile():
    with open('D/CodeHackProject/Examples/1.txt', 'wt') as f:
        print('Hello World!', file=f)

if __name__ == '__main__':
    print_tofile()

def print_sepend():
    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=',')
    print('ACME', 50, 91.5, sep=',', end='!!\n')
    for i in range(5):
        print(i)
    for i in range(5):
        print(i, end=' ')
    print()

    row = ['ACME', 50, 91.5]
    print(*row, sep=',')

if __name__ == '__main__':
    print_sepend()
############################################################################################################################
import io
def string_io():
    s = io.StringIO()
    s.write('Hello World\n')
    print('This is a test', file=s)
    # Get all of the data written so far
    print(s.getvalue())

    # Wrap a file interface around an existing string
    s = io.StringIO('Hello\nWorld\n')
    print(s.read(4))
    print(s.read())

if __name__ == '__main__':
    string_io()
##########################################################################################################################
import gzip
import bz2


def gzip_bz2():
    with gzip.open('D/CodeHackProject/Examples/1.gz', 'rt') as f:
        text = f.read()
    with bz2.open('D/CodeHackProject/Examples/1.bz2', 'rt') as f:
        text = f.read()

    with gzip.open('D/CodeHackProject/Examples/1.gz', 'wt') as f:
        f.write(text)
    with bz2.open('D/CodeHackProject/Examples/1.bz2', 'wt') as f:
        f.write(text)
    with gzip.open('D/CodeHackProject/Examples/1.gz', 'wt', compresslevel=5) as f:
        f.write(text)

    # 作用在已打开的二进制文件上
    f = open('D/CodeHackProject/Examples/1.gz', 'rb')
    with gzip.open(f, 'rt') as g:
        text = g.read()

if __name__ == '__main__':
    gzip_bz2()

from functools import partial


def iterate_fixed():
    RECORD_SIZE = 32

    with open('D/CodeHackProject/Examples/1.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')
        for r in records:
            print(r)

if __name__ == '__main__':
    iterate_fixed()

import os.path


def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, 'rb') as f:
            f.readinto(buf)
        return buf


def read_tobuffer():
    buf = bytearray(os.path.getsize('D/CodeHackProject/Examples/1.txt'))
    print(buf)
    m1 = memoryview(buf)
    m2 = m1[-5:]
    print(m2)
    m2[:] = b'WORLD'
    print(buf)

    bytearray(b'Hello World')


if __name__ == '__main__':
    read_tobuffer()
##################################################################################################################################
print("文件和I/O 3")
import gzip
with gzip.open('1.gz', 'rt') as f:
    text = f.read()
import bz2
with bz2.open('1.bz2', 'rt') as f:
    text = f.read()
#使用gzip压缩
import gzip
with gzip.open('1.gz;, 'wt')m as f:
    f.write(text)

#使用bz2压缩
import bz2
with bz2.open('1.bz2', 'wt') as f:
    f.write(text)
from functools import partial


def iterate_fixed():
    RECORD_SIZE = 32

    with open('somefile.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')
        for r in records:
            print(r)

if __name__ == '__main__':
    iterate_fixed()
import os.path


def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, 'rb') as f:
            f.readinto(buf)
        return buf


def read_tobuffer():
    buf = bytearray(os.path.getsize('filename'))
    print(buf)
    m1 = memoryview(buf)
    m2 = m1[-5:]
    print(m2)
    m2[:] = b'WORLD'
    print(buf)

    bytearray(b'Hello World')


if __name__ == '__main__':
    read_tobuffer()
################################################################################
print("文件和I/O 4")
import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)
import os


def path_names():
    path = '/Users/beazley/Data/data.csv'
    print(os.path.basename(path))
    print(os.path.dirname(path))
    print(os.path.join('tmp', 'data', os.path.basename(path)))

    path = '~/Data/data.csv'
    print(os.path.expanduser(path))
    print(os.path.splitext(path))

if __name__ == '__main__':
    path_names()
################################################################################
print("文件和I/O 5")
import os	
import os.path
import glob
from fnmatch import fnmatch
import sys
def dir_listfile():
    names = os.listdir('somedir')
    # Get all regular files
    names = [name for name in os.listdir('somedir')
    if os.path.isfile(os.path.join('somedir', name))]
    dirnames = [name for name in os.listdir('somedir')
    if os.path.isdir(os.path.join('somedir', name))]
    pyfiles = [name for name in os.listdir('somedir')
    if name.endswith('.py')]
    pyfiles = glob.glob('somedir/*.py')
    pyfiles = [name for name in os.listdir('somedir')
    if fnmatch(name, '*.py')]
    pyfiles = glob.glob('*.py')
    # Get file sizes and modification dates
    name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
    for name in pyfiles]
    for name, size, mtime in name_sz_date:
        print(name, size, mtime)
    # Alternative: Get file metadata
        file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)
    if __name__ == '__main__':
        dir_listfile()
	def bypass_encoding():
	    print(sys.getfilesystemencoding())
	if __name__ == '__main__':
	    bypass_encoding()
    
########################################################################
print("文件与I/O 6")
def bad_filename():
    return repr(filename)[1:-1]
try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))
import urllib.request
import io
import sys
def change_open_encode():
    u = urllib.request.urlopen('http://www.python.org')
    f = io.TextIOWrapper(u, encoding='utf-8')
    text = f.read()
print(sys.stdout.encoding)

    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
    print(sys.stdout.encoding)
f = open('sample.txt','w')
    print(f)
    print(f.buffer)
    print(f.buffer.raw)
if __name__ == '__main__':
    change_open_encode()
import sys
def bytes_tofile():
    sys.stdout.buffer.write(b'Hello\n')
if __name__ == '__main__':
    bytes_tofile()
################################################################################
print("文件与I/O 7")
import os
import sys
from socket import socket, AF_INET, SOCK_STREAM
def file_descriptor():
    fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)
# Turn into a proper file
    f = open(fd, 'wt')
    f.write('hello world\n')
    f.close()
 # Create a binary-mode file for stdout
    bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
    bstdout.write(b'Hello World\n')
    bstdout.flush()
def echo_client(client_sock, addr):
    print('Got connection from', addr)
# Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)
client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)
# Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
client_sock.close()
def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)
if __name__ == '__main__':
    file_descriptor()
tempfile.Temporaryfile:
from tempfile import TemporaryFile
from tempfile import TemporaryDirectory
from tempfile import NamedTemporaryFile
import tempfile
def temp_file():
    with TemporaryFile('w+t') as f:
        # Read/write to the file
        f.write('Hello World\n')
        f.write('Testing\n')
# Seek back to beginning and read the data
        f.seek(0)
        data = f.read()
        print(data)
 with NamedTemporaryFile('w+t') as f:
        print('filename is:', f.name)
#创建一个临时目录
    with TemporaryDirectory() as dirname:
        print('dirname is:', dirname)
print(tempfile.mkstemp())
    print(tempfile.mkdtemp())
    print(tempfile.gettempdir())
if __name__ == '__main__':
    temp_file()
import serial
def serial_posts():
    ser = serial.Serial('/dev/tty.usbmodem641',  # Device name varies
                        baudrate=9600,
                        bytesize=8,
                        parity='N',
                        stopbits=1)
if __name__ == '__main__':
    serial_posts()
############################################################################
print("文件与I/O 8")
import pickle
def serailize_object():
    data = [1, 2, 3]
    f = open('somefile', 'wb')
    pickle.dump(data, f)
s = pickle.dumps(data)
# Restore from a file
    f = open('somefile', 'rb')
    data = pickle.load(f)
# Restore from a string
    data = pickle.loads(s)
f = open('somedata', 'wb')
    pickle.dump([1, 2, 3, 4], f)
    pickle.dump('hello', f)
    pickle.dump({'Apple', 'Pear', 'Banana'}, f)
    f.close()
f = open('somedata', 'rb')
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
if __name__ == '__main__':
    serailize_object()
# countdown.py
import time
import threading
class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()
def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
def __getstate__(self):
        return self.n
def __setstate__(self, n):
        self.__init__(n)
##########################################################################
print("数据编码与处理")
import csv
from collections import namedtuple


def rw_csv():
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            print(row)

    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            # Process row
            print(row.Change)

    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
    ]

    with open('stocks.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


if __name__ == '__main__':
    rw_csv()

import json
from collections import OrderedDict


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

# Dictionary mapping names to known classes
classes = {
    'Point': Point
}


def rw_json():
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }

    json_str = json.dumps(data)  # str类型
    data = json.loads(json_str)

    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # Reading data back
    with open('data.json', 'r') as f:
        data = json.load(f)

    # 使用object_pairs_hook
    s = '{"name": "ACME", "shares": 50, "price": 490.1}'
    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)

    # 解码为自定义对象
    # data = json.loads(s, object_hook=JSONObject)
    # print(data.name)
    # print(data.shares)

    print(json.dumps(data))
    print(json.dumps(data, indent=4))

    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)
    print(s)
    a = json.loads(s, object_hook=unserialize_object)
    print(a)


if __name__ == '__main__':
    rw_json()
################################################################################
