class Vertex:

    # Constructor for a Vertex
    # Sets the name of the Vertex
    # Initializes an adjacency list for the vertex using a dictionary, the key is the adjacent node the value is the weight
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.GetName())

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return NotImplemented
        return (self.GetName() == other.GetName())

    def __ne__(self, other):
        if not isinstance(other, Vertex):
            return NotImplemented
        return (self.GetName() != other.GetName())

    # Adds a neighbor vertex with default weight of 1
    # If the neighbor exists, it will update the weight
    def AddNeighbor(self, neighbor, weight=1):
        self.neighbors[neighbor] = weight

    # Removes the neighbor
    def RemoveNeighbor(self, neighbor):
        try:
            self.neighbors.pop(neighbor)
        except KeyError:
            print("Neighbor does not exist for Vertex {0}".format(self.GetName()))

    # Returns the weight of the neighbor
    def GetNeighbor(self, neighbor):
        return self.neighbors[neighbor]

    # Return the list of neighbors with weights
    def GetNeighbors(self):
        return self.neighbors

    # Get the name of the node
    def GetName(self):
        return self.name
