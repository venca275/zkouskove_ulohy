from cProfile import label
from vertex import Vertex

class Graph:

    def __init__(self, lines):
        self.vertices = {}
        # Cycle that goes through all the lines in the file
        for line in lines:
            [label1, label2] = line.split(" ")
            if label1 not in self.vertices: # adds label1 to the list in the Vertex class if it is not already there
                self.vertices[label1] = Vertex(label1)
            if label2 not in self.vertices: # adds label2 to the list in the Vertex class if it is not already there
                self.vertices[label2] = Vertex(label2)
            self.vertices[label1].add_neighbour(self.vertices[label2])
            self.vertices[label2].add_neighbour(self.vertices[label1])