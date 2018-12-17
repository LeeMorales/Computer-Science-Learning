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