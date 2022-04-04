# Dijkstra 's algorithm
# algorithm for finding the shortest paths between nodes in a graph

# input: distance matrix
# output: Node, shortest distance from source

# graph as a dict {node: {adj_node: vertex distance}}
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'D': 1, 'C': 5}
}

unvisited = list(graph.keys())
visited = []

prev_nodes = {n: '' for n in graph}

dist_A = {i: 100 for i in unvisited}
dist_A['A'] = 0

print('')

# visit all nodes
while unvisited:
    # min dist in distances
    aux = 100
    for k, v in dist_A.items():
        if k in unvisited:
            if v < aux:
                node_u = k
                aux = v

    print(f'node_u: {node_u}')
    unvisited.remove(node_u)

    # neighbors not visited
    for node_v in graph[node_u]:

        if node_v in unvisited:

            if prev_nodes[node_v] == '':
                prev_nodes[node_v] = node_u

            print(f'\n \tnode_v: {node_v}')
            print(f'\tdist u -> v: {graph[node_u][node_v]}')
            print('')

            alt = dist_A[node_u] + graph[node_u][node_v]

            # print(f'\tTotal:   {alt}')
            # print(f'\tdist :   {dist_A[node_u]}')
            # print(f'\tvertex : {graph[node_u][node_v]}')

            if alt < dist_A[node_v]:
                dist_A[node_v] = alt
                prev_nodes[node_v] = node_u

            if node_u in visited:
                continue

            else:
                visited.append(node_u)

            # print(f'visited nodes: {visited}')
            # print(f'unvisited nodes: {unvisited}')

    # print(f'\nDistances: {dist_A}')
    # print(f'visited nodes: {visited}')
    # print(f'previous vertex: {prev_nodes}')
    print('-------------------------- \n')
    # break

initial_node = 'A'
end_node = 'C'
aux = ''
total_dist = 0

print('Path A -> C')
print(f'Total distance: {dist_A[end_node]}\n')

while end_node:
    if prev_nodes[end_node] == '':
        break

    print(f'{prev_nodes[end_node]} <- {end_node}')
    print(f'dist:{graph[end_node][prev_nodes[end_node]]}')
    print(' ')

    aux = prev_nodes[end_node]
    end_node = aux
