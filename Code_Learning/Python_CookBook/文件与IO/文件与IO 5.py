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