def get_data():
    with open('day7.txt','r') as f:
        data = f.read().splitlines()
        print(len(data))
        # data = {result:numbers for row in data[:2] for result, numbers in row.split(':')} # this results in unpacking errors, see below
        data = [(int(desired.strip()), [int(num) for num in numbers.strip().split(' ')]) for row in data for desired, numbers in [row.split(':')]]
    return data

puzzle = get_data()
print(len(puzzle))

# print(puzzle)


from itertools import product

# Define operators
operators = ['+', '*']

# Generate all combinations of operators (len(integers) - 1 slots for operators)

s = 0

# p = {6}
for desired, numbers in puzzle:
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    for operator_combo in operator_combinations:
        output = numbers[0]
        for idx, num in enumerate(numbers[1:]):
            if operator_combo[idx] == '+':
                output+=num
            else:
                output*=num
        if output == desired:
            s+=desired
            break


print(f"Part 1 answer = {s}")

#################### PART 2 #########################

# Define operators
operators = ['+', '*', '||']

# Generate all combinations of operators (len(integers) - 1 slots for operators)

s = 0

# p = {6}
for idx, (desired, numbers) in enumerate(puzzle):
    print(f"we have reached {idx}/850")
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    for operator_combo in operator_combinations:
        output = numbers[0]
        for idx, num in enumerate(numbers[1:]):
            op = operator_combo[idx]
            if op == '+':
                output+=num
            elif op == '*':
                output*=num
            else:
                output = int(str(output)+str(num))
        if output == desired:
            s+=desired
            break


print(f"Part 2 answer = {s}")