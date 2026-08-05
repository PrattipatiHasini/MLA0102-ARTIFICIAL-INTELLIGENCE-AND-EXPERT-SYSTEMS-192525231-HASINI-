from collections import deque

maze = [
    [0,0,1,0],
    [1,0,1,0],
    [0,0,0,0],
    [0,1,1,0]
]

start = (0,0)
goal = (3,3)

rows = len(maze)
cols = len(maze[0])

queue = deque([(start,0)])
visited = set()

while queue:
    (x,y),steps = queue.popleft()

    if (x,y)==goal:
        print("Shortest Path Steps =",steps)
        break

    if (x,y) in visited:
        continue

    visited.add((x,y))

    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==0:
            queue.append(((nx,ny),steps+1))
