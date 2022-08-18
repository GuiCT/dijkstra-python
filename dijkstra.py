from graph import Graph
from math import inf

# Função que encontra vértice com menor distância
# a partir do conjunto de vértices ainda não incluídos
# na Árvore dos caminhos mínimos 
def minDistance(distances, path):
    # Tamanho do grafo é inferido
    size = len(distances)
    # Distância mínima
    valueMin = inf

    # Realiza a busca pelo mínimo
    for i in range(size):
        if distances[i] < valueMin and (i not in path):
            valueMin = distances[i]
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
    # Caminho percorrido pelo algoritmo
    path = list()
    # Predecessores
    predecessors = dict()

    # O Algoritmo de Dijkstra realiza um passo para cada vértice
    # presente no grafo
    for _ in range(size):
        # Índice do vértice mais próximo dentre os
        # vértices ainda não visitados.
        closest = minDistance(distances, path)

        # Incluindo-o no percurso
        path.append(closest)

        # Atualizando as distâncias para todos os
        # vértices adjacentes ao vértice escolhido na
        # etapa anterior. Essa distância só é atualizada
        # se foi encontrada uma nova distância MENOR que
        # a atual para um determinado vértice. Se o vértice
        # destino está presente na SPT, o mesmo é ignorado.
        # Lista de adjacência do vértice escolhido:
        closestDict = graph.adj_list[closest]
        for i in range(size):
            # Extrai o índice de todos os vértices adjacentes
            # Verifica se i está presente na lista
            adjs = closestDict.keys()
            isAdj = i in adjs
            # Se é adjacente, extrair a distância
            if isAdj:
                dist_i = closestDict[i]
            # Caso contrário, próxima iteração
            else:
                continue
            # Verifica se i já está presente no percurso
            inPath = i in path
            # Nova distância
            newDist = distances[closest] + dist_i
            # Verifica se a distância nova é menor (ou igual) a atual
            smallerDist = distances[i] > newDist
            # Realizando a condicional comentada anteriormente
            # Atualizando predecessor de i
            if isAdj and not inPath and smallerDist:
                distances[i] = newDist
                predecessors[i] = closest

    # Retornando o percurso calculado, assim como a distância
    # do vértice de origem para cada um dos vértices no grafo
    return path, distances, predecessors

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
    path, distances, predecessors = dijkstra(graph, 0)
    print('Caminho ideal calculado pelo algoritmo de Dijkstra: ' + str(path))
    print('Distância do vértice de origem (0) para cada vértice:')
    for i, dist in enumerate(distances):
        predecessor_i = predecessors.get(i, None)
        if predecessor_i is None:
            print(f'0: {dist}')
            continue
        path_i = [i]
        predecessor_i = i
        while True:
            predecessor_i = predecessors[predecessor_i]
            path_i.append(predecessor_i)
            if predecessor_i == 0:
                break
        path_i.reverse()
        size_path_i = len(path_i)
        for i in range(size_path_i-1):
            print(f'{path_i[i]} -> ', end='')
        print(f'{path_i[-1]}: {dist}')