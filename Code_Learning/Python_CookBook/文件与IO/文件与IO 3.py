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