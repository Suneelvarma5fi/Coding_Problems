def power_sum(x,n,num):
    if num**n > x:
        return 0
    elif num**n == x:
        return 1
    else:
        return power_sum(x,n,num+1)+power_sum((x-num**n),n,num+1)