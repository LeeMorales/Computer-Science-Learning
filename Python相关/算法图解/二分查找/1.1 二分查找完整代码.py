#二分查找
##思路：输入一列有序的元素列表，如果要查找的元素包含在列表中，二分查找返回其位置，否则返回null
#coding=utf-8
def binary_search(list, item):
#----------------------------------
##low和high用于跟踪要在其中的查找的列表部分
    low = 0
    high = len(list) - 1
#----------------------------------
##只要范围没有缩小到只包含一个元素就检查中间元素
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
#----------------------------------
##找到了元素
        if guess == item:
            return mid
#----------------------------------
##数字大了
        if guess > item :
            high = mid - 1
#----------------------------------
##数字小了
        else:
            low = mid + 1
#----------------------------------
##没有指定元素
        return None
#----------------------------------
##测试
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (binary_search(my_list, 5))
print (binary_search(my_list, 9))       