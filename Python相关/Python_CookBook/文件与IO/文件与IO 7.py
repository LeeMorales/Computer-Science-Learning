def bad_filename():
    return repr(/Users/leemorales/Documents/Computer-Science-Learning/Examples/1.txt)[1:-1]
try:
    print(/Users/leemorales/Documents/Computer-Science-Learning/Examples/1.txt)
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