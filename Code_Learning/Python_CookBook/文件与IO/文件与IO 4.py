print("文件和I/O 4")
import gzip
with gzip.open('1.gz', 'rt') as f:
    text = f.read()
import bz2
with bz2.open('1.bz2', 'rt') as f:
    text = f.read()

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