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