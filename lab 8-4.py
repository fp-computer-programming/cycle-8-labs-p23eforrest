def sum(n):
    x = 0
    #sets x variable equal to 0
    y = 0
    #sets y variable equal to 0
    while x <(n+1):
        # while x is greater than what the function outputs + 1
        y += 1
        x+=1
    return y
    
print(sum(5))