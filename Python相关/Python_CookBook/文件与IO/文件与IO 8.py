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