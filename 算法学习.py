list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
low = 0
high = len(list) = 1
mid = (low+high) // 2
guess = list[mid]
if guess < item:
    low = mid + 1
def binary_search(list,item):
    low = 0
    high = len(list)-1

while low <= high:
    mid = (low+high)
    guess = list[mid]
    if guess ==item:
        return mid
    if guess > item:
        high = mid - 1
    else:
        low = mid + 1        
    return None
