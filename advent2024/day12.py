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
seen = set()


# visited[0,0] = 1

regions:dict[int,list] = {}#{0:[0,0]} # dict of regions with values being list of [area, perimeter] and key being a unique plot identifier

# Define the search values (all directions including diagonally BUG NO! not diagonally)
# values = np.array([0, 1, -1]) 

# Generate all possible pairs. This is an 8 by 2 array of all search directions 
# visit_directions = np.array(np.meshgrid(values, values)).T.reshape(-1, 2)[1:] # we don't want the 0,0 pair so exclude the first one

visit_directions = np.array([[0,1],[0,-1],[1,0],[-1,0]])

# print(f"{visit_directions=}")

queue = deque()

queue.append(np.array([0,0]))

plot_id = -1


def explore(plot_id:int, pos:np.ndarray) -> None:
    # print(f"{plot_id=}")
    if visited[*pos]==1:
        return plot_id
    visited[*pos] = 1
    # print(visited)
    to_visit = pos + visit_directions
    # filter to keep only in bounds locations
    in_bounds_idx = (to_visit[:,0]>=0) & (to_visit[:,0]<puzzle.shape[0])\
                   &(to_visit[:,1]>=0) & (to_visit[:,1]<puzzle.shape[1])
    to_visit = to_visit[in_bounds_idx]
    values_at_indices = puzzle[to_visit[:,0], to_visit[:,1]]

    # Create a boolean mask for priority (same value as current position)
    priority_mask = values_at_indices == puzzle[*pos]
    visit_first = to_visit[priority_mask]

    if visit_first.size == 0 or np.all(visited[visit_first[:,0], visit_first[:,1]] == 0):
        plot_id += 1
        regions[plot_id] = [0,0]

    regions[plot_id][0]+=1 # add 1 to area
    regions[plot_id][1]-=len(visit_first) # when going to the same plant, remove 2 from perimeter since all plots start surrounded by 4 walls
    # print(F"{plot_id=}, {regions=}")
    # print(f"{plot_id=}")
    # print(f"{visit_first=}")
    visit_later = to_visit[~priority_mask]
    # visit_first = to_visit[puzzle[to_visit[:,0], to_visit[:,1]]==puzzle[*pos]] # visit the same plot first->depth first search
    to_visit = np.vstack((visit_first, visit_later))
    # print(f"{to_visit=}")

    # print(f"{visit_first=}") 
    for loc in to_visit:
        if visited[*loc] == 1:
            continue
        # if tuple(loc) in seen:
        #     continue
        if puzzle[*loc] == puzzle[*pos]:
            queue.appendleft(loc)
        else:
            queue.append(loc)
        # seen.add(tuple(loc))
    return plot_id
        

while np.any(visited==0):
    loc = queue.popleft()
    if visited[*loc] == 1:
        continue
    plot_id = explore(plot_id, loc)

price = 0
for key in regions:
    regions[key][1]+=4*regions[key][0]
    price += regions[key][0]*regions[key][1]

# print(regions)

print(f"Part 1 answer = {price}")


############ ANIMATE ###############

# import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
# im = ax.imshow(visited, cmap='gray', interpolation='nearest') .
# im = ax.imshow(visited, cmap='gray', vmin=0, vmax=1)
im = ax.imshow(visited, cmap='viridis', vmin=puzzle.min()-10, vmax=puzzle.max())

# im = ax.imshow(visited)

current_plant = puzzle[0,0]
plot_id = 0
visited = np.zeros_like(puzzle)
queue = deque()
queue.append(np.array([0,0]))


def update(frame):
    global current_plant
    global plot_id
    # Update your visited array here
    # ...
    if np.any(visited==0):
        loc = queue.popleft()
        if visited[*loc] == 1:
            update(frame)
        plot_id = explore(plot_id, loc)

    masked_puzzle = puzzle * visited

    im.set_array(masked_puzzle)

    return [im]

ani = FuncAnimation(fig, update, frames=200, interval=0, blit=True)
plt.show()

