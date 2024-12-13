import heapq

def get_data():
    with open('info.txt', 'r') as info:
        info = info.read()
        # Split the content into lines
        lines = info.strip().split("\n")

        # Initialize two empty lists
        column1 = []
        column2 = []

        # Process each line
        for line in lines:
            # Split each line into two numbers
            num1, num2 = map(int, line.split())
            column1.append(num1)
            column2.append(num2)
    return column1, column2

# Print the two lists
# print("Column 1:", column1)
# print("\n\nColumn 2:", column2)
column1, column2 = get_data()

heap1 = heapq.heapify(column1)
heap2 = heapq.heapify(column2)

s = 0
while True:
    try:
        a = heapq.heappop(column1)
        b = heapq.heappop(column2)
    except IndexError:
        break  # Stop when the heap is empty
    s += abs(a-b)

print(s)


######## PART 2 #####################
column1, column2 = get_data()


occurences = {}
similarity = 0
for num in column1:
    # print(num)
    if num not in occurences:
        occurences[num] = column2.count(num)
    similarity += num * occurences[num]
    
print(f"{similarity=}")