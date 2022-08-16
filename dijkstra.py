from graph import Graph
from math import inf

# Algoritmo de Dijsktra
def dijkstra(graph : Graph):
    # Quantidade de vértices
    size = len(graph.adj_list)
    # Começando a partir do grafo 0
    visited = [0]
    # Para todos os vértices, se for adjacente ao 0, guardar a distância
    # caso contrário, distância é infinita
    # é infinita também em relação ao próprio vértice
    distances = [inf] * size
    conns = graph.adj_list[0]
    for (ind, val) in conns:
        distances[ind] = val
    
    while len(visited) < size:
        not_n = list(filter(lambda l: l[0] not in visited, conns))
        min_nn = min(not_n, key=lambda l: l[1])
        closest_next = min_nn[0]
        dist_next = [inf] * size
        conns_next = graph.adj_list[closest_next]
        for (ind, val) in conns_next:
            if ind not in visited:
                dist_next[ind] = val
        for i in range(size):
            distances[i] = min(distances[i], distances[closest_next] + dist_next[i])
        last_visited = min(enumerate(distances), key=lambda l: l[1])[0]
        visited.append(last_visited)
        distances[last_visited] = inf

# Testando
if __name__ == '__main__':
    connections = [
        (0, 1, 2),
        (0, 3, 1),
        (0, 2, 5),
        (1, 2, 3),
        (1, 3, 2),
        (2, 3, 3),
        (2, 4, 1),
        (2, 5, 5),
        (3, 4, 1),
        (4, 5, 2)
    ]
    graph = Graph(connections, 6)
    n = dijkstra(graph)