from collections import deque

capacity = (11,9)
goal = 8

visited = set()
queue = deque([((0,0),[])])

while queue:
    (a,b),path = queue.popleft()

    if a==goal or b==goal:
        print("Solution:")
        print(path+[(a,b)])
        break

    if (a,b) in visited:
        continue

    visited.add((a,b))

    states = []

    states.append((11,b))
    states.append((a,9))
    states.append((0,b))
    states.append((a,0))

    transfer=min(a,9-b)
    states.append((a-transfer,b+transfer))

    transfer=min(b,11-a)
    states.append((a+transfer,b-transfer))

    for s in states:
        queue.append((s,path+[(a,b)]))
