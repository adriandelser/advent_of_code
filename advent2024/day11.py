import numpy as np

def get_data():
    with open('day11.txt', 'r') as f:
        data = f.read().split(' ')
        return data
    
puzzle = get_data()

explored = {}

def blink(input:list[str])->list[str]:
    output = []
    # return
    for s in input:
        if s in explored:
            output.extend(explored[s])
            continue
        if len(s)&1 == 0:
            # even length
            new_s = [str(int(s[:len(s)//2])),
                     str(int(s[len(s)//2:]))
                     ]
        elif s == '0':
            new_s = ['1']

        else:
            new_s = [str(2024*int(s))]
        
        output.extend(new_s)
        explored[s] = new_s

    return output

output = puzzle.copy()
for i in range(25):
    # print(f"{i=}")
    output = blink(output)

print(f"Part 1 answer = {len(output)}")

########## PART 2 ################

# We have to be smart here and keep a list as short as possible while removing duplicate items before each blink
# As a duplicate is removed, its score needs to transferred to the only equal number. ie if there are two fours, the second four
# is removed and its score is transferred to the first. 
# Each number starts with a score of one. if a duplicate is removed, the score of the remaining goes up by one (or the number of duplicates removed)
# order doesn't matter

from collections import defaultdict

input = puzzle.copy()
current = {num:puzzle.count(num) for num in puzzle}

def blink(input:dict[str,int])->dict[str,int]:
    output = defaultdict(int)
    # return
    for s in input:
        if len(s)&1 == 0:
            # even length
            new_s = [str(int(s[:len(s)//2])),
                     str(int(s[len(s)//2:]))
            ]
        elif s == '0':
            new_s = ['1']

        else:
            new_s = [str(2024*int(s))]
        
        for val in new_s:
            # print(f"{input[s]=} {type(input[s])=}")
            output[val]+=input[s]
        # explored[s] = new_s


    return output

print(f"{current=}")

for i in range(75):
    current = blink(current) # can be called with dictionary 

total_length = sum(current.values())
print(f"Part 2 answer = {total_length}")
    # print(current)
    # break



# d = defaultdict(int)

# d['1']+=10
# print(d['1'])