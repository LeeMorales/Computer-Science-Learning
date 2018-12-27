def sum(arr):
   total = 0
   for x in arr:
    total += x
   return total
print (sum([1, 2, 3, 4]))
####################################################################################
# #给定一个list
def sum(list):
#调用sum函数
      if list == []:
#基线条件
          return 0
#递归条件
          return list[0] + sum(list[1:])
#####################################################################################
def quicksort(array):
      if len(array) < 2:
       return array
      else:
             pivot = array[0]
             less = [i for i in array[1:] if i <= pivot]
             greater = [i for i in array[1:] if i > pivot]
             return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))