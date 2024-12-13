import sys

with open("input.txt") as f:
    lines = f.readlines()

print(lines[0])

sum = 0 
for line in lines:
    digits = []
    for char in line:
        # print(char)
        if char.isnumeric():
            digits.append(char)
            # print(char, "isnumeric")
    code:int = int(digits[0]+digits[-1])
    # print(code)
    sum+=code
print(sum)

