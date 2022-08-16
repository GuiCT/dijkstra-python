# Necessário utilizar grafos NÃO direcionados com peso

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
 
        # Incluindo arestas para formar os grafos com peso
        for (first, second, value) in connections:
            # Para o grafo 1, adicionar destino (2) e peso
            self.adj_list[first].append((second, value))
            # Para o grafo 2, adicionar destino (1) e peso
            self.adj_list[second].append((first, value))
 