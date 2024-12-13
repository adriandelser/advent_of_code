import numpy as np

def get_data():
    with open('day6.txt','r') as f:
        data = f.read().split('\n')
        return data

obstacle_val = -5
data = get_data()
puzzle = np.array([[1 if char =='.' else obstacle_val if char=='#' else 2 for char in row] for row in data])
print(puzzle.shape)

start = np.where(puzzle==2)
print(f"{start=}")
# start = np.asarray(start).flatten()
print(puzzle[start])
row0, col0 = start[0][0], start[1][0]
print(data[row0][col0]) # returns '^' therefore we start pointing up the map

still_in = True
n_rot = 0
current_array = puzzle.copy()
n_row, n_col = puzzle.shape[0], puzzle.shape[1]

first_primes = [2,3,5,7]

while still_in:
    # print(f"{n_rot&1=}, {n_rot%2=}")
    obstacle_pos = np.where(current_array[:row0,col0]==obstacle_val)[0]
    if len(obstacle_pos) == 0:
        # exit the maze
        # current_array[:row0,col0] += n_rot%4
        current_array[:row0,col0] = 2
        still_in = False
        break
    # take the closest to us therefore max (if it exists)
    obstacle_idx = max(obstacle_pos)
    # current_array[obstacle_idx+1:row0,col0] += 1+n_rot%4
    current_array[obstacle_idx+1:row0,col0] = 2

    row0 = obstacle_idx+1
    # print(f"{row0=}")
    current_array = np.rot90(current_array)
    n_rot+=1
    
    row0, col0 = n_row-1-col0, row0
    # col0 = row0
    # print(f"{row0=}, {col0=}")
    # break

# flip array back for plotting:
current_array = np.rot90(current_array,k=-n_rot%4)
visited = np.count_nonzero(current_array==2)

print(f"Part 1 answer = {visited}")


# plot the path
import matplotlib.pyplot as plt
# current_array+=10
plt.imshow(current_array)
# plt.show()

##################### PART 2 #######################
guard_indices = np.where(current_array==2)
print(guard_indices)

n_loops = 0
for guard_row, guard_col in zip(*guard_indices):
    # iterate through where the original path went
    row0, col0 = start[0][0], start[1][0]

    # print(data[row0][col0]) # returns ^ therefore we start pointing up the map

    still_in = True
    n_rot = 0
    current_array = puzzle.copy()
    current_array[guard_row, guard_col] = obstacle_val

    n_row, n_col = puzzle.shape[0], puzzle.shape[1]

    first_primes = [2,3,5,7]

    while still_in:
        # print(f"{n_rot&1=}, {n_rot%2=}")
        obstacle_pos = np.where(current_array[:row0,col0]==obstacle_val)[0]
        if len(obstacle_pos) == 0:
            # exit the maze
            current_array[:row0,col0] *= first_primes[n_rot%4]
            # current_array[:row0,col0] = 2
            still_in = False
            break
        # take the closest to us therefore max (if it exists)
        obstacle_idx = max(obstacle_pos)
        # current_array[obstacle_idx+1:row0,col0] += 1+n_rot%4
        if np.any(current_array[obstacle_idx+1:row0,col0]==first_primes[n_rot%4]):
            # loop exists
            print("WE ARE IN A LOOP")
            n_loops += 1
            print(f"{n_loops=}")
            break
        current_array[obstacle_idx+1:row0,col0] *= first_primes[n_rot%4]

        row0 = obstacle_idx+1
        # print(f"{row0=}")
        current_array = np.rot90(current_array)
        n_rot+=1
        
        row0, col0 = n_row-1-col0, row0
        # col0 = row0
        # print(f"{row0=}, {col0=}")
        # break

    # flip array back for plotting:
    # current_array[guard_row, guard_col] = 1



# visited = np.count_nonzero(current_array==2)

print(f"Part 2 answer = {n_loops}")

current_array = np.rot90(current_array,k=-n_rot%4)

# plot the path
import matplotlib.pyplot as plt
# current_array+=10
plt.imshow(current_array)
plt.show()