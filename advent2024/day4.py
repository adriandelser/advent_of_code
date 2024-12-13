def get_data():
    with open('day4.txt','r') as f:
        data = f.read().splitlines()
        return data
    
input = get_data() #list of strings
# print(input)

# print(input[6][45])


def solution(puzzle:list[str])->int:
    count = 0
    # start = [0,0]
    # current = ''
    # visited = set()

    def dp(loc:list, current:str, next:list):
        '''location is current coords eg [3,6], current is current string eg X, XM, XMA. next is the direction to search eg [0,1] for right, [1,1] for diagonally up and right etc
        remember the first coord is the row, and the second is the column so it [y,x]'''

        if not 0<=loc[0]+next[0]<=len(puzzle)-1 or not 0<=loc[1]+next[1]<=len(puzzle[0])-1:
            return #out of bounds
        if current == 'X':
            expected = 'M'
        elif current == 'XM':
            expected = 'A'
        elif current == 'XMA':
            expected = 'S'

        next_loc = [loc[0]+next[0], loc[1]+next[1]]
        if puzzle[next_loc[0]][next_loc[1]] == expected:
            if expected == 'S':
                nonlocal count
                count += 1
            else:
                dp(next_loc, current+expected, next)
        

    for idx_y, row in enumerate(puzzle):
        for idx_x, char in enumerate(row):
            loc = [idx_y,idx_x]
            if char == 'X':
                dp(loc, 'X', [0,1]) #search right
                dp(loc, 'X', [0,-1]) #search left
                dp(loc, 'X', [1, 0]) #search down
                dp(loc, 'X', [-1, 0]) #search up
                dp(loc, 'X', [1, 1]) #search diagonally down and right
                dp(loc, 'X', [-1, -1]) #search diagonally up and left
                dp(loc, 'X', [1, -1]) #search diagonally down and left
                dp(loc, 'X', [-1, 1]) #search diagonally up and right


    return count
    

count = solution(input)

print(f"Part 1 solution = {count}")


########## PART 2 #############

def solution(puzzle:list[str])->int:
    count = 0
    # start = [0,0]
    # current = ''
    # visited = set()

    def dp(loc:list, current:str, next:list):
        '''location is current coords eg [3,6], current is current string eg X, XM, XMA. next is the direction to search eg [0,1] for right, [1,1] for diagonally up and right etc
        remember the first coord is the row, and the second is the column so it [y,x]'''

        if not 0<=loc[0]+next[0]<=len(puzzle)-1 or not 0<=loc[1]+next[1]<=len(puzzle[0])-1:
            return #out of bounds
        
        if current == 'M':
            expected = 'A'
        elif current == 'MA':
            expected = 'S'

        next_loc = [loc[0]+next[0], loc[1]+next[1]]
        if puzzle[next_loc[0]][next_loc[1]] == expected:
            if expected == 'S':
                nonlocal count
                count += 1
            else:
                # expected is A and we are on a central A
                if not 1<=next_loc[0]<=len(puzzle)-2 or not 1<=next_loc[1]<=len(puzzle[0])-2:
                    # the central A can not be on the edge of the puzzle
                    return
                if (next[0] > 0 and next[1] > 0) or (next[0] < 0 and next[1] < 0):
                    # we were searching along the y = -x line so check for m and s on the y=x line
                    other_diag = puzzle[next_loc[0]-1][next_loc[1]+1] + puzzle[next_loc[0]+1][next_loc[1]-1]
                elif (next[0] > 0 and next[1] < 0) or (next[0] < 0 and next[1] > 0):
                    # we were searching along the y = x line so check for m and s on the y=-x line
                    other_diag = puzzle[next_loc[0]-1][next_loc[1]-1] + puzzle[next_loc[0]+1][next_loc[1]+1]
                if 'M' in other_diag and 'S' in other_diag:
                    dp(next_loc, current+expected, next)
        

    for idx_y, row in enumerate(puzzle):
        for idx_x, char in enumerate(row):
            loc = [idx_y,idx_x]
            if char == 'M':
                dp(loc, 'M', [1, 1]) #search diagonally down and right
                dp(loc, 'M', [-1, -1]) #search diagonally up and left
                dp(loc, 'M', [1, -1]) #search diagonally down and left
                dp(loc, 'M', [-1, 1]) #search diagonally up and right

    # we are double counting all the crosses so need to divide by 2. 
    # Can make this more efficient but the solution is fast enough for this puzzle input
    return count/2 
    

count = solution(input)

print(f"Part 2 solution = {count}")