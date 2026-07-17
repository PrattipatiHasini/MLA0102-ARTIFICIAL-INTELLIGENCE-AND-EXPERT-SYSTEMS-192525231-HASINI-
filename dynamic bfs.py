from collections import deque

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    graph[vertex] = []

e = int(input("Enter number of edges: "))

print("Enter edges (source destination):")
for i in range(e):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)   # Remove this line for directed graph

start = input("Enter starting vertex: ")

visited = set()
queue = deque()

visited.add(start)
queue.append(start)

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
