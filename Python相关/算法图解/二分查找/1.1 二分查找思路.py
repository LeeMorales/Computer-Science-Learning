#二分查找
##思路：输入一列有序的元素列表，如果要查找的元素包含在列表中，二分查找返回其位置，否则返回null
#coding=utf-8
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def binary_search(list, item):
#--------------------------------
##查找范围
    low = 0
    high = len(list)-1
#--------------------------------
##检查中间元素
    mid = (low + high) // 2
    guess = list(mid)
#--------------------------------
##如果猜的数字小了，就相应的修改low
    if guess < item:
        low = mid + 1
#--------------------------------
##如果猜的数字大了，就修改high
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item :
            high = mid - 1
        else:
            low = mid + 1
        return None
#---------------------------------
##输出结果
print (binary_search(list, 5))
print (binary_search(list, 9))



