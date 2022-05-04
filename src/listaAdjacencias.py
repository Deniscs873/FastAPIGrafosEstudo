class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        # Grafo direcionado
        self.grafo[u-1].append(v)

        # Grafo não direcionado
        # self.grafo[v-1].appende(u)

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

g = Grafo(4)

g.adiciona_aresta(1,2)
g.adiciona_aresta(1,3)
g.adiciona_aresta(1,4)
g.adiciona_aresta(2,3)

g.mostra_lista()