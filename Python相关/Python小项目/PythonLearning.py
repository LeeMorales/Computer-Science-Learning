#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print ('Hello world, I am Python')
print (985*211)
print (45678+0x12fd2)
print ('Learn Python in imooc')
print (100 < 99)
print (0xff == 255)
x1 = 1
d = 3
n = 100
x100 = x1+(n-1)*d
s = (x1+x100)*100/2
print (s)
s = 'Python was started in 1989 by "Guido".Python is free and easy to learn.'
print (s)
############################################################################################################
print("下面是文本文件数字比大小程序")
name = input('Enter file:')
handle = open(name, 'r')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list[counts.items()]:
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    print(bigcount, bigword)
###############################################################################################################
print("字典程序")
n = 100
s1 = ['a,b,c']
s2 = [1,2,3]
print (dict(zip(s1,s2)))
###############################################################################################################
print("A和B比大小")
a = input("imput a:")
b = input("imput b:")
if a < b:
    print (int(a)/int(b), int(a)+int(b))
else:
    print ("none")
#################################################################################################################
print("计算符")
a = int(input("imput a: "))
b = int(input("imput b: "))
c = int(input("imput c: "))
if a > b:
    print(a*b, a*b*c, c%a, a%b*c+a)
else:
    print(a%b)
##################################################################################################################
#   &	    按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
#   |	    按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
#   ^	    按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
#   ~	    按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
#   <<    左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
#   >>    右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
print("多位运算符练习")
a = 60           
b = 13            
c = 0
c = a & b        
print ("1 - c 的值为：", c)
c = a | b;        
print ("2 - c 的值为：", c)
c = a ^ b;        
print ("3 - c 的值为：", c)
c = ~a;           
print ("4 - c 的值为：", c)
c = a << 2;      
print ("5 - c 的值为：", c)
c = a >> 2;       
print ("6 - c 的值为：", c)
##############################################################################################################################
print("布尔型判断")
k = int(input("input the k: "))
z = int(input("input the z: "))
if (k and z):
    print("true")
else:
    print("none")
if (k or z):
    print("all true or one of them are true")
else:
    print("all none true")
###################################################################################################################################
print("判断数是否在列表中")
Q = int(input("input the Q: "))
W = int(input("Input the W: "))
list = [112, 223, 554, 1, 2, 3, 4, 5]
if (Q in list):
    print(Q)
else:
    print(W)
if (W not in list):
    print("not in the list")
else:
    print("W is in the list and the W is ", W)
#is	        is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
#is not	    is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
#Examples:
print("标识符练习")
e = int(input("Please input the e: "))
r = int(input("Please input the r: "))
if (id(e) == id(r)):
    print("E is R")
else:
    print("E is not R", "And The E is", e,",","The R is", r)
#交换
if (id(e) != id(r)):
    print("E is not the R")
else:
    print("E is the R")
# |  运算符                        |      描述
#-------------------------------------------------------------------------------------------------------------
# |  **	                          |     指数 (最高优先级)
# |  ~ + -	                      |     按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# |  * / % //                     |     乘，除，取模和取整除
# |  + -	                      |     加法减法
# |  >> <<                        |     右移，左移运算符
# |  &	                          |     位 'AND'
# |  ^ |                          |     位运算符
# |  <= < > >=	                    |     比较运算符
# |  <> == !=	                  |     等于运算符
# |  = %= /= //= -= += *= **=	  |     赋值运算符
# |  is/is not	                  |     身份运算符
# |  in not in	                  |     成员运算符
# |  and or not	                  |     逻辑运算符
#Example
print("常用运算符例子")
a = int(input("Input the A: "))
b = int(input("Input the B: "))
c = int(input("Input the C: "))
d = int(input("Input the D: "))
e = int(input("Input the E: "))
e = (a + b) * c / d     
print ("(a + b) * c / d 运算结果为：",  e)
e = ((a + b) * c) / d     

print ("((a + b) * c) / d 运算结果为：",  e)
e = (a + b) * (c / d);   

print ("(a + b) * (c / d) 运算结果为：",  e)
e = a + (b * c) / d;      
print ("a + (b * c) / d 运算结果为：",  e)
###############################################################################################################################
print("数值多位计算")
x = int(input("Please Input the number"))
if x >= 10:
   a = int(x * (x+1))
else:
   a = int(x**x)
print(a)

################################################################################################################################
print("斐波那契数列")
a = int(input("Please Input the A: "))
b = int(input("Please Input the B: "))

while b < 20483219993:
    print(b)
    a, b = b, a+b
##################################################################################################################################
print("LeetCode的数组排序")
class Solution:
    def removeDuplicates(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        k = 1
        nums_len = len(nums)
        while k < nums_len:
            if nums[k] == nums[k - 1]:
                del nums[k]
                nums_len -= 1
            else:
                k += 1
        return nums_len
#########################################################################################################################################
print("Leetcode算法学习")
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
#########################################################################################################################################
print("二分查找")
# 定义binary_search,但我也不知道为什么要在这定义......
def binary_search(list, item):  # low和high跟踪你将搜索的列表的哪个部分
  low = 0
  high = len(list) - 1

#只要范围没有缩小到只包含一个元素,就检查中间元素
  while low <= high:
    #查找中间数
    mid = (low + high) // 2
    guess = list[mid]
    # 找到了元素
    if guess == item:
      return mid
    # 猜的数字大了
    if guess > item:
      high = mid - 1
    # 猜的数字小了
    else:
      low = mid + 1

  # 没有指定元素
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1

# 在python中,None表示空,意味着没有找到指定的元素
print(binary_search(my_list, -1)) # => None
#################################################################################################################################
print("选择排序")
# 在数组中找到最小值
def findSmallest(arr):
  # 存储最小值
  smallest = arr[0]
  # 存储最小元素的索引
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index
# 对数组进行排序
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # 找出数组中最小的元素，并将其加入到新的数组中
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr
print(selectionSort([5, 3, 6, 2, 10]))
##################################################################################################################################
print("递归")
def greet(name):
    print ("hello")
    def greet2(name):
        print (("getting ready to say goodbye"))
    print ("bye")
#####################################################################################################################################
print("基线条件和递归条件")
def countdown(i):
    print(i)
    if i <= 1:
        return 
    else:
        countdown (i-1)
#####################################################################################################################################
print("D&C和快速排序")
def sum(arr):
       total = 0
       for x in arr:
           total += x
           return total

print (sum([1, 2, 3, 4]))     
def quicksort(array):
      if len(array) < 2:
          return array
      else:
              pivot = array[0]
              less = [i for i in array[1:] if i <= pivot]
              greater = [i for i in array[1:] if i > pivot]
              return quicksort(less) + [pivot] + quicksort(greater)
              print(quicksort([10, 5, 2, 3]))
####################################################################################################################################
print("散列表")
#创建一个空的散列表
book = dict()
#创建后，在里面添加元素
book["内存"] = 110       #一条 内存 110  元
book["CPU"] = 3700       #一颗 CPU  3700 元
book["硬盘"] = 119       #一块 硬盘 119  元
######################################################################################################################################
print("图与广度优先搜索")
from collections import deque

def person_is_seller(name):
      return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person not in searched:
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
    return False

search("you")
####################################################################################################################################################、
print("狄克斯特拉算法")
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None    
    for node in costs:
        cost = costs[node]        
        if cost < lowest_cost and node not in processed:           
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]    
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]       
        if costs[n] > new_cost:            
            costs[n] = new_cost            
            parents[n] = node   
    processed.append(node)   
    node = find_lowest_cost_node(costs)
print("Cost from the start to each node:")
print(costs)
######################################################################################################################################
print("贪婪算法")
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
  best_station = None
  states_covered = set()
  for station, states in stations.items():
    covered = states_needed & states
    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered

  states_needed -= states_covered
  final_stations.add(best_station)

print(final_stations)
###########################################################################################################################################
print("二叉树")
class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        print(self.data)
        root = Node(10)
        root.PrintTree()
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
        def insert(self, data):
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data
        def PrintTree(self):
            if self.left:
                self.left.PrintTree()
            print( self.data),
            if self.right:
                self.right.PrintTree()
    root = node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.PrintTree()
###############################################################################################################################################
print("傅里叶变换")
import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import seaborn


#采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
x=np.linspace(0,1,1400)      

#设置需要采样的信号，频率分量有180，390和600
y=7*np.sin(2*np.pi*180*x) + 2.8*np.sin(2*np.pi*390*x)+5.1*np.sin(2*np.pi*600*x)

yy=fft(y)                     #快速傅里叶变换
yreal = yy.real               # 获取实数部分
yimag = yy.imag               # 获取虚数部分

yf=abs(fft(y))                # 取绝对值
yf1=abs(fft(y))/len(x)           #归一化处理
yf2 = yf1[range(int(len(x)/2))]  #由于对称性，只取一半区间

xf = np.arange(len(y))        # 频率
xf1 = xf
xf2 = xf[range(int(len(x)/2))]  #取一半区间


plt.subplot(221)
plt.plot(x[0:50],y[0:50])   
plt.title('Original wave')

plt.subplot(222)
plt.plot(xf,yf,'r')
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表

plt.subplot(223)
plt.plot(xf1,yf1,'g')
plt.title('FFT of Mixed wave(normalization)',fontsize=9,color='r')

plt.subplot(224)
plt.plot(xf2,yf2,'b')
plt.title('FFT of Mixed wave)',fontsize=10,color='#F08080')


plt.show()

##############################################################################################################################################
print("并行，分布式算法")
import multiprocessing

def f(x):
    return x * x

cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=cores)
xs = range(5)

# method 1: map
print (pool.map(f, xs))  # prints [0, 1, 4, 9, 16]

# method 2: imap
for y in pool.imap(f, xs):
    print(y)           
for y in pool.imap_unordered(f, xs):
    print(y)           # may be in any order
###################################################################################################################################
print("数据结构与算法1")
def drop_first_last(grades):
    first = grades
    middle = grades
    last = grades
def avg(middle):
    return avg(middle)

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]
def do_foo(x,y):
    print ('foo', x, y)
def do_bar(s):
    print('bar', s)
def args():
    for tag, *args in records:
        if tag == 'foo':
            do_foo(args)
        elif tag == 'bar':
            do_bar(args)

items = [1, 10, 7]
head, middle, tail = items
print(head),
print('    ')
print(tail)

from collections import deque
def search(lines, pattern , history = 5):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
          yield line, previous_lines
        previous_lines.append(line)
########################################################################################################################################################################
print("数据结构与算法2")
from collections import deque
def heapq():
    nums = [1,8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))
    nums = [1,8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    print (heap)

import heapq
class priorityqueue:
    def _init_(self):
      self.queue = []
      self._index = 0
def push(self, item, priority, self_index):
    heapq.heappush(self._queue, (-priority, self._index, item))
    self_index += 1
def pop(self):
    return heapq.heappop(self._queue)[-1]
################################################################################################################################
print("数据结构与算法3")
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])
#####################################################################################################################################
print("数据结构与算法4")
def dedupe(items):
    """元素都是hashable"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    """元素不是hashable的时候"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def remove_dup():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe2(a, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe2(a, key=lambda d: d['x'])))


if __name__ == '__main__':
    remove_dup()

def name_slice():
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)
    print(SHARES.start)
    print(SHARES.stop)
    print(SHARES.step)

    a = slice(5, 50, 2)
    s = 'HelloWorld'
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])


if __name__ == '__main__':
    name_slice()


def most_freqency():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    from collections import Counter
    word_counts = Counter(words)
    # 出现频率最高的3个单词
    top_three = word_counts.most_common(3)
    print(top_three)
    # Outputs [('eyes', 8), ('the', 5), ('look', 4)]

if __name__ == '__main__':
    most_freqency()
#############################################################################################################################################
print("数据结构与算法5")
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))

    from operator import attrgetter
    print(sorted(users, key=attrgetter('user_id')))

    # print(sorted(users, key=attrgetter('last_name', 'first_name')))

    print(min(users, key=attrgetter('user_id')))
    print(max(users, key=attrgetter('user_id')))
if __name__ == '__main__':
    sort_notcompare()

def sort_dictlist():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print(rows_by_uid)

    rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
    print(rows_by_lfname)

if __name__ == '__main__':
    sort_dictlist()

from operator import itemgetter
from itertools import groupby


def group_iter():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))
    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)

    # defaultdict使用
    from collections import defaultdict
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

if __name__ == '__main__':
    group_iter()
from itertools import compress


def cb_filter():
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print([n for n in mylist if n > 0])
    print([n for n in mylist if n < 0])

    pos = (n for n in mylist if n > 0)
    print(pos)
    for x in pos:
        print(x, end=',')
    print()
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    def values():
        try:
            x = (val)
            return True
        except ValueError:
            return False
    ivals = list(filter(is_int, values))
    print(ivals)
    # Outputs ['1', '2', '-3', '4', '5']

    # 条件过滤
    clip_neg = [n if n > 0 else 0 for n in mylist]
    print(clip_neg)

    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [n > 5 for n in counts]
    print(list(compress(addresses, more5)))


if __name__ == '__main__':
    cb_filter()
########################################################################################################################
print("数据结构与算法6")
def sub_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}

if __name__ == '__main__':
    sub_dict()
from collections import namedtuple


def name_seq():
    subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = subscriber('jonesy@example.com', '2012-10-19')
    print(sub)
    print(sub.addr, sub.joined)

    print(len(sub))
    addr, joined = sub
    print(addr, joined)


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


def compute_cost2(records):
    Stock = namedtuple('SSS', ['name', 'shares', 'price'])
    total = 0.0
    for rec in records:
        st = Stock(*rec)
        total += st.shares * st.price
    s = Stock('ACME', 100, 123.45)
    # 更新命名元组
    s = s._replace(shares=75)
    print(s)
    return total

Stock1 = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock1('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

def default_stock():
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(dict_to_stock(a))
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(b))

if __name__ == '__main__':
    name_seq()
    # rs = [('aa', 12, 33)]
    rs = [['aa', 12, 33]]  # 元组和序列都可以
    print(compute_cost2(rs))
    default_stock()

#############################################################################################################################
print("数据结构与算法7")
import os
def trans_reduce():
    def path():
        nums = [1, 2, 3, 4, 5]
        s = sum(x * x for x in nums)
        print(s)
        files = os.listdir(path)
        if any(name.endswith('.py') for name in files):
            print('There be python!')
        else:
            print('Sorry, no python.')
        # Output a tuple as CSV
        s = ('ACME', 50, 123.45)
        print(','.join(str(x) for x in s))
        # Data reduction across fields of a data structure
        portfolio = [
            {'name':'GOOG', 'shares': 50},
            {'name':'YHOO', 'shares': 75},
            {'name':'AOL', 'shares': 20},
            {'name':'SCOX', 'shares': 65}
        ]
        
        min_shares = min(s['shares'] for s in portfolio)

        # Original: Returns 20
        min_shares = min(s['shares'] for s in portfolio)
        # Alternative: Returns {'name': 'AOL', 'shares': 20}
        min_shares = min(portfolio, key=lambda s: s['shares'])
    if __name__ == '__main__':
        trans_reduce()
    from collections import ChainMap


    def combine_map():
        a = {'x': 1, 'z': 3 }
        b = {'y': 2, 'z': 4 }
        c = ChainMap(a,b)
        print(c['x']) # Outputs 1 (from a)
        print(c['y']) # Outputs 2 (from b)
        print(c['z']) # Outputs 3 (from a)

        print(len(c))
        print(list(c.keys()))
        print(list(c.values()))

        c['z'] = 10
        c['w'] = 40
        del c['x']
        print(a)
        # del c['y']

        values = ChainMap()
        values['x'] = 1
        # Add a new mapping
        values = values.new_child()
        values['x'] = 2
        # Add a new mapping
        values = values.new_child()
        values['x'] = 3
        print(values)
        print(values['x'])
        # Discard last mapping
        values = values.parents
        print(values['x'])
        # Discard last mapping
        values = values.parents
        print(values['x'])
        print(values)


    if __name__ == '__main__':
        combine_map()
#####################################################################################################################################################################
print("第一章完成")
#################################################################################################################################################################################################################################################
print("第二章开始")
print("字符串和文本1")
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http', 'https', 'ftp:')):
        return urlopen(name) .read()
    else:
       with open(name) as f:
            return f.read()
##############################################################################################################################
print("字符串和文本2没有程序，全是shell下完成")
print("字符串与文本3")
def matchcase(word):
    def replace(m):
        text = m.group()
    def text():
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0] .isupper():
            return word.capitalize()
        else:
            return word
        return replace
#######################################################################################################################
print("字符串与文本4")
import sys

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
class SafeSub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'
def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))
def var_str():
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))
    # vars()和format_map
    a = Info('Guido', 37)
    print(s.format_map(vars(a)))
    name = 'Lisi'
    print(s.format_map(SafeSub(vars())))
    name = 'Guido'
    n = 37
    print(sub('Hello {name}'))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))
if __name__ == '__main__':
     var_str()
###################################################################################################################
print("字符串与文本5")
import textwrap
import os


def reformat_width():
    s = "No man is an island, entire it self, Every man is a piece of the continent，a part of the main."

    print(textwrap.fill(s, 70))
    print('*' * 40)
    print(textwrap.fill(s, 40))
    print('*' * 40)
    print(textwrap.fill(s, 40, initial_indent='    '))
    print('*' * 40)
    print(textwrap.fill(s, 40, subsequent_indent='    '))

import html


def html_xml():
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    print(html.escape(s))

    # Disable escaping of quotes
    print(html.escape(s, quote=False))

    s = 'Spicy Jalapeño'
    print(s.encode('ascii', errors='xmlcharrefreplace'))

if __name__ == '__main__':
    html_xml()

import re
from collections import namedtuple


def tokenize_str():
    text = 'foo = 23 + 42 * 10'
    tokens = [
        ('NAME', 'foo'), 
        ('EQ', '='), 
        ('NUM', '23'), 
        ('PLUS', '+'),
        ('NUM', '42'), 
        ('TIMES', '*'), 
        ('NUM', '10')
]
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'

    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

    scanner = master_pat.scanner('foo = 42')
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)

    # 实际生成器代码

    # Example use
    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)
    # Produces output
    # Token(type='NAME', value='foo')
    # Token(type='WS', value=' ')
    # Token(type='EQ', value='=')
    # Token(type='WS', value=' ')
    # Token(type='NUM', value='42')
    tokens = (tok for tok in generate_tokens(master_pat, text)
              if tok.type != 'WS')
    for tok in tokens:
        print(tok)

    print('*'*40)

    LT = r'(?P<LT><)'
    LE = r'(?P<LE><=)'
    EQ = r'(?P<EQ>=)'
    master_pat = re.compile('|'.join([LE, LT, EQ])) # Correct
    # master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect




def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


if __name__ == '__main__':
    tokenize_str()
#######################################################################################################################################
print("字符串与文本6")
import re
import collections

# 表述规范化
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))
# 生成器
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


# 分析器
class ExpressionEvaluator:
    '''
    Implementation of a recursive descent parser. Each method
    implements a single grammar rule. Use the ._accept() method
    to test and accept the current lookahead token. Use the ._expect()
    method to exactly match and discard the next token on on the input
    (or raise a SyntaxError if it doesn't match).
    '''

    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None  # Last symbol consumed
        self.nexttok = None  # Next symbol tokenized
        self._advance()  # Load first lookahead token
        return self.expr()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # 需要使用的语法规则
    def expr(self):
        "expression ::= term { ('+'|'-') term }*"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }*"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | ( expr )"
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


def descent_parser():
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2 + 3'))
    print(e.parse('2 + 3 * 4'))
    print(e.parse('2 + (3 + 4) * 5'))
    if __name__ == '__main__':
        descent_parser()
###########################################################################################################################
print("字符串与文本7")
import re


def byte_str():
    data = b'Hello World'
    print(data[0:5])
    print(data.startswith(b'Hello'))
    print(data.split())
    print(data.replace(b'Hello', b'Hello Cruel'))

    # 字节数组
    data = bytearray(b'Hello World')
    print(data[0:5])
    print(data.startswith(b'Hello'))
    print(data.split())
    print(data.replace(b'Hello', b'Hello Cruel'))

    # 正则式
    data = b'FOO:BAR,SPAM'
    print(re.split(b'[:,]',data))

    # 字节字符串打印不美观
    s = b'Hello World'
    print(s)
    print(s.decode('utf-8'))

    print('{:10s} {:10d} {:10.2f}'.format   ('ACME', 100, 490.1).encode('ascii'))


if __name__ == '__main__':
    byte_str()
###############################################################################################################################
print("第二章完结！")
##############################################################################################################################
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
###########################################################################################################################
print("数字，日期与时间2")
def bin_octal():
    x = 1234
    print(type(bin(x)))
    print(bin(x), oct(x), hex(x))

    # format() function
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    print(int('4d2', 16))
    print(int('10011010010', 2))


if __name__ == '__main__':
    bin_octal()

def int_bytes():
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))
    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))

    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))
    print(x.to_bytes(20, 'big'))


    # bit_length真有用
    x = 523 ** 23
    print(x)
    print(x.bit_length())
    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1
    print(x.to_bytes(nbytes, 'little'))

if __name__ == '__main__':
    int_bytes()

import cmath


def complex_math():
    a = complex(2, 4)
    b = 3 - 5j
    print(a.conjugate())

    # 正弦 余弦 平方根等
    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.sqrt(a))



if __name__ == '__main__':
    complex_math()
##########################################################################################################################
print("数字，日期与时间3")
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

import numpy as np


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
#########################################################################################################################
print("数字，日期和时间4")
import numpy as np


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

import numpy as np
import numpy.linalg


def matrix_linear():
    m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
    print(m)

    # Return transpose  转置矩阵
    print(m.T)

    # Return inverse  # 逆矩阵
    print(m.I)


    # Create a vector and multiply
    v = np.matrix([[2],[3],[4]])
    print(v)
    print(m * v)

    # Determinant 行列式
    print(numpy.linalg.det(m))

    # Eigenvalues 特征值
    print(numpy.linalg.eigvals(m))

    # Solve for x in m*x = v
    x = numpy.linalg.solve(m, v)
    print(x)
    print(m * x)
    print(v)



if __name__ == '__main__':
    matrix_linear()

from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta


def date_time():
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    # 具体的日期
    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)
    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

    # 标准库中datetime模块
    a = datetime(2012, 9, 23)
    # a + timedelta(months=1)  # 这个会报错

    # 使用dateutil模块解决这个问题
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))

    # Time between two dates
    b = datetime(2012, 12, 21)
    d = b - a
    print(d)
    d = relativedelta(b, a)
    print(d)
    print(d.months, d.days)



if __name__ == '__main__':
    date_time()
######################################################################
print("数字，日期和时间5")
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
#创建一周的列表
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

#初始化
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


def last_friday():
    print(datetime.today())
    print(get_previous_byday('Monday'))
    print(get_previous_byday('Tuesday'))
    print(get_previous_byday('Friday'))
    print(get_previous_byday('Saturday'))
    # 显式的传递开始日期
    print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

    # 使用dateutil模块
    d = datetime.now()
    # 下一个周五
    print(d + relativedelta(weekday=FR))
    # 上一个周五
    print(d + relativedelta(weekday=FR(-1)))
    # 下一个周六， 为什么如果今天是周六，下一个/上一个都返回今天的日期？？
    print(d + relativedelta(weekday=SA))
    # 上一个周六
    print(d + relativedelta(weekday=SA(-1)))


if __name__ == '__main__':
    last_friday()

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)
    def date_range(start, stop, step):
        while start < stop:
            yield start
        start += step
        def month_range():
            a_day = timedelta(days=1)
            first_day, last_day = get_month_range()
            while first_day < last_day:
                print(first_day)
                first_day += a_day
            # 使用生成器
            for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1),
                                timedelta(hours=6)):
                print(d)
        if __name__ == '__main__':
            month_range()

from datetime import datetime, timedelta
from pytz import timezone
import pytz


def tz_local():
    d = datetime(2012, 12, 21, 9, 30, 0)
    print(d)

    # Localize the date for Chicago
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print(loc_d)

    # Convert to Bangalore time
    bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
    print(bang_d)


    # 夏令时
    d = datetime(2013, 3, 10, 1, 45)
    loc_d = central.localize(d)
    print(loc_d)
    later = loc_d + timedelta(minutes=30)
    print(later)
    # 使用normalize修正这个问题
    later = central.normalize(loc_d + timedelta(minutes=30))
    print(later)

    # 一个普遍策略是先转换为UTC时间，使用UTC时间来进行计算
    print(loc_d)
    utc_d = loc_d.astimezone(pytz.utc)
    print(utc_d)

    later_utc = utc_d + timedelta(minutes=30)
    # 转回到本地时间
    print(later_utc.astimezone(central))

    # 根据ISO 3166国家代码查找时区名称
    print(pytz.country_timezones['IN'])

if __name__ == '__main__':
    tz_local()
#####################################################################################################
"""
print("迭代器和生成器1")
def manual_iter():
    with open('/CodeHackProject/1.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

def manual_iter2():
    with open('/etc/passwd') as f:
        while True:
            line = next(f)
            if line is None:
                break
            print(line, end='')
if __name__ == '__main__':
    manual_iter()

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment 

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

def gen_pattern():
    for n in frange(0, 4, 0.5):
        print(n)
    print(list(frange(0, 1, 0.125)))

    #生成器函数
    # Create the generator, notice no output appears
    c = countdown(3)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))

if __name__ == '__main__':
    gen_pattern()
"""
##########################################################################################
print("迭代器和生成器2")
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
    with open('1.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

if __name__ == '__main__':
    gen_extrastate()
################################################################################################
print("迭代器和生成器3")
"""
import itertools

def count(n):
    while True:
        yield n
        n += 1

def iter_slice():
    c = count(0)
    for x in itertools.islice(c, 10, 20):
        print(x)

if __name__ == '__main__':
    iter_slice()

from itertools import dropwhile
from itertools import islice
"""

def skip_iter():
    # with open('/etc/passwd') as f:
    #     for line in dropwhile(lambda line: line.startswith('#'), f):
    #         print(line, end='')

    # 明确知道了要跳过的元素个数
    def islice():
        items = ['a', 'b', 'c', 1, 4, 10, 15]
        for x in islice(items, None, 3):
                print(x)

    if __name__ == '__main__':
        skip_iter()

    from itertools import permutations
    from itertools import combinations
    from itertools import combinations_with_replacement


def permutation():
    """排列组合"""

    items = ['a', 'b', 'c']

    # 全排列
    for p in permutation(items):
        print(p)

    # 指定长度
    for p in permutation(items, 2):
        print(p)

    # 组合
    for c in combinations(items, 3):
        print(c)

    # 可重复组合
    for c in combinations_with_replacement(items, 3):
        print(c)

if __name__ == '__main__':
    permutation()
###################################################################################################################
print("生成器和迭代器4")
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


def iter_permutation():
    """排列组合"""

    items = ['a', 'b', 'c']

    # 全排列
    for p in permutations(items):
        print(p)

    # 指定长度
    for p in permutations(items, 2):
        print(p)

    # 组合
    for c in combinations(items, 3):
        print(c)

    # 可重复组合
    for c in combinations_with_replacement(items, 3):
        print(c)

if __name__ == '__main__':
    iter_permutation()

from collections import defaultdict


def iterate_index():
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)
    # 索引从1开始
    for idx, val in enumerate(my_list, 1):
        print(idx, val)

    # 序列中含有元组的解压
    data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
    for n, (x, y) in enumerate(data):
        print(n)
        print(x, y)


def parse_data(filename):
        with open(filename, 'rt') as f:
            for lineno, line in enumerate(f, 1):
                fields = line.split()
                try:
                    count = int(fields[1])
                    # ...
                except ValueError as e:
                    print('Line {}: Parse error: {}'.format(lineno, e))


def word_lines():
    word_summary = defaultdict(list)
    with open('myfile.txt', 'r') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        # Create a list of words in current line
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)

if __name__ == '__main__':
    iterate_index()

from itertools import zip_longest


def iterate_simul():
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)

    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a,b):
        print(i)  # 默认是按最短长度
    for i in zip_longest(a,b):
        print(i)
    for i in zip_longest(a, b, fillvalue=0):
        print(i)

    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    s = dict(zip(headers,values))

    for name, val in zip(headers, values):
        print(name, '=', val)


if __name__ == '__main__':
    iterate_simul()
###################################################################################################################################
print("生成器和迭代器5")
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

def process_pipline():
    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
    bytes = (int(x) for x in bytecolumn if x != '-')
    print('Total', sum(bytes))
    if __name__ == '__main__':
        process_pipline()

    from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    def iterable():
        for x in items:
            if isinstance(x, iterable) and not isinstance(x, ignore_types):
                yield from flatten(x)
            else:
                yield x


def flatten_seq():
    items = [1, 2, [3, 4, [5, 6], 7], 8]  
    for x in flatten(items):
        print(x)
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)

    if __name__ == '__main__':
        flatten_seq()

    import heapq


    def merge_sorted():
        a = [1, 4, 7, 10]
        b = [2, 5, 6, 11]
        for c in heapq.merge(a, b):
            print(c)

        # 合并排序文件
        with open('sorted_file_1', 'rt') as file1, \
                open('sorted_file_2', 'rt') as file2, \
                open('merged_file', 'wt') as outf:

                for line in heapq.merge(file1, file2):
                    outf.write(line)


    if __name__ == '__main__':
        merge_sorted()

    import sys

    def process_data():
        print(data)


    def reader(s, size):
        while True:
            data = s.recv(size)
            if data == b'':
                break
                # process_data(data)
    def reader2(s, size):
        for data in iter(lambda: s.recv(size), b''):
            process_data(data)
    def iterate_while():
        CHUNKSIZE = 8192
        with open('/etc/passwd') as f:
            for chunk in iter(lambda: f.read(10), ''):
                n = sys.stdout.write(chunk)


    if __name__ == '__main__':
        iterate_while()
########################################################################################################################
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
    with open('d:/CodeHackProject/1.txt', 'wt') as f:
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
############################################################################################################################
print("文件和I/O 2")
def rw_binary():
    # Read the entire file as a single byte string
    with open('D/CodeHackProject/1.bin', 'rb') as f:
        data = f.read()

    # Write binary data to a file
    with open('D:/CodeHackProject/1.bin', 'wb') as f:
        f.write(b'Hello World')

    # Text string
    t = 'Hello World'
    print(t[0])

    # Byte string
    b = b'Hello World'
    print(b[0])
    for c in b:
        print(c)

if __name__ == '__main__':
    rw_binary()

def write_noexist():
    with open('D:/CodeHackProject/1.txt', 'wt') as f:
        f.write('BBBBBBBBBBBB')
    with open('D:/CodeHackProject/1.txt', 'xt') as f:
        f.write('XXXXXXX')

if __name__ == '__main__':
    write_noexist()


import io
def string_io():
    s = io.StringIO()
    s.write('Hello World\n')
    print('This is a test', file=s)
    # Get all of the data written so far
    print(s.getvalue())

    # Wrap a file interface around an existing string
    s = io.StringIO('Hello\nWorld\n')
    print(s.read(4))
    print(s.read())

if __name__ == '__main__':
    string_io()
##########################################################################################################################
