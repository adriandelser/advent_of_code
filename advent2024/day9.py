def get_data():
    with open('day9.txt','r') as f:
        data = f.read()
        return data
    
puzzle = get_data() + '0' # add a gap of length zero at the end


print(len(puzzle))

blocks = puzzle[::2]
# block_dict = {id:num for id, num in enumerate(blocks)}
# block_tuples = [(id,num) for id, num in enumerate(blocks)]
# block_list = [[i]*int(num) for i, num in enumerate(blocks)]
block_list = [str(i) for i, num in enumerate(blocks) for _ in range(int(num))]

gaps = puzzle[1::2]
num_gaps = sum([int(i) for i in gaps])
print(f"{num_gaps=}")

s = []
i=0
for block, gap in zip(blocks,gaps):
    # print(block, gap)
    s.extend([str(i)]*int(block) + ['.']*int(gap))
    i+=1

print(f"{s.count('.')=}")
# print(f"\n{block_list=}")
# print(f"\n{s=}")
s_copy = s.copy()
for idx, char in enumerate(s_copy):
    if char == '.':
        replacement = block_list.pop()
        # print(replacement)
        s[idx] = replacement

s[-num_gaps:] = ['0' for _ in range(num_gaps)]

print(f"\n{s[:100]=}")

checksum = 0
for idx, num in enumerate(s):
    checksum+=idx*int(num)

print(f"Part 1 answer = {checksum}")


#################### PART 2 ##########################
print(f"#################### PART 2 ##########################")
import numpy as np
gaps_np = np.array([int(gap) for gap in gaps])
puzzle_np = np.array([int(i) for i in puzzle])
s = s_copy.copy()
modifiable_puzzle = np.array([int(num) for num in puzzle])
ids = [i for i, _ in enumerate(blocks)][::-1]
# print(f"{ids=}")

print(f"{len(s_copy)=}")
print(f"{len(puzzle_np)=}")

block_counter = 0
for id, block in zip(ids,blocks[::-1]):
    # we need a idx for when the block starts
    block_start_idx = np.sum(puzzle_np[:-(2*block_counter+2)])
    print(f"{block_start_idx=}")
    block = int(block)
    # go through block lengths backwards
    # print(f"{block=}")
    # print(f"{gaps_np>=block=}")
    print(f"{id=}, {block=}")
    # Check if there is at least one True
    if not np.any(gaps_np>=block):
        # raise ValueError("No True values in the array.")
        block_counter+=1
        continue
    compatible_gap = np.argmax(gaps_np>=block) #first instance big enough to hold the block
    print(f"{compatible_gap=}")
    # now find the index where this gap starts. use a modified puzzle input for this
    gap_start = np.sum(modifiable_puzzle[:2*compatible_gap+1]) #its index in the full string of modified puzzle input
    if gap_start>block_start_idx:
        block_counter+=1
        continue
        # break # done
    print(f"{gap_start=}")
    s_copy[gap_start:gap_start+block] = [str(id)]*block # replace gaps with id
    s_copy[block_start_idx:block_start_idx+block] = ['.']*block # replace id with gap
    gaps_np[compatible_gap] -= block # reduce available space
    print(f"{modifiable_puzzle[:10]=}")
    print(f"{2*compatible_gap+1=}")
    modifiable_puzzle[2*compatible_gap+1] -= block # reduce gap space in full puzzle
    modifiable_puzzle[2*compatible_gap] += block # increase non gap space just before the gap
    block_counter+=1
    # break

checksum = sum([idx*int(num) for idx,num in enumerate(s_copy) if num!='.'])

print(f"Part 2 answer = {checksum}\n")
print(f"{s_copy[:20]=}\n")
print(f"{block_list[:20]=}")
print(f"{blocks[:10]=}")
print(f"{gaps[:5]=}")
print(f"{gaps_np[:5]=}")
print(f"{modifiable_puzzle[:10]=}")
print(f"{puzzle[:10]=}")

print(np.argmax([0,0,1]))
# print(puzzle[:10])


# for i in range(0):
#     print("asdf")

# File path
file_path = "day9part2output.txt"

# Save to file
with open(file_path, "w") as file:
    file.write(" ".join(s_copy))  # Join strings with a space as the separator


print([0,1,2,3,4][:-2])