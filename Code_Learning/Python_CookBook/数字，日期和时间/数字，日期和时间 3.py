print("数字，日期与时间3")
import numpy as np
def inf_nan():
    a = float('inf')
    b = float('-inf')
    c = float('nan')

    print(a + 45)
    print(a + 45 == a)
    print(a * 10 == a)
    print(10 / a)

    # undifined
    print(a / a)
    print(a + b)

    print(c + 23)
    print(c / 2 == c)  # False ?


if __name__ == '__main__':
    inf_nan()

from fractions import Fraction


def frac():
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(print(a + b))
    print(a.numerator, a.denominator)

    c = a + b
    print(float(c))
    print(type(c.limit_denominator(8)))
    print(c.limit_denominator(8))


if __name__ == '__main__':
    frac()



def array_numpy():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2)
    print(x + y)

    # Numpy arrays
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)
    print(ax + ay)
    print(ax * ay)

    print(f(ax))
    print(np.sqrt(ax))
    print(np.cos(ax))

    # 大数组
    grid = np.zeros(shape=(10000, 10000), dtype=float)
    grid += 10
    print(grid)
    print(np.sin(grid))

    # 二维数组的索引操作
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    print(a[1])  # Select row 1
    print(a[:, 1])  # Select column 1
    # Select a subregion and change it
    print(a[1:3, 1:3])
    a[1:3, 1:3] += 10
    print(a)

    # Broadcast a row vector across an operation on all rows
    print(a + [100, 101, 102, 103])
    # Conditional assignment on an array
    print(np.where(a < 10, a, 10))



def f(x):
    return 3 * x ** 2 - 2 * x + 7


if __name__ == '__main__':
    array_numpy()