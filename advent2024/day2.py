import numpy as np

def get_data():
    with open('day2.txt', 'r') as info:
        info = info.read()
        # Split the content into lines
        lines = info.strip().split("\n")
        data = []

        # return list(lines)

        # Process each line
        for line in lines:
            # Split each line into two numbers
            data.append(np.asarray(list(map(int, line.split()))))
            
        return data


# info is a list of np arrays of reports
reports = get_data()
safe = 0

for report in reports:
    # report eg 2 4 6 9 10 9
    diff = np.diff(report)
    if not (np.all(diff<0) or np.all(diff>0)):
        # print(report, diff)
        continue #report unsafe
    if np.any(diff>3) or np.any(diff<-3):
        # print(report, diff)
        continue #report unsafe)
    # print(report, diff)
    safe+=1

print(f"{safe=}")

############## PART 2 ##############


def is_safe(report:np.ndarray)->bool:
    # report eg 2 4 6 9 10 9
    diff = np.diff(report)
    if not (np.all(diff<0) or np.all(diff>0)):
        # print(report, diff)
        return False
    if np.any(diff>3) or np.any(diff<-3):
        # print(report, diff)
        return False #report unsafe)
    # print(report, diff)
    return True

safe = 0
for report in reports:
    if is_safe(report):
        safe+=1
    else:
        for i in range(0, len(report)):
            if is_safe(np.delete(report, i)):
                safe+=1
                break
print(f"{safe=}")

