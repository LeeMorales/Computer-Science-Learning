#二分查找
##思路：输入一列有序的元素列表，如果要查找的元素包含在列表中，二分查找返回其位置，否则返回null
#coding=utf-8
def binary_search(list, item):
#----------------------------------
##low和high用于跟踪要在其中的查找的列表部分
    low = 0
    high = len(list) - 1

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

print (binary_search(list, 5))
print (binary_search(list, 9))       