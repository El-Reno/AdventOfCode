import sys
sys.path.append('..')

from Reno.Advent import IntcodeComputer as IC

def CreatePhaseSequences(domain=[x for x in range(0, 5)], phaseSequence=[]):
    phaseSequence += []
    phaseSequences = []
    if(len(domain) == 1):
        phaseSequence += [domain[0]]
        return [phaseSequence]
    else:
        for i in range(len(domain)):
            tmp = domain.copy()
            tmp.remove(domain[i])
            restore = phaseSequence.copy()
            phaseSequence += [domain[i]]
            newphases = CreatePhaseSequences(tmp, phaseSequence)
            for newphase in newphases:
                phaseSequences += [newphase]
            phaseSequence = restore
    return phaseSequences

# Open the file with the intcode and create the computer
file = open('input.txt','r')
intcode = file.read().strip()
computer = IC.IntcodeComputer(intcode,'AUTO')
# Day 7 range is 0-4
phaseSequences = CreatePhaseSequences([x for x in range(0,5)])
# 5 amplifiers
amps = 5
maxOut = 0
maxSequence = []
inNum = 0
output = 0

for i in phaseSequences:
    inNum = output = 0
    for j in range(amps):
        computer.ExecuteIntcode([i[j],inNum])
        inNum = output = computer.GetCurrentOutput()
    computer.ResetIntcode()

    if(output > maxOut):
        maxOut = output
        maxSequence = i
print("Max output: {0}".format(maxOut))
print("Max sequence: {0}".format(maxSequence))
