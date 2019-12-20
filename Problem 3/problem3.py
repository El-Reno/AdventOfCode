import sys
from math import dist
import numpy as np

#pathOne = ['R8','U5','L5','D3']
#pathTwo = ['U7','R6','D4','L4']
#pathOne = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#pathTwo = ['U62','R66','U55','R34','D71','R55','D58','R83']
pathOne = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
pathTwo = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

origin = [0,0]

# Function to get max coord value
# axis must be X or Y
def GetMaxAxis(path, axis):
    max_coord = 0
    cur = 0
    if axis == 'X':
        for point in path:
            if(point[0] == 'R'):
                cur += int(point[1:])
                max_coord = max(max_coord, cur)
            elif(point[0] == 'L'):
                cur -= int(point[1:])
                max_coord = max(max_coord, cur)
    elif axis == 'Y':
        for point in path:
            if(point[0] == 'U'):
                cur += int(point[1:])
                max_coord = max(max_coord, cur)
            elif(point[0] == 'D'):
                cur -= int(point[1:])
                max_coord = max(max_coord, cur)
    return max_coord

def InitGrid(x, y):
    grid = np.zeros((x,y))
    return grid

# Returns a new grid with the path
# pathNum is the integer representation of the path (i.e. pathOne is 1)
def AddPathToGrid(path, grid, pathNum):
    curHead = [0,0]
    for point in path:
        if(point[0] == 'R'):
            for x in range(int(point[1:])):
                curHead[0] += 1
                grid[curHead[0]][curHead[1]] += pathNum
        if(point[0] == 'L'):
            for x in range(int(point[1:]), 0, -1):
                curHead[0] -= 1
                grid[curHead[0]][curHead[1]] += pathNum
        if(point[0] == 'U'):
            for y in range(int(point[1:])):
                curHead[1] += 1
                grid[curHead[0]][curHead[1]] += pathNum
        if(point[0] == 'D'):
            for y in range(int(point[1:]), 0, -1):
                curHead[1] -= 1
                grid[curHead[0]][curHead[1]] += pathNum

def GridIntersectionPoints(g):
    points = []
    x = g.shape[0]
    y = g.shape[1]
    for i in range(x):
        for j in range(y):
            if g[i][j] == 3:
                points.append((i,j))
    return points

# Requires the grid as an argument
def ManhattenDistance(g):
    # Don't have a grid over 4 million in any direction
    min_dist = 4000000
    # Find the points of intersection
    intersect_points = GridIntersectionPoints(g)
    for point in intersect_points:
        min_dist = min(min_dist, point[0] + point[1])
    return min_dist

# Get the max x and y for the grid
x = max(GetMaxAxis(pathOne, 'X'), GetMaxAxis(pathTwo, 'X'))
y = max(GetMaxAxis(pathOne, 'Y'), GetMaxAxis(pathTwo, 'Y'))

# Initialize the grid
grid = InitGrid(x + 1,y + 1)
AddPathToGrid(pathOne, grid, 1)
AddPathToGrid(pathTwo, grid, 2)
print("##### Grid prints with X and Y inverted -- thanks python #####")
print(grid)
print("##### Intersection Points #####")
print(GridIntersectionPoints(grid))
print("##### ManhattenDistance #####")
print(ManhattenDistance(grid))
