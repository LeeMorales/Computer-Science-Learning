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