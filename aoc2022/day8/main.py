import numpy as np

with open('./aoc2022/day8/task.txt','r') as file:
    inputs = [x.strip() for x in file]


#make an np array
toGrid = []
for input in inputs:
    curr = list(input)
    curr = [int(c) for c in curr]
    toGrid.append(curr)

grid = np.array(toGrid)

height, width = grid.shape

count = 4*(height -1)
#print(height,width)
#print(grid)

for i in range(1,height-1):
    visible = False
    for j in range(1,width-1):
        observe = grid[i][j]
        left = grid[i][:j]
        right = grid[i][j+1:]
        grid = np.transpose(grid)
        top = grid[j][:i]
        bottom = grid[j][i+1:]
        grid = np.transpose(grid) 


        lM = np.max(left)
        bM = np.max(bottom)
        tM = np.max(top)
        rM = np.max(right)
        
        test = np.array([lM,bM,tM,rM]) - observe
        #print(observe,"|",test)
        min = np.min(test)
        if min < 0:
            count+=1

print(count)

#part 2

scenic = 0

for i in range(1,height-1):
    for j in range(1,width-1):
        observe = grid[i][j]
        countleft = 0
        countbottom = 0
        counttop = 0
        countright = 0
        #left
        k=1
        while (k <= j):
            if(grid[i][j-k] < observe):
                countleft+=1
            elif(grid[i][j-k] >= observe):
                countleft+=1
                break
            k+=1
        #bottom
        k=1
        while (k < height-i):
            if(grid[i+k][j] < observe):
                countbottom+=1
            elif(grid[i+k][j] >= observe):
                countbottom+=1
                break
            k+=1
        #top
        k=1
        while(k <= i):
            if(grid[i-k][j] < observe):
                counttop+=1
            elif(grid[i-k][j] >= observe):
                counttop+=1
                break
            k+=1
        #right
        k=1
        while(k < height-j):
            if(grid[i][j+k] < observe):
                countright+=1
            elif(grid[i][j+k] >= observe):
                countright+=1
                break
            k+=1
        
        newscenic = countleft * countbottom * counttop * countright
        if (newscenic > scenic):
            scenic = newscenic
print(scenic)