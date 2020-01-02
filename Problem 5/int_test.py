import sys
sys.path.append('C:\\Users\\kylee\\Documents\\GitHub\\AdventOfCode')
from Reno.Advent import IntcodeComputer as IC

f = open('input.txt','r')
i = f.read().strip()

c = IC.IntcodeComputer(i, "AUTO")
print("Code string before: {0}".format(c.GetIntcodeString()))
print("Code array before: {0}".format(c.GetIntcodeArray()))
c.ExecuteIntcode(1)
print("Code string after: {0}".format(c.GetIntcodeString()))
print("Code array after: {0}".format(c.GetIntcodeArray()))
c.ResetIntcode()
print("Code string after reset: {0}".format(c.GetIntcodeString()))
print("Code array after reset: {0}".format(c.GetIntcodeArray()))
