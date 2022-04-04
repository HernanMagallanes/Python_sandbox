class Vertex:
    def __init__(self, i):
        self.id = i
        self.visited = False
        self.level = -1
        self.adjacent = []

    def add_adjacent(self, v):
        if not v in self.adjacent:
            self.adjacent.append(v)


class Graph:
    # vertex, edges , incidences
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertex(v)

    def add_edge(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].add_adjacent(b)
            self.vertices[b].add_adjacent(a)


def main():
    g = Graph()

    n = [i for i in range(7)]
    print(f'\nnodes: {n} \n')

    for v in n:
        g.add_vertex(v)

    # incidences
    ind = [2, 0,
           0, 6,
           6, 3,
           0, 5,
           6, 5,
           0, 1,
           6, 4,
           1, 4]

    for i in range(0, len(ind) - 1, 2):
        g.add_edge(ind[i], ind[i + 1])

    print('v adjacent')
    for v in g.vertices:
        print(v, g.vertices[v].adjacent)


if __name__ == '__main__':
    main()
