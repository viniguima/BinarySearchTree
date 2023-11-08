class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append(vertice2)
            self.grafo[vertice2].append(vertice1)

    def remover_vertice(self, vertice):
        if vertice in self.grafo:
            del self.grafo[vertice]
            for v in self.grafo:
                if vertice in self.grafo[v]:
                    self.grafo[v].remove(vertice)

    def remover_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            if vertice2 in self.grafo[vertice1]:
                self.grafo[vertice1].remove(vertice2)
                self.grafo[vertice2].remove(vertice1)

    def imprimir_grafo(self):
        for vertice in self.grafo:
            print(vertice, ":", "->".join(self.grafo[vertice]))

# Adição de Vertices e Arestas
grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')
grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('B', 'C')
grafo.adicionar_aresta('C', 'D')
grafo.adicionar_aresta('D', 'A')
grafo.adicionar_aresta('A', 'C')
grafo.imprimir_grafo()

# Remoção de Vertices e Aresta
print("\nRemovendo vértice 'C' e aresta entre 'A' e 'B':")
grafo.remover_vertice('C')
grafo.remover_aresta('A', 'B')
