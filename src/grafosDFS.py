grafo = [ [1],           # Vizinhos do vértice 0.
          [2, 3],        # Vizinhos do vértice 1.
          [1, 4],        # Vizinhos do vértice 2.
          [0],           # Vizinhos do vértice 3.
          [1]            # Vizinhos do vértice 4.
        ]

def dfs(grafo, vertice):
    visitados = set()

    def dfs_iterativa(grafo, vertice_fonte):
        visitados.add(vertice_fonte)
        falta_visitar = [vertice_fonte]
        while falta_visitar:
            vertice = falta_visitar.pop()
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    falta_visitar.append(vizinho)

    dfs_iterativa(grafo, vertice)


    