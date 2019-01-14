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
####################################################################################################################
print("Python算法图解完成")