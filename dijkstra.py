from io import TextIOWrapper
from graph import Graph
from math import inf

# Função que encontra vértice com menor distância
# a partir do conjunto de vértices ainda não incluídos
# na Árvore dos caminhos mínimos 
def minDistance(distances : list, path : list) -> int:
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

# Função para ler os vértices de um arquivo texto
def readFromFile(file : TextIOWrapper) -> Graph:
    # Cada linha deve ter o formato O,D,P
    # Onde:
    # O é a origem
    # D é o destino
    # P é o peso
    lines = file.readlines()
    connections = list()
    # Vértice com maior número determina o tamanho do grafo
    maximum = 0
    for l in lines:
        # Removendo todos espaços e quebra de linha
        l = l.replace(' ', '')
        l = l.replace('\n', '')
        # Lendo as informações
        source, destination, value = l.split(',')
        connections.append((int(source), int(destination), int(value)))
        # Atualizando máximo
        newMax = max(int(source), int(destination))
        if newMax > maximum:
            maximum = newMax
    # Tamanho do grafo é 1 a mais que o vértice de maior valor
    size = maximum + 1
    # Gerando e retornando grafo
    return Graph(connections, size)

# Função auxiliar que transforma lista
# em string com setas como delimitadores
def printList(lst : list) -> str:
    list_str = str(lst)
    # Removendo colchetes
    list_str = list_str.replace("[", "")
    list_str = list_str.replace("]", "")
    # Transformando vírgulas em setas
    list_str = list_str.replace(",", " ->")
    return list_str

# Função auxiliar para mostrar as informações
def printInfo(source : int, path : list, distances : list, predecessors : dict):
    print(f'Caminho ideal calculado pelo Algoritmo de Dijkstra: {printList(path)}')
    print(f'Distância e caminho a partir da origem ({source}) até cada vértice:')
    for i, dist in enumerate(distances):
        # Formando caminho até a origem a partir dos predecessores
        path_i = [i]
        predecessor_i = predecessors.get(i, None)
        # Caso não seja origem (sem predecessor)
        if predecessor_i is not None:
            path_i.append(predecessor_i)
            while predecessor_i != 0:
                predecessor_i = predecessors[predecessor_i]
                path_i.append(predecessor_i)
        # Invertendo caminho para partir da origem
        path_i.reverse()
        print(f'{printList(path_i)}: {dist}')

# Função main, executada quando o arquivo é aberto como script
if __name__ == '__main__':
    try:
        filename = input('Digite um arquivo contendo o grafo: ')
        with open(filename, 'r') as f:
            graph = readFromFile(f)
        source = input('Digite o número do vértice de origem: ')
        source = int(source)
        path, distances, predecessors = dijkstra(graph, source)
        printInfo(source, path, distances, predecessors)
    except FileNotFoundError:
        print('O arquivo digitado não existe, favor indicar um arquivo válido.')