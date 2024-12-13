import numpy as np
import re

def get_data():
    with open('day3.txt', 'r') as info:
        info = info.read() 
        return info
    
input = get_data() #string 

expression = r'mul\(\d+,\d+\)'

matches = re.findall(expression, input)
# print(matches,"\n")

s = 0
for match in re.finditer(r'mul\((\d+),(\d+)\)', input):
    a = int(match.group(1))
    b = int(match.group(2))
    s += a * b

print(f"Part 1 answer = {s}\n")

    # print(f"Function: {match.group(0)}, Arg1: {match.group(1)}, Arg2: {match.group(2)}")



########################## PART 2 ###################################


expression2 = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"

matches = re.findall(expression2, input)

# print(matches)

do = True
s = 0

for match in re.finditer(r"don't\(\)|do\(\)|mul\((\d+),(\d+)\)", input):
    if match.group(0) == "don't()":
        # print("don't")
        do = False
    elif match.group(0) == "do()":
        # print("do")
        do = True
    else:
        a = int(match.group(1))
        b = int(match.group(2))
        # print(f"{a} * {b} = {a * b}")
        s += a*b if do else 0

print(f"Part 2 answer = {s}")