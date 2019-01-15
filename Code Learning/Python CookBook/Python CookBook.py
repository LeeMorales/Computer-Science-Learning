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
"""
import os
def trans_reduce():
    nums = [1, 2, 3, 4, 5]
    s = sum(x * x for x in nums)
    print(s)

    files = os.listdir('D:\CodeHackProject\1.txt')
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
"""
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
