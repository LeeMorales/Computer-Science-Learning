#二分查找
##思路：输入一列有序的元素列表，如果要查找的元素包含在列表中，二分查找返回其位置，否则返回null
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 0
high = len(list) - 1
mid = (low + high) // 2
guess = list(mid)

if guess < item:
    low = mid + 1
def binary_search(list, item):
    low = 0
    high = len(list)-1

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

print binary_search(my_list, 5)
print binary_search(my_list, 9)



