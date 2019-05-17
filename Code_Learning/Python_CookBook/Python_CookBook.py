#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
            process_data(15)
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
tempfile.Temporaryfile
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
###################################