import numpy as np
from typing import Iterable

def get_data():
    with open('day10.txt','r') as f:
        data = f.read().splitlines()
        data = np.array([[int(i) for i in line] for line in data])
    return data

puzzle = get_data()

# print(f"{puzzle=}")
print(f"{puzzle.shape=}")

# this seems like a dynamic programming problem

def solution(puzzle:np.ndarray)->int:

    trailheads = 0
    zeros = np.argwhere(puzzle==0)

    

    def search(expected:int, position:np.ndarray, visited:set):
        nonlocal trailheads
        # Define offsets for neighbors: up, down, left, right
        offsets = np.array([[0, 1],  # up
                            [0, -1], # down
                            [-1, 0], # left
                            [1, 0]]) # right

        # Calculate neighbour positions
        neighbours = position + offsets
        # return
        in_bounds = (neighbours[:,0]>=0) & (neighbours[:,0]<puzzle.shape[0])\
        & (neighbours[:,1]>=0) & (neighbours[:,1]<puzzle.shape[0])

        neighbours = neighbours[in_bounds]

        # neighbour_vals = puzzle[puzzle[neighbours]==expected]
        # Get the values at the neighbor positions
        neighbour_vals = puzzle[neighbours[:, 0], neighbours[:, 1]]

        # Filter neighbor values to include only those that match the expected value
        matching_vals = neighbour_vals[neighbour_vals == expected]
        matching_neighbors = neighbours[neighbour_vals == expected]

        # print(f"{neighbours=}")
        # print(f"{expected=}")
        # print(f"{neighbour_vals=}")
        # print(f"{matching_vals=}")
        # print(f"{matching_neighbors=}\n")
        # print(f"{position=}, {puzzle[*position]=}")
        # print(f"{neighbours=}")
        # print(f"{expected=}")
        # print(f"{neighbour_vals=}")
        # print(f"{matching_vals=}")
        # print(f"{len(matching_vals)=}")
        # print(f"{matching_neighbors=}\n")

        if expected == 9:
            for matching in matching_neighbors:
                visited.add(tuple(matching))
            # trailheads=len(visited)
            return
        
        for pos in matching_neighbors:
            search(expected+1, pos, visited)

        # print(f"{visited=}")
        return len(visited)


        # neighbours = neighbours[puzzle[neighbours]==expected]

        # return
    

    for zero in zeros:
        visited = set()
        trailheads += search(1, zero, visited)
        # print(f"{n=}")
        # print()
        # break
    
    return trailheads

    
trailheads = solution(puzzle)

print(f"Part 1 answer = {trailheads}")


################ PART 2 #####################
def solution(puzzle:np.ndarray)->int:

    trailheads = 0

    

    def search(expected:int, position:np.ndarray):
        nonlocal trailheads
        # Define offsets for neighbors: up, down, left, right
        offsets = np.array([[0, 1],  # up
                            [0, -1], # down
                            [-1, 0], # left
                            [1, 0]]) # right

        # Calculate neighbour positions
        neighbours = position + offsets
        # return
        in_bounds = (neighbours[:,0]>=0) & (neighbours[:,0]<puzzle.shape[0])\
        & (neighbours[:,1]>=0) & (neighbours[:,1]<puzzle.shape[0])

        neighbours = neighbours[in_bounds]

        # neighbour_vals = puzzle[puzzle[neighbours]==expected]
        # Get the values at the neighbor positions
        neighbour_vals = puzzle[neighbours[:, 0], neighbours[:, 1]]

        # Filter neighbor values to include only those that match the expected value
        matching_vals = neighbour_vals[neighbour_vals == expected]
        matching_neighbors = neighbours[neighbour_vals == expected]

        if expected == 9:
            # for matching in matching_neighbors:
            #     visited.add(tuple(matching))
            trailheads+=len(matching_neighbors)
            return
        
        for pos in matching_neighbors:
            search(expected+1, pos)

        # print(f"{visited=}")
        return trailheads


        # neighbours = neighbours[puzzle[neighbours]==expected]

        # return
    
    zeros = np.argwhere(puzzle==0)
    for zero in zeros:
        search(1, zero)
        # print(f"{n=}")
        # print()
        # break
    
    return trailheads

# print(puzzle)
    
trailheads = solution(puzzle)

print(f"Part 2 answer = {trailheads}")
        

        
    


# zeros = np.argwhere(puzzle==0)

# in_bounds = (zeros[:,0]>=0)
# print(in_bounds)

# print(f"{zeros=}")

# print(puzzle[[4,4]])