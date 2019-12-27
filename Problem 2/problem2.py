import sys

DEBUG = False

# Declare variables to read input and execute the program
path = "./input.txt"
file = open(path, 'r')
code = []

# Test cases
case1 = [1,0,0,0,99]
case2 = [2,3,0,3,99]
case3 = [2,4,4,5,99,0]
case4 = [1,1,1,4,99,5,6,0,99]

def ExecuteIntcode(code):
    opcode_index = 0
    # Iterate through the code until the prgram terminates
    while code[opcode_index] != 99:
        opcode = code[opcode_index]
        value1 = code[code[opcode_index+1]]
        value2 = code[code[opcode_index+2]]
        if(opcode == 1):
            sum = value1 + value2
            # Store the values at locations index plus 1 & 2 in index 3
            code[code[opcode_index+3]] = sum
        elif(opcode == 2):
            m = value1 * value2
            # Store the values at locations index plus 1 & 2 in index 3
            code[code[opcode_index+3]] = m
        opcode_index += 4

# Read input and place into code array
input = file.read()
for item in input.split(','):
    code.append(int(item))

if DEBUG:
    print("Read line from file")
    print()
    print(code)
    print(len(code))
    print()
    print("End code line from file")
    print("Test Case")
    ExecuteIntcode(case4)
    print(case4)

# Restore system state per website
code[1] = 12
code[2] = 2

# Run the program
ExecuteIntcode(code)
print("Value at index 0: {0}", code[0])
