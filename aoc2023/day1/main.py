import os
print(os.getcwd())

with open('./day1/input.txt','r') as file:
    inputs = [x.strip() for x in file]

numbers = '1234567890'
#part 1
'''

nums = []
for calib in inputs:

    digits = [ x for x in calib if x in numbers ] 

    first_last = digits[0] + digits[-1]
    val = int(first_last)

    nums.append(val)

print('Part 1: ',sum(nums))
'''

#part 2

k_numbers = {'zero': 0,
             'one': 1,
             'two': 2,
             'three': 3,
             'four': 4,
             'five': 5,
             'six': 6,
             'seven': 7,
             'eight': 8,
             'nine': 9}

nums = []
for calib in inputs:

    digits = []
    letters = ''
    for x in calib:
        if x not in numbers:
            letters += x
            letters = letters.lower()
            for key in  k_numbers.keys():
                idx = letters.find(key)
                if idx != -1:
                    letters = letters[idx:]
                if key in letters:
                    digits.append(k_numbers[key])
                    letters = letters[len(key)-1:]
        else:
            digits.append(x)
            letters = ''     
    
    first_last = str(digits[0]) + str(digits[-1])
    val = int(first_last)

    nums.append(val)

print('Part 2: ',sum(nums))