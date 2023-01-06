
adj_list = [[1,3], [0], [3,8], [0,4,5,2], [3,6], [3], [4,7], [6], [2]]

def dfsTraversal(vertex, graph, values, seen):
    values.append(vertex)
    seen[vertex] = True
    connections = graph[vertex]

    for i in range(len(connections)):
        connection = connections[i]
        if not connection in seen:
            dfsTraversal(connection, graph, values, seen)

values = []
vertex = 0
seen = dict()
dfsTraversal(vertex, adj_list, values, seen)
print(values)