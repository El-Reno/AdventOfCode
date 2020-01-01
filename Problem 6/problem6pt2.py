import sys
from Reno import Graph as Graph
from Reno import Vertex as Vertex

file = open("./input.txt")
g = Graph()
vertices = {}

# creates the graph from day 6 file
def ParseInput(graph, vertices, file):
    # Create the vertices
    for line in file:
        str = line.split(')')
        v1 = Vertex(str[0].strip())
        v2 = Vertex(str[1].strip())
        if(v1 not in vertices):
            vertices[v1.GetName()] = v1
        if(v2 not in vertices):
            vertices[v2.GetName()] = v2
    # Create the edges
    file.seek(0)
    for line in file:
        str = line.split(')')
        graph.AddEdge(vertices[str[0].strip()],vertices[str[1].strip()])


ParseInput(g, vertices, file)

# Use the FindShortestPath function to find the path between Santa and You
# Subtract 2 to eliminate the nodes YOR and SAN from being included
# this finds the minimal number of orbital transfers required
minOrbitalTransfers = g.FindShortestPath(vertices['YOU'],vertices['SAN'])[0] - 2
print("Minimum orbital transfers to reach Santa: {0}".format(minOrbitalTransfers))
