import os

print(os.getcwd())

with open('./aocTest/day3/input.txt','r') as file:
    inputs = [x.strip() for x in file]

n = len(inputs)
l = len(inputs[0])

pos_count = []
for j in range(l):
    pos_count.append(0)

for i in range(n):    
    for j in range(l):
        if(int(inputs[i][j]) == 1):
            pos_count[j] += 1

gamma_b_count = [int((e/n)>=0.5) for e in pos_count]
epsilon_b_count = [1-e for e in gamma_b_count]
print(gamma_b_count)
print(epsilon_b_count)

s = '0b'
for e in gamma_b_count:
    s += str(e)
s2 = '0b'
for e in epsilon_b_count:
    s2 += str(e)

a,b = (int(s,base=2),int(s2,base=2))
power_consumption = (a*b)
print(power_consumption)

oxygen = 0
co2 = 0