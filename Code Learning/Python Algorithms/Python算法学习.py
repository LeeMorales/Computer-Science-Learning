#1.1 抽象数据类型和面向对象编程#############################################################################################################################
#实列1#####################################################################################################################################################
class Bag(object):
    
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._items = list()

    def add(self, item):
        if len(self) >= self.maxsize:
            raise Exception('Full')
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item
def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)


if __name__ == '__main__':
    test_bag()
##############################################################################################################################################################
#1.2 数组和列表################################################################################################################################################
#实列2########################################################################################################################################################
from array import array    # python 提供的比较原始的 array 类
arr = array('u', 'asdf')
print(arr[0], arr[1], arr[2], arr[3])
class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __len__(self):
        return self._size
    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value
    def __iter__(self):
        for item in self._items:
            yield item
def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    assert len(a) == 10