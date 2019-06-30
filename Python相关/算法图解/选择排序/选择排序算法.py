def findSmallest (arr):
#----------------------------------
##存储最小的值
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        smallest = arr[i]
        smallest_index = i
    return smallest_index

def selectionSort (arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
