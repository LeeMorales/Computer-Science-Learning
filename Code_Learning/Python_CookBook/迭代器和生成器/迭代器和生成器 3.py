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