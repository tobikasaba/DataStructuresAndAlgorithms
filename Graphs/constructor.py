class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ": ", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            # accounts for situations where a vertex is added but does not have an edge
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        # check if the vertex is in the graph
        if vertex in self.adj_list.keys():
            # check for all the vertices that the vertex has a bidirectional edge with
            for other_vertex in self.adj_list[vertex]:
                # remove the vertex from the list of edges which are present in each of the "other_vertex"
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.print_graph()

print("\n----Adding an edge------")
my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_edge(1, 2)
my_graph.print_graph()

print("\n-----Removing an edge-----")
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')
my_graph.print_graph()

print("----After Applying The Method----")
my_graph.remove_edge('A', 'B')
my_graph.print_graph()

print("\n-----Removing a vertex-----")
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')
my_graph.print_graph()

print("----After Applying The Method----")
my_graph.remove_vertex("D")
my_graph.print_graph()
