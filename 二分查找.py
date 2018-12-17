low = 0
high = len(list) - 1
def_list = [1, 3, 5, 7, 9]
mid = (low + high)
guess = list[mid]
if guess < item:
  low = mid + 1
def binary_search(list, item):
  low = 0
  high = len(list)-1

while low <= high:
  mid = (low + high)
  guess = list[mid]
  if guess == item:
      return mid
  if guess > item:
        high = mid - 1
  else:
      low = mid + 1
return None

print (binary_search(list, 3))
print (binary_search(list, -1))