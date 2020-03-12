
def valid(arr,i,j,checked):
    if i<0 or j<0 or (i,j) in checked:
        return 0
    else:
        try:
            x = arr[i][j]
        except IndexError:
            return 0
        else:
            return x
        
def adjcheck(word,i,j,arr,checked):
    x = valid(arr,i,j,checked)
    if x in word and (i,j) not in checked:

        checked.append((i,j))
        word.remove(x)
        adjcheck(word,i+1,j,arr,checked)
        adjcheck(word,i,j+1,arr,checked)
        adjcheck(word,i-1,j,arr,checked)
        adjcheck(word,i,j-1,arr,checked)
        adjcheck(word,i+1,j+1,arr,checked)
        adjcheck(word,i-1,j-1,arr,checked)
        adjcheck(word,i-1,j+1,arr,checked)
        adjcheck(word,i+1,j-1,arr,checked)
        if word == []:
            return word,checked
        return word,
    
    
def eachword(word,m,n,arr,checked):
    now = list(word)
    for i in range(m):
        for j in range(n):
            curr = valid(arr,i,j,[])
            if curr and curr in now:
                final = adjcheck(now,i,j,arr,[])
                #print(final)
                if final[0] != []:
                    return False
                else:
                    return word,final[1]
                
def checkpresence(word,arr,m,n):
    l = list(word)
    for i in range(m):
        for j in range(n):
            if arr[i][j] in l:
                l.remove(arr[i][j])
    if l == []:
        return True
    else:
        return False
                
if __name__ == '__main__':
#    word = ['GEEKS','FOR','QUIZ','GO']
#
#    arr = [['G','I','Z'],
#           ['U','E','K'],
#           ['Q','S','E']]
    
    t = int(input())
    arr = []
    tmp = []
    for i in range(t):
        wordscount = int(input())
        words = input().strip().split()
        m,n = tuple(map(int,input().split()))
        lis = input().split()
        x = 0
        for i in range(m):
            for j in range(n):
                tmp.append(lis[x])
                x += 1
            arr.append(tmp)
            tmp = []

        
        output = []
        checked  = []
        
    
        for word in words:
            if checkpresence(word,arr,m,n):
                
                x = eachword(word,m,n,arr,checked)
                if x:
                    output.append(x[0])
                    checked += x[1]


        if output == []:
            print(-1)                
        else:
            #output= sorted(output,key = lambda x :len(x),reverse = True)
            print(*output)