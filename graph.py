# Necessário utilizar grafos direcionados com peso

# Classe utilizada para implementar grafos
class Graph:
    def __init__(self, connections, n):
        # Lista de adjacência, com n vértices
        # Cada elemento da lista é uma lista em si, visto
        # que um único vértice pode ter mais de um vizinho,
        # logo o número é variável.
        self.adj_list = list()
        for _ in range(n):
            self.adj_list.append(list())
 
        # Incluindo arestas para formar os grafos direcionados com peso
        for (source, destination, value) in connections:
            # Para o grafo de origem, adicionar destino e peso
            self.adj_list[source].append((destination, value))
 