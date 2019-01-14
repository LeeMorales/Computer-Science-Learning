def countdown(i):
    print(i)
    if i <= 1:  #基线条件
        return
    else:       #递归条件
        countdown (i-1)