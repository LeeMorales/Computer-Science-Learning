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
#############################################################################################################################################
print("二叉树2")

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

from collections import deque:
def search(lines, pattern , history = 5):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
          yield line, previous_lines
        previous_lines.append(line)
########################################################################################################################################################################
print("数据结构与算法2")
from collections import deque
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