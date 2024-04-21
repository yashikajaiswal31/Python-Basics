from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]
 
 
def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True
     
    while pq.empty() == False:
        u = pq.get()[1]
        print(u, end=" ")
        if u == target:
            break
 
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
def display_graph(graph):
    for i, adj_list in enumerate(graph):
        print("Node", i, ":", adj_list)
addedge(0, 1, 2)
addedge(0, 2, 4)
addedge(0, 3, 4)
addedge(1, 4, 8)
addedge(1, 5, 7)
addedge(2, 6, 3)
addedge(2, 7, 5)
addedge(3, 8, 12)
addedge(8, 9, 15)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
print("Visualization is given below:")
display_graph(graph)
source = 0
target = 9
print("After Best first search we get:")
best_first_search(source, target, v)