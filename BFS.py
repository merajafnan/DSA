
from queue import Queue

adj_list ={
    'A':['B','D'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E','F'],
    'E':['D','F','G'],
    'F':['D','E','H'],
    'G':['E','H'],
    'H':['G','F']
}

visited = {}
level = {}
parent = {}
bfs_traversal = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    level[node] = -1
    parent[node] = None

print('Visited: {}\nLevel: {}\nParent: {}'.format(visited,level,parent))

root = 'A'
visited[root] = True
level[root] = 0
queue.put(root)

while not queue.empty():
    node_q = queue.get()
    bfs_traversal.append(node_q)

    for item in adj_list[node_q]: #item = 'B','D'
        if not visited[item]:
            visited[item] = True
            parent[item] = node_q
            level[item] = level[node_q]+1
            queue.put(item)
print('\nAfter BFS:-- \nVisited: {}\nLevel: {}\nParent: {}\nBFS_Traversal: {}'.format(visited,level,parent,bfs_traversal))

# Shortest path from node

item = 'H'
path = []

while item is not None:
    path.append(item)
    item = parent[item]
path.reverse()
print(path)



