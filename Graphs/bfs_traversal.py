from multiprocessing import connection


adj_list = [[1,3], [0], [3,8], [0,4,5,2], [3,6], [3], [4,7], [6], [2]]

def bfsTraversal(graph):
    queue = [0]
    values = []
    seen = dict()
    while(len(queue)):
        vertex = queue.pop(0)
        values.append(vertex)
        seen[vertex] = True
        connections = graph[vertex]
        for i in range(len(connections)):
            connection = connections[i]
            if not connection in seen:
                queue.append(connection)
    return values


print(bfsTraversal(adj_list))