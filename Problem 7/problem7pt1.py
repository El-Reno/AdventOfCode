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
file = open('example1.txt','r')
computer = IC.IntcodeComputer(file)
phases = CreatePhaseSequences([x for x in range(0,5)])
print("Length: {0}".format(len(phases)))
print(phases)
