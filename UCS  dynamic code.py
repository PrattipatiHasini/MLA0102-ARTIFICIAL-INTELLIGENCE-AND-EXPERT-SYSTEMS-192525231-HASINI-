import heapq

graph = {
    'A':[('B',2),('C',4)],
    'B':[('D',3),('E',1)],
    'C':[('F',5)],
    'D':[],
    'E':[('F',2)],
    'F':[]
}

pq = [(0,'A')]
visited = set()

while pq:
    cost,node = heapq.heappop(pq)

    if node not in visited:
        print(node,cost)
        visited.add(node)

        for neighbour,w in graph[node]:
            heapq.heappush(pq,(cost+w,neighbour))
