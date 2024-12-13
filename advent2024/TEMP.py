#%%
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def get_data():
    with open('day12.txt', 'r') as f:
        data = f.read().splitlines()
    data = np.array([[ord(s) for s in line] for line in data])
    return data

puzzle = get_data()

# print(puzzle)

# uncomment two lines below to see the map of the plots
# plt.imshow(puzzle)
# plt.show()

# let's search in all directions. When an adjacent search space is different to the current one, we can start a new search while adding 
# to the perimeter of both areas and stopping the search of the previous area.
# we also keep a visited set to ensure we don't count any pixel twice.
# NOTE Ah! The search should be depth first along each unique plot id otherwise there will be 
# issues with grouping plots of the same crop but on a different 'island'

# create a generator to get unique ids
# def unique_number_generator(start=0):
#     current = start
#     while True:
#         yield current
#         current += 1

# gen = unique_number_generator(start=0)

visited = np.zeros_like(puzzle) # could use set as well

# visited[0,0] = 1

regions:dict[int,list] = {0:[0,0]} # dict of regions with values being list of [area, perimeter] and key being a unique plot identifier

# Define the search values (all directions including diagonally BUG NO! not diagonally)
# values = np.array([0, 1, -1]) 

# Generate all possible pairs. This is an 8 by 2 array of all search directions 
# visit_directions = np.array(np.meshgrid(values, values)).T.reshape(-1, 2)[1:] # we don't want the 0,0 pair so exclude the first one

visit_directions = np.array([[0,1],[0,-1],[1,0],[-1,0]])

# print(f"{visit_directions=}")

queue = deque()

queue.append(np.array([0,0]))

def explore(plot_id:int, pos:np.ndarray) -> None:
    visited[*pos] = 1
    # print(visited)
    to_visit = pos + visit_directions
    in_bounds_idx = (to_visit[:,0]>=0) & (to_visit[:,0]<puzzle.shape[0])\
                   &(to_visit[:,1]>=0) & (to_visit[:,1]<puzzle.shape[1])
    # either all 4 are valid ie we are inside the puzzle
    # or 3 are valid because we are on an edge but not a corner
    # or 2 are valid because we are on a corner
    # add to the perimeter based on the above:
    # if 
    # plot_id = next(gen)
    # regions[plot_id] = [0,1] # add 1 to perimeter for being on a plot boundary
    # explore(plot_id, loc)
    # num_in_bounds = len(in_bounds_idx[in_bounds_idx==True])
    # if num_in_bounds == 2:
    #     regions[plot_id][1]+=2 # being on a corner adds 2 to perimeter
    # elif num_in_bounds == 3:
    #     regions[plot_id][1]+=1 # being on an edge adds 1 to perimeter
    regions[plot_id][0]+=1 # add 1 to area
    
    # filter to keep only in bounds locations
    to_visit = to_visit[in_bounds_idx]
    # filter to ignore visited ones
    # to_visit = to_visit[visited[to_visit[:,0], to_visit[:,1]]==0]
    # now set them to visited
    # visited[to_visit[:,0], to_visit[:,1]] = 1 

    values_at_indices = puzzle[to_visit[:,0], to_visit[:,1]]
    # Create a boolean mask for priority (same value as current position)
    priority_mask = values_at_indices == puzzle[*pos]
    visit_first = to_visit[priority_mask]
    regions[plot_id][1]-=len(visit_first) # when going to the same plant, remove 2 from perimeter since all plots start surrounded by 4 walls
    # print(f"{plot_id=}")
    # print(f"{visit_first=}")
    visit_later = to_visit[~priority_mask]
    # visit_first = to_visit[puzzle[to_visit[:,0], to_visit[:,1]]==puzzle[*pos]] # visit the same plot first->depth first search
    to_visit = np.vstack((visit_first, visit_later))
    # print(f"{to_visit=}")

    # print(f"{visit_first=}") 
    for idx, loc, in enumerate(to_visit):
        if visited[*loc] == 1:
            continue
        if puzzle[*loc] == puzzle[*pos]:
            # same type of crop, no special treatment
            # print(f'same crop')
            # print(f"{loc=}")
            # explore(plot_id, loc)
            queue.appendleft(loc)
            # return
            continue
        queue.append(loc)
        

# print(visited)

current_plant = puzzle[0,0]
plot_id = 0
while np.any(visited==0):
    loc = queue.popleft()
    if visited[*loc] == 1:
        continue
    plant = puzzle[*loc]
    if plant == current_plant:
        # same plot
        
        explore(plot_id, loc)
    else:
        current_plant = plant
        plot_id+=1
        regions[plot_id] = [0,0]
        explore(plot_id, loc)


price = 0
for key in regions:
    regions[key][1]+=4*regions[key][0]
    price += regions[key][0]*regions[key][1]

print(regions)

print(f"Part 1 answer = {price}")

from scipy.ndimage import label


unique_vals = np.unique(puzzle)
regions = 0
for val in unique_vals:
    # Create a mask for this specific value
    mask = (puzzle == val)
    # Label connected components of this value
    _, n = label(mask)
    # print(ord('B'))
    print(val,n)
    regions += n

print("Number of regions:", regions)

############ ANIMATE ###############
# plt.imshow(puzzle)
# plt.show()
# %%

