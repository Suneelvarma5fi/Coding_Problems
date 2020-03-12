
def check(l,i,j,checklist):
    if (i,j) in checklist:
        return 'yes'
    elif i>=0 and j>=0:
        try:
            x = 1 if l[i][j] else 0
            return x
        except IndexError:
            return 0
    else:
        return 0
    
def fun(arr,i,j,checked):
    x = check(arr,i,j,checked)
    if x == 'yes':
        return 1
    elif x == 1:
        checked.append((i,j))
        fun(arr,i+1,j,checked)
        fun(arr,i,j+1,checked)
        fun(arr,i-1,j,checked)
        fun(arr,i,j-1,checked)
        return checked
    elif x == 0:
        return 0
    
if __name__ == '__main__':
    
    arr = [[1, 1, 1, 1, 1, 1],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 0, 1, 1, 1],
           [0, 1, 1, 1, 1, 1],
           [1, 1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0]]
    
    groups = []
    checked = []
    for i in range(6):
        for j in range(6):
            if arr[i][j] == 1 and (i,j) not in checked:
                temp = fun(arr,i,j,[])
                groups.append(len(temp))
                checked += temp
                
    print(groups)