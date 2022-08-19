# Dijkstra in Python

Algoritmo de Dijkstra implementado na Linguagem Python, utilizando grafos não direcionados.

# Input

O arquivo exemplo.txt mostra como deve ser realizado o input para a execução do script:
- Cada linha deve conter três números, o vértice de origem, o vértice de destino e o peso(distância) da conexão, separados por vírgulas.
- Não é necessário indicar arestas redundantes, por exemplo:
	- Se foi inserida a aresta (0,1,2) ou seja, vértice 0 está ligado ao vértice 1 com peso 2, logo a aresta (1,0,2) já será adicionada automaticamente.
	- Se uma aresta (1,0,2) for incluída no arquivo, nada irá ocorrer
	- No entanto, se uma aresta (1,0,3) for incluída no arquivo, a aresta anterior com peso 2 será sobscrita.
- Qualquer outro caractere que não seja dígito ou vírgula será ignorado

# Output

O algoritmo executado retornará:
- Caminho ideal encontado pelo Algoritmo de Dijkstra
- Caminho ideal para cada vértice a partir da origem escolhida
- Distância da origem para cada vértice utilizando os caminhos escolhidos
