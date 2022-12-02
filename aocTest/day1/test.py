

with open('aocTest/input.txt','r') as file:
    inputs = [int(x) for x in file]


count = 0

for i in range(len(inputs)):
    if i>=3 and (inputs[i] > inputs[i-3]):
        count+=1

print(count)
