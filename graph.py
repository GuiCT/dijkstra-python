# Necessário utilizar grafos NÃO direcionados com peso

# Classe utilizada para implementar grafos
class Graph:
    def __init__(self, connections, n):
        # Lista de adjacência, com n vértices
        # Cada elemento da lista é um dict, com chave
        # indicando o destino e o valor o peso (distância)
        self.adj_list = list()
        for _ in range(n):
            self.adj_list.append(dict())
 
        # Incluindo arestas para formar os grafos com peso
        for (first, second, value) in connections:
            # Para o grafo 1, adicionar destino (2) e peso
            self.adj_list[first][second] = value
            # Para o grafo 2, adicionar destino (1) e peso
            self.adj_list[second][first] = value