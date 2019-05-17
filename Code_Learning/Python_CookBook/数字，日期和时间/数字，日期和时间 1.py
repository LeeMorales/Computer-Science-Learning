print("数字，日期与时间1")
def round_num():
    print(round(1.23, 1))
    print(round(1.27, 1))
    print(round(-1.27, 1))
    print(round(1.25361,3))

    # 舍入数为负数
    a = 1627731
    print(round(a, -1))
    print(round(a, -2))
    print(round(a, -3))

    # 格式化输出
    x = 1.23456
    print(format(x, '0.2f'))
    print(format(x, '0.3f'))
    print('value is {:0.3f}'.format(x))

    # 不要自以为是的用round去修正一些精度问题
    a = 2.1
    b = 4.2
    c = a + b
    print(c)
    c = round(c, 2)  # "Fix" result (???)
    print(c)

if __name__ == '__main__':
    round_num()

from decimal import Decimal
from decimal import localcontext
import math


def acc_deciamal():
    a = 4.2
    b = 2.1
    print(a + b)
    print((a + b) == 6.3)

    # 使用decimal模块
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b)
    print((a + b) == Decimal('6.3'))

    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

    nums = [1.23e+18, 1, -1.23e+18]
    print(sum(nums))
    print(math.fsum(nums))


if __name__ == '__main__':
    acc_deciamal()

def format_number():
    x = 1234.56789
    # Two decimal places of accuracy
    print(format(x, '0.2f'))

    # Right justified in 10 chars, one-digit accuracy
    print(format(x, '>10.1f'))

    # Left justified
    print(format(x, '<10.1f'))

    # Centered
    print(format(x, '^10.1f'))

    # Inclusion of thousands separator
    print(format(x, ','))
    print(format(x, '0,.1f'))

    print(format(x, 'e'))
    print(format(x, '0.2E'))

    # strings
    print('The value is {:0,.2f}'.format(x))

    print(format(x, '0.1f'))
    print(format(-x, '0.1f'))

    swap_separators = {ord('.'): ',', ord(','): '.'}
    print(format(x, ',').translate(swap_separators))


if __name__ == '__main__':
    format_number()