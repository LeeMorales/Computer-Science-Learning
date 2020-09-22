def sum(arr):
    Total = 0
    sum = input("Please input your array")
    if sum < 0:
        print("Total is unvaild")
    elif sum == 0:
        print("Total is 0")
    else:
        for x in sum:
            Total += x
            return print (Total)  
