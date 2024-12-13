from collections import defaultdict, deque


def get_data():
    with open('day5.txt','r') as f:
        # split the input into two by double new line character
        rules, updates = f.read().split('\n\n')
        rules = rules.split('\n')
        updates = updates.split('\n')
        updates = [page.split(',') for page in updates]
        # pages = [[int(num) for num in page] for page in pages]
        return rules, updates
    
rules,updates = get_data()

# print(rules, updates)

# set up a rules dictionary

rules_dict = defaultdict(set)

for rule in rules:
    rule = rule.split('|')
    left, right = rule[0], rule[1]
    if left not in rules_dict:
        rules_dict[left] = {right}
    else:
        rules_dict[left].add(right)

s = 0
incorrect_updates = []
for idx_update, update in enumerate(updates):
    legal = True
    for idx0, page in enumerate(update[::-1][:-1]):
        # reverse the update 
        for idx1, page1 in enumerate(update[::-1][idx0+1:]):
            if page in rules_dict:
                if page1 in rules_dict[page]:
                    #rule violated
                    legal = False
                    # print(idx_update, page0, page1)
                    # break
    if legal:
        length = len(update)
        middle_number = update[length//2]
        s+=int(middle_number)
    else:    
        incorrect_updates.append(update)
            

print(f"Answer Part 1 = {s}")


######################## PART 2 ########################

# This is a topological sort. We can use Kahn's algorithm


print(f"Number of incorrectly ordered updates = {len(incorrect_updates)}")



# create empty deque

# print(in_degree)
s = 0
for update in incorrect_updates:
    corrected = []
    q = deque()
    print(f"{update=}")
    update_set = set(update)
    new_rules_dict = defaultdict(set)
    # keep only the rules that have the numbers in the current update
    for page in update:
        new_rules_dict[page] = update_set.intersection(rules_dict[page]) 
        

    in_degree = defaultdict(int)
    for before, afters  in new_rules_dict.items():
        for after in afters:
            in_degree[after] += 1
        
    for page in update:
        # print(page, type(page),in_degree[page])
        if in_degree[page] == 0:
            q.append(page)
            in_degree[page] -=1

    # print(len(q), q)
    while q:
        page = q.popleft()
        corrected.append(page)
        for other_page in new_rules_dict[page]:
            in_degree[other_page]-=1
        # print(in_degree)
        
        for page in update:
            if in_degree[page] == 0:
                q.append(page)
                in_degree[page] -=1

    print(corrected)
    middle_number = corrected[len(corrected)//2]
    s+=int(middle_number)

print(f"Part 2 answer = {s}")
            

            
            

    