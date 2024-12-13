#%%
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

def get_data():
    with open('day8.txt','r') as f:
        data = f.read().splitlines()
    data_np = np.array([[ord(char) for char in row] for row in data])
    data_np[data_np==ord('.')] = 0 # convert vacant locations to 0
    return data_np

puzzle = get_data()

antennae = np.unique(puzzle)[1:] #remove the first one as it is zero
# print(f"Unique antenae are {antennae}")

all_pairs = np.empty((0,2,2))
for num in antennae:
    locations = np.argwhere(puzzle==num)
    pairs = combinations(locations, 2)
    pairs = np.array(list(pairs))
    # print(pairs, pairs.shape)
    all_pairs = np.vstack((all_pairs,pairs))
    # print(diff)
    # for pair in pairs:
    #     print(num, pair)
diff = all_pairs[:,1,:]-all_pairs[:,0,:]
# print(f"{all_pairs.shape=}")
# print(f"{diff[:,None,:].shape=}")

#add these vectors to the second of each pair:
potential_antinodes = all_pairs[:,1,:]+diff
# print(f"{all_pairs[:,1,:].shape=},{potential_antinodes.shape=}")
potential_antinodes = np.vstack((
    potential_antinodes, all_pairs[:,0,:]-diff))
# print(f"{potential_antinodes.shape=}")
unique = np.unique(potential_antinodes,axis=0)
# print(f"{unique.shape=}")

n_rows, n_cols = puzzle.shape[0], puzzle.shape[1]

antinodes = unique[
    ((unique[:,0]>=0) & (unique[:,0]<n_rows)) &
    ((unique[:,1]>=0) & (unique[:,1]<n_cols))
]

# print(antinodes.shape)

n_antinodes = antinodes.shape[0]
print(f"Part 1 answer is {n_antinodes}")

# plt.imshow(puzzle)
# plt.show()
################### PART 2 ###############################



# %%

antennae = np.unique(puzzle)[1:] #remove the first one as it is zero
# print(f"Unique antenae are {antennae}")

# we already have all pairs from part 1
diff = all_pairs[:,1,:]-all_pairs[:,0,:]
diff = diff.astype(np.int64)
# diff = np.array()
# now we want to reduce each diff pair to its simplest form
# print(diff, diff.shape)
gcds = np.gcd(diff[:,0],diff[:,1])
# it seems like all gcds are 1 by design but we do it anyway for robustness
diff = diff // gcds[:, None]

#this for loop is overkill but it's fast enough for what we need
new_diff = diff.copy()
for i in range(-puzzle.shape[0],puzzle.shape[0]):
    new_diff = np.hstack((new_diff, i*diff))

new_diff = new_diff.reshape((diff.shape[0],-1,2))
# print(new_diff.shape)

diff = new_diff.copy()
#add these vectors to the second of each pair:

potential_antinodes = all_pairs[:,1,:][:,None,:] + diff
potential_antinodes = potential_antinodes.reshape(-1,2)
# print(potential_antinodes.shape)
# print(f"{all_pairs[:,1,:].shape=},{potential_antinodes.shape=}")
# potential_antinodes = np.vstack((
#     potential_antinodes, all_pairs[:,0,:]-diff))
# print(f"{potential_antinodes.shape=}")
unique = np.unique(potential_antinodes,axis=0)
# print(f"{unique.shape=}")

n_rows, n_cols = puzzle.shape[0], puzzle.shape[1]

antinodes = unique[
    ((unique[:,0]>=0) & (unique[:,0]<n_rows)) &
    ((unique[:,1]>=0) & (unique[:,1]<n_cols))
]

# print(antinodes.shape)

n_antinodes = antinodes.shape[0]
print(f"Part 2 answer is {n_antinodes}")
# %%
