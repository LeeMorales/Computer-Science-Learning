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
for word, count in list(counts.items()):
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
while b < 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    print(b)
    a, b = b, a+b
##################################################################################################################################
print("LeetCode的数组排序")
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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

##########################################################################################################################################
print("生成器")
 
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()

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
##############################################################################################################################################
print("二叉树")
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        print(self.data)
root = Node(10)
root.PrintTree()
class Node:
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
root = Node(12)
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
####################################################################################################################################################################
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

items = [1, 10, 7, 4, 5, 9]
head, tail = items
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
nums = int[1,8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
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
    seen = set()
    for item in items:
      if item not in seen:
         yield item
         seen.add(item)

def dedupe(items, key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
           yield item
           seen.add(val)

SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost = int(records[20:32]) * float(records[40:48])

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
        def _init_(self, user_id):
            self.user_id = user_id
        def _repr_(self):
            return 'User({})'.format(self.user_id)
            users = [User(23). User(3), User(99)]
            sorted(User, key = lambda u: u.user_id)
rows = [
    {"'address': '1390 S Lee', 'date', '01/07/2019'"},
    {"'address': '1391 S Mark', 'date', '01/06/2019'"},
    {"'address': '1392 S ranklin', 'date' , '01/05/2019'"},
    {"'address': '1393 S Kevin', 'date' , '01/04/2019'"},
    {"'address': '1394 S Marcus', 'date' , '01/03/2019'"},
    {"'address': '1395 S Sherlock', 'date' , '01/02/2019'"},
    {"'address': '1396 S Watson', 'date' , '01/01/2019'"},
    {"'address': '1397 S Jane', 'date' , '12/31/2018'"},
    {"'address': '1398 S Miles Morales', 'date' , '12/30/2018'"}
]

from operator import itemgetter
from itertools import groupby
from collections import defaultdict
rows_by_date = defaultdict(list)
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key = itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
        for row in rows:
            rows_by_date[row['date']].append(rows)
            valuse = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(value):
    try:
       x = int(value)
       return True
    except ValueError:
       return False
def value():
    ivals = list(filter(is_int, value)) 
    print(ivals)
########################################################################################################################
print("数据结构与算法6")
prices = ("ACME:45.23", "AAPL: 612.78", "IBM: 205.55", "HPQ: 37.20", "FB: 10.75")
def tech_names():
#创建一个价格大于200的字典
    p1 = { key:value for key, value in prices.items() if value > 200}
#创建一个技术类的股票
    p2 = { key:value for key, value in prices.items() if key in tech_names}

from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
        return total

from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price','date', 'time'])
#创建原型元组
stock_prototype = Stock(' ', 0, 0.0, None, None)
#用来替换的函数
def dict_to_stock(s):
    return stock_prototype._replace(**s)

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
#############################################################################################################################
print("数据结构与算法7")
from collections import ChainMap
def a():
    def b():
        c = ChainMap(a,b)
        print(c['x'])  #输出a
        print(c['y'])  #输出b
        print(c['z'])  #输出a
##############################################################################################################################
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
    tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
              ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
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
############################################################################################################################
