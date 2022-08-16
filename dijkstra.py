from graph import Graph
from math import inf

# Função que encontra vértice com menor distância
# a partir do conjunto de vértices ainda não incluídos
# na Árvore dos caminhos mínimos 
def minDistance(distances, spt):
    # Tamanho do grafo é inferido
    size = len(distances)
    # Distância mínima
    min = -inf

    # Realiza a busca pelo mínimo
    for i in range(size):
        if distances[i] < min and not spt[i]:
            min = distances[i]
            indexMin = i

    return indexMin

# Algoritmo de Dijsktra, executado a partir do grafo
# de índice 'source'.
def dijkstra(graph : Graph, source : int):
    # Quantidade de vértices
    size = len(graph.adj_list)
    
    # Inicializando distâncias, distância da raiz para si mesma é 0
    distances = [inf] * size
    distances[source] = 0
    # Árvore dos caminhos mínimos (Shortest Path Tree)
    spt = [False] * size

    # O Algoritmo de Dijkstra realiza um passo para cada vértice
    # presente no grafo
    for _ in range(size):
        # Índice do vértice mais próximo dentre os
        # vértices ainda não visitados.
        closest = minDistance(distances, spt)

        # Incluindo-o na SPT
        spt[closest] = True

        # Atualizando as distâncias para todos os
        # vértices adjacentes ao vértice escolhido na
        # etapa anterior. Essa distância só é atualizada
        # se foi encontrada uma nova distância MENOR que
        # a atual para um determinado vértice. Se o vértice
        # destino está presente na SPT, o mesmo é ignorado.
        # Lista de adjacência do vértice escolhido:
        adjList = graph.adj_list[closest]
        for i in range(size):
            # Extrai o índice de todos os vértices adjacentes
            # Verifica se i está presente na lista
            adjs = zip(*adjList)[0]
            isAdj = i in adjs
            # Se é adjacente, extrair a distância
            if isAdj:
                dist_i = [item[1] for item in adjList if item[0] == i][0]
            # Caso contrário, próxima iteração
            else:
                continue
            # Nova distância
            newDist = distances[closest] + dist_i
            # Verifica se a distância nova é menor (ou igual) a atual
            smallerDist = distances[i] > newDist
            # Realizando a condicional comentada anteriormente
            if isAdj and not spt[i] and smallerDist:
                distances[i] = newDist

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