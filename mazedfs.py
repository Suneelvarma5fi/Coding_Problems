
maze = [['0', '1', '0', '1', '1', '1', '0', '1'],
        ['1', '1', '0', '1', '1', '0', '0', '1'],
        ['1', '0', '0', '1', '0', '0', '1', '1'],
        ['1', '0', '0', '1', '1', '0', '1', '0'],
        ['1', '0', '0', '0', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '1', '0', '1', '1'],
        ['0', '1', '1', '1', '1', '1', '0', '1'],
        ['1', '1', '0', '0', '0', '1', '1', '1']]


visited = [[0 for i in range(8)] for i in range(8)]

def valid(maze,i,j,visited):
    if i>=0 and j>=0 and i<8 and j<8 and maze[i][j] == '1' and visited[i][j]==0:
        return 1
    else:
        return 0
    
    
def showpath(visited):
    for i in visited:
        print(i)
    return

def findingpath(maze,i,j,visited):

    if i == 0 and j == 7:
        visited[0][7] = 1
        print("There is path: ")
        showpath(visited)
        return True
    
    elif valid(maze,i,j,visited):
        visited[i][j] = 1
        if findingpath(maze,i+1,j,visited):#down
            visited[i][j] = 1
            return True
        if findingpath(maze,i,j-1,visited):#left
            visited[i][j] = 1
            return True
        if findingpath(maze,i,j+1,visited):#right
            visited[i][j] = 1
            return True
        if findingpath(maze,i-1,j,visited):#up
            visited[i][j] = 1
            return True
        visited[i][j] = 0
    else:
        return False
        