
urlFile = './aocTest/day3/task.txt'

with open(urlFile,'r') as file:
    inputs = [x.strip() for x in file]


n = len(inputs)
l = len(inputs[0])

sum = 0
j = 0
while(j < l and n > 1):
    sum = 0
    i = 0
    while(i < n):
        if(int(inputs[i][j]) == 1):
                sum += 1
        i+=1
    most = int(sum/n >= 0.5)

    r = 0
    while(n > 0 and r < n):
        if(int(inputs[r][j]) != most):
            inputs.pop(r)
            n-=1
        else:
            r+=1 
    j+=1

print(inputs)
result1 = int('0b'+inputs[0], base=2)

with open(urlFile,'r') as file:
    inputs = [x.strip() for x in file]

n = len(inputs)
l = len(inputs[0])

sum = 0
j = 0
while(j < l and n > 1):
    sum = 0
    i = 0
    while(i < n):
        if(int(inputs[i][j]) == 1):
                sum += 1
        i+=1
    most = int(sum/n >= 0.5)
    r = 0
    while(n > 0 and r < n):
        if(int(inputs[r][j]) == most):
            inputs.pop(r)
            n-=1
        else:
            r+=1 
    j+=1

print(inputs)
result2 = int('0b'+inputs[0], base=2)

print(result1,result2)
life_support = result1*result2
print(life_support)