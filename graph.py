class Graph:
    def __init__(self):
        self.graph = {}
        
        
    def add_vertex(self, vertex):
        if vertex not in self.graph: 
            self.graph[vertex]=[]
            
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            
    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
            
            
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)

g.display()