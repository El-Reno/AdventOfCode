import sys

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

class Graph:

    # Class constructor for initializing the Graph using a diction
    def __init__(self):
        # List of vertices
        self.vertices = []
        self.num_vertices = 0

    def GetVertices(self):
        return self.vertices;

    def GetNumVertices(self):
        return self.num_vertices

    # Adds a node to the graph
    # The node becomes a vertex in the Graph
    # Returns:
    # 1 - successfully added
    # 0 - Node already there
    # -1 - failed to add
    def AddVertex(self, vertex):
        if(vertex not in self.vertices):
            self.vertices.append(vertex)
            self.num_vertices += 1
            return 1
        else:
            return 0
        return -1

    # Removes a node in the graph
    # Returns the node if successfull, otherwise KeyException thrown
    def RemoveVertex(self, vertex):
        try:
            return self.vertices.remove(vertex)
        except ValueError:
            print("Vertex not found")
            return None

    # Tests whether Node X and Node Y are adjacent
    def Adjacent(self, x, y):
        adjacent = False
        if(y in x.GetNeighbors()):
            adjacent = True
        return adjacent

    # Returns a list of neighbors for Node X
    def Neighbors(self, x):
        return x.GetNeighbors()

    # Adds an edge between the Vertices X and Y with weight
    def AddEdge(self, x, y, weight=1):
        if(x not in self.vertices):
            self.AddVertex(x)
        if(y not in self.vertices):
            self.AddVertex(y)
        x.AddNeighbor(y, weight)
        y.AddNeighbor(x, weight)

    # Removes an edge from the graph
    def RemoveEdge(self, x, y):
        if(x in self.vertices and y in self.vertices):
            if(self.Adjacent(x,y)):
                x.RemoveNeighbor(y)
                y.RemoveNeighbor(x)

    # Returns distance associated with the path
    def PathDistance(self, path):
        dist = 0
        # Use <= 1 so if a path that is empty shows up, the length is 0
        if(len(path) <= 1):
            return 0
        else:
            source = path[0]
            dist += path[1].GetNeighbor(source) + self.PathDistance(path[1:])
        return dist

    # Returns all paths between nodes source and dest
    # Path list is empty if no path exists
    def FindAllPaths(self, source, dest, path=[]):
        path = path + [source]
        newpaths = []
        paths = []
        if(source.GetName() == dest.GetName()):
            return [path]
        for neighbor in source.GetNeighbors():
            if neighbor not in path:
                newpaths = self.FindAllPaths(neighbor, dest, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    # Returns a tuple containing the minimum distance and path
    def FindShortestPath(self, source, dest):
        paths = []
        minPath = []
        allPaths = self.FindAllPaths(source, dest, paths)
        minDist = sys.maxsize
        for path in allPaths:
            dist = self.PathDistance(path)
            if(dist < minDist):
                minDist = dist
                minPath = path
        return (minDist, minPath)

    # DepthFirstSearch algorithm from the starting source
    def DepthFirstSearch(self, source, explored=[]):
        explored += [source]
        if(len(source.GetNeighbors()) == 0):
            return 1
        for neighbor in source.GetNeighbors():
            if neighbor not in explored:
                self.DepthFirstSearch(neighbor, explored)
        return explored

    # Calculates the Orbit Count Checksum
    def OrbitCountChecksum(self, source):
        allPaths = []
        checksum = 0
        for v in self.vertices:
            if(v != source):
                allPaths.append(self.FindAllPaths(source, v))
        for paths in allPaths:
            for p in paths:
                # Remove COM
                p.pop(0)
                checksum += len(p)
        return checksum


# For testing purposes
if __name__ == "__main__":
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')
    h = Vertex('H')
    i = Vertex('I')
    j = Vertex('J')
    g = Graph()
    g.AddEdge(a,b,5)
    g.AddEdge(b,c,3)
    g.AddEdge(c,f,4)
    g.AddEdge(a,i)
    g.AddEdge(i,j)
    g.AddEdge(j,f)
    g.AddEdge(a,d,4)
    g.AddEdge(d,e)
    g.AddEdge(e,f,2)
    g.AddEdge(f,h)
    paths = g.FindAllPaths(a, f)
    print("All Paths from a to f: {0}".format(paths))
    print("Minimum path: {0}".format(g.FindShortestPath(a,f)))
