import heapq

graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':['F'],
'F':[]
}

heuristic={
'A':5,
'B':4,
'C':3,
'D':2,
'E':1,
'F':0
}

pq=[(heuristic['A'],'A')]
visited=set()

while pq:
    h,node=heapq.heappop(pq)

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            heapq.heappush(pq,(heuristic[neighbour],neighbour))
