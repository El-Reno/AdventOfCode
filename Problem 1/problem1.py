import sys
from math import floor

# For printing debug output
DEBUG = False

# Declare variables needed to read and then store component weights in components array
path = "./input.txt"
file = open(path, 'r')
components = []
# Declare functions for calculation
def CalculateFuel(component):
    return(floor(component / 3) - 2)
# Read the weights from the file
for line in file:
    components.append(int(line))

if DEBUG:
    print(components)
    print("Test for formula with weight 100756")
    print(CalculateFuel(100756))

# Calculate the fuel required for all components
sum_fuel = 0;
for component in components:
    sum_fuel += CalculateFuel(component)

print("Fuel required is: {0}".format(sum_fuel))
