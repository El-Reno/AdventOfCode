# Find the pair (noun / verb) that produces 19690720 given the equation 100 * noun + verb

DEBUG = False

# Declare variables to read input and execute the program
path = "./input.txt"
file = open(path, 'r')
c = []
execute = []

def ExecuteIntcode(code):
    opcode_index = 0
    length = len(code)
    # Iterate through the code until the prgram terminates
    while code[opcode_index] != 99:
        opcode = code[opcode_index]
        if(code[opcode_index+1] < length):
            value1 = code[code[opcode_index+1]]
        else:
            raise ValueError("Index out of bounds ExecuteCode index+1")
        if(code[opcode_index+2] < length):
            value2 = code[code[opcode_index+2]]
        else:
            raise ValueError("Index out of bounds ExecuteCode index+2")
        if(opcode == 1):
            sum = value1 + value2
            # Store the values at locations index plus 1 & 2 in index 3
            if(code[opcode_index+3] < length):
                code[code[opcode_index+3]] = sum
            else:
                raise ValueError("Index out of bounds ExecuteCode index+3")
        elif(opcode == 2):
            m = value1 * value2
            # Store the values at locations index plus 1 & 2 in index 3
            if(code[opcode_index+3] < length):
                code[code[opcode_index+3]] = m
            else:
                raise ValueError("Index out of bounds ExecuteCode index+3")
        opcode_index += 4

def ReadIntcode():
    # Read input and place into code array
    input = file.read()
    for item in input.split(','):
        c.append(int(item))

def CheckAnswer(output):
    # Is the answer 19690720
    return output == 19690720

# noun and verb are between 0 and 99
ReadIntcode()
execute = c.copy()
noun = 0
verb = 0

for n in range(100):
    for v in range(100):
        execute[1] = n
        execute[2] = v
        try:
            ExecuteIntcode(execute)
            #print("Trying noun: {0} and verb {1} and output: {2}".format(n, v, execute[0]))
        except ValueError as err:
            #print("Next pair")
            continue
        if(CheckAnswer(execute[0])):
            noun = n
            verb = v
            print("Found noun: {0} and verb: {1} with output: {2}".format(n, v, execute[0]))
            break
        execute = c.copy()

# Now find the answer to the formula response
answer = (100*noun) + verb
print("Answer is: {0}".format(answer))
