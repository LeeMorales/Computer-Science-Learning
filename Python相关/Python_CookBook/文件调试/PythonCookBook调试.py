print("迭代器和生成器1")
def manual_iter():
    with open('D:/CodeHackProject/Examples/1.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            print('Here is the End')

def manual_iter2():
    with open('/etc/passwd') as f:
        while True:
            line = next(f)
            if line is None:
                break
            print(line, end='')
if __name__ == '__main__':
    manual_iter()

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment 

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

def gen_pattern():
    for n in frange(0, 4, 0.5):
        print(n)
    print(list(frange(0, 1, 0.125)))

    #生成器函数
    # Create the generator, notice no output appears
    c = countdown(3)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))

if __name__ == '__main__':
    gen_pattern()
###################################################################
print("迭代器和生成器3")
import itertools

def count(n):
    while True:
        yield n
        n += 1

def iter_slice():
    c = count(0)
    for x in itertools.islice(c, 10, 20):
        print(x)

if __name__ == '__main__':
    iter_slice()

from itertools import dropwhile
from itertools import islice


def skip_iter():
    items = ['a', 'b', 'c', 1, 4, 10, 15]
    for x in islice(items, None, 3):
        print(x)

if __name__ == '__main__':
    skip_iter()
######################################################################
print("文件和I/O 2")
def rw_binary():
    with open('D/CodeHackProject/Examples/1.bin', 'rb') as f:
        data = f.read()
    with open('D/CodeHackProject/Examples/1.bin', 'wb') as f:
        f.write(b'Hello World')

    # Text string
    t = 'Hello World'
    print(t[0])

    # Byte string
    b = b'Hello World'
    print(b[0])
    for c in b:
        print(c)

if __name__ == '__main__':
    rw_binary()
def write_noexist():
    with open('D/CodeHackProject/Examples/2.txt', 'wt') as f:
        f.write('BBBBBBBBBBBB')
    with open('D/CodeHackProject/Examples/2.txt', 'xt') as f:
        f.write('XXXXXXX')

if __name__ == '__main__':
    write_noexist()