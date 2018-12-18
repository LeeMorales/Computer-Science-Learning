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
c = a & b;        
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
