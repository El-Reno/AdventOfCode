import sys
from math import floor

# For printing debug output
DEBUG = True

# Declare variables needed to read and then store component weights in components array
path = "./input.txt"
file = open(path, 'r')
components = []
# Declare functions for calculation
def CalculateFuel(component):
    return(floor(component / 3) - 2)

def CalculateFuelFuel(fuel_mass):
    if(fuel_mass <= 0):
        return 0
    else:
        return fuel_mass + CalculateFuelFuel(CalculateFuel(fuel_mass))
# Read the weights from the file
for line in file:
    components.append(int(line))

if DEBUG:
    print(components)
    print("Test for formula with weight 100756")
    print(CalculateFuel(100756))
    print("Test for formula with fuel component 20533")
    print(CalculateFuelFuel(CalculateFuel(20533)))

# Calculate the fuel required for all components
sum_fuel = 0;
for component in components:
    component_fuel = CalculateFuel(component)
    component_fuel_fuel = CalculateFuelFuel(CalculateFuel(component_fuel))
    print("Component: {0} + Component Fuel: {1} + Fuel Fuel: {2}".format(component, component_fuel, component_fuel_fuel))
    sum_fuel += component_fuel + component_fuel_fuel

print("Fuel required is: {0}".format(sum_fuel))
