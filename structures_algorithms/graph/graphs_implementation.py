class Graph(object):
    def __init__(self):
        self.n_nodes = 0
        self.adjacentlist = dict()

    def add_vertex(self, node):
        self.adjacentlist.update({
            node: []
        })
        self.n_nodes += 1

    def addEdge(self, node1, node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)
        return self.adjacentlist

    def print_connections(self):
        for k,v in self.adjacentlist.items():
            print(str(k) + "-->"+"".join(str(i) for i in v))

graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
print(graph.addEdge(1,2))
graph.print_connections()
