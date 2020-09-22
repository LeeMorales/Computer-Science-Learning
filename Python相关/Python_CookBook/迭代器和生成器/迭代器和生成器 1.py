#建立树结构
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
#产生自身
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
#添加子类
    def add_child(self, node):
        self._children.append(node)
#迭代自己
    def __iter__(self):
        return iter(self._children)
#深度优先搜索来产生其它元素
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

class Node2:
    #迭代
    def __init__(self, value):
        self._value = value
        self._children = []
#产生自身
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
#添加子类
    def add_child(self, node):
        self._children.append(node)
#迭代子类
    def __iter__(self):
        return iter(self._children)
#深度优先搜索产生其它元素
    def depth_first(self):
        return DepthFirstIterator(self)

#深度优先搜索遍历所有节点
class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        #为子结点创建迭代器
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # 前进到下一个子节点并开始迭代
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

def reverse_iterate():
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)
        
class Countdown:
    def __init__(self, start):
        self.start = start

    # 正向迭代器
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # 反向迭代器
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


if __name__ == '__main__':
    reverse_iterate()

from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

def gen_extrastate():
    with open('D/CodeHackProject/Examples/1.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

if __name__ == '__main__':
    gen_extrastate()