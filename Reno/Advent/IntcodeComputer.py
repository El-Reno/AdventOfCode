DEBUG = False

# Declare variables to read input and execute the program
path = "./input.txt"
file = open(path, 'r')
code = []

# Outputs if the memory location is within the opcode
# Requires integer arguments
def CheckMemoryIndex(location, opcode_len):
    return location < opcode_len

# Reads the position in the opcode
# If mode '0', reads the value at the memory location indicated by the value in position
# If mode '1', then reads the value at the position
def ReadOpcodePosition(position, mode):
    if(mode == '0'):
        if(CheckMemoryIndex(code[position], len(code))):
            return code[code[position]]
        else:
            raise ValueError("Index out of bounds ReadOpcodePosition")
    if(mode == '1'):
        if(CheckMemoryIndex(position, len(code))):
            return code[position]
        else:
            raise ValueError("Index out of bounds ReadOpcodePosition")

# Writes the integer value into the given position
def WriteOpcodePosition(position, value):
    if(CheckMemoryIndex(position, len(code))):
        code[code[position]] = int(value) # Ensure it is an integer
    else:
        raise ValueError("Index out of bounds ReadOpcodePosition")

# Reads the opcode from the current position
# Code is an array of the opcode
# Position is the instruction pointer
# Returns a tupel
def ReadOpcode(position):
    opcode_int = code[position]
    opcode_string = str(opcode_int).zfill(5)
    # The rule says that if the numbers dont exist for the opcode parameters, those numbers are 0
    # So, use the python function to pad the string with zeros to ensure the string length is 5
    return (opcode_string[:3], opcode_string[3:])

def ExecuteIntcode():
    opcode_index = 0
    incrementor = 0
    length = len(code)
    # Iterate through the code until the prgram terminates
    while ReadOpcode(opcode_index)[1] != '99':
        # Begin the loop by reading the opcode
        opcode = ReadOpcode(opcode_index)
        if DEBUG:
            print(code)
            print("Current Opcode: {0}".format(opcode[1]))
            input()
        # Add opcode
        if(opcode[1] == '01'):
            incrementor = 4
            # Third digit in mode portion
            value1_mode = opcode[0][2]
            value1 = ReadOpcodePosition(opcode_index+1, value1_mode)
            # Second digit in mode portion
            value2_mode = opcode[0][1]
            value2 = ReadOpcodePosition(opcode_index+2, value2_mode)
            # Dont need mode for storage value, thats always position mode
            sum = value1 + value2
            # Store the values at locations index plus 1 & 2 in index 3
            WriteOpcodePosition(opcode_index+3, sum)
            opcode_index += incrementor
        # Multiply opcode
        elif(opcode[1] == '02'):
            incrementor = 4
            # Third digit in mode portion
            value1_mode = opcode[0][2]
            value1 = ReadOpcodePosition(opcode_index+1, value1_mode)
            # Second digit in mode portion
            value2_mode = opcode[0][1]
            value2 = ReadOpcodePosition(opcode_index+2, value2_mode)
            # Dont need mode for storage value, thats always position mode
            m = value1 * value2
            # Store the values at locations index plus 1 & 2 in index 3
            WriteOpcodePosition(opcode_index+3, m)
            opcode_index += incrementor
        # Input opcode
        elif(opcode[1] == '03'):
            incrementor = 2
            user_input = input("Enter a value: ")
            user_int = int(user_input)  # Should probably error check
            WriteOpcodePosition(opcode_index+1, user_int)
            opcode_index += incrementor
        # Output opcode
        elif(opcode[1] == '04'):
            incrementor = 2
            value1_mode = opcode[0][2]
            value = ReadOpcodePosition(opcode_index+1,value1_mode)
            if(value == 0):
                print("Program Output: {0}".format(value))
            else:
                print("Program Output: {0}".format(value))
            opcode_index += incrementor
        # Jump if true opcode
        elif(opcode[1] == '05'):
            incrementor = 3
            value1_mode = opcode[0][2]
            value1 = ReadOpcodePosition(opcode_index+1,value1_mode)
            value2_mode = opcode[0][1]
            value2 = ReadOpcodePosition(opcode_index+2,value2_mode)
            if DEBUG:
                print("Opcode {0}".format(opcode[1]))
                print("Opcode modes {0}".format(opcode[0]))
                print("Value 1: {0} Mode: {1}".format(value1, value1_mode))
                print("Value 2: {0} Mode: {1}".format(value2, value2_mode))
                print("Code slice: [{0},{1},{2}]".format(code[opcode_index],code[opcode_index+1],code[opcode_index+2]))
                print("Opcode index: {0}".format(opcode_index))
                print("Incrementor: {0}".format(incrementor))
            if(value1 != 0):
                opcode_index = value2
            else:
                opcode_index += incrementor
        # Jump if false
        elif(opcode[1] == '06'):
            incrementor = 3
            value1_mode = opcode[0][2]
            value1 = ReadOpcodePosition(opcode_index+1,value1_mode)
            value2_mode = opcode[0][1]
            value2 = ReadOpcodePosition(opcode_index+2,value2_mode)
            if DEBUG:
                print("Opcode {0}".format(opcode[1]))
                print("Opcode modes {0}".format(opcode[0]))
                print("Value 1: {0} Mode: {1}".format(value1, value1_mode))
                print("Value 2: {0} Mode: {1}".format(value2, value2_mode))
                print("Code slice: [{0},{1},{2}]".format(code[opcode_index],code[opcode_index+1],code[opcode_index+2]))
                print("Opcode index: {0}".format(opcode_index))
                print("Incrementor: {0}".format(incrementor))
            if(value1 == 0):
                opcode_index = value2
            else:
                opcode_index += incrementor
        # Less than
        elif(opcode[1] == '07'):
            incrementor = 4
            value1_mode = opcode[0][2]
            value1 = ReadOpcodePosition(opcode_index+1,value1_mode)
            value2_mode = opcode[0][1]
            value2 = ReadOpcodePosition(opcode_index+2,value2_mode)
            value3_mode = opcode[0][0]
            value3 = ReadOpcodePosition(opcode_index+3,value3_mode)
            if DEBUG:
                print("Opcode {0}".format(opcode[1]))
                print("Opcode modes {0}".format(opcode[0]))
                print("Value 1: {0} Mode: {1}".format(value1, value1_mode))
                print("Value 2: {0} Mode: {1}".format(value2, value2_mode))
                print("Value 3: {0} Mode: {1}".format(value3, value3_mode))
                print("Code slice: [{0},{1},{2},{3}]".format(code[opcode_index],code[opcode_index+1],code[opcode_index+2],code[opcode_index+3]))
                print("Opcode index: {0}".format(opcode_index))
                print("Incrementor: {0}".format(incrementor))
            if(value1 < value2):
                WriteOpcodePosition(opcode_index+3, 1)
            else:
                WriteOpcodePosition(opcode_index+3, 0)
            opcode_index += incrementor
        # Equals
        elif(opcode[1] == '08'):
            incrementor = 4
            value1_mode = opcode[0][2]
            value1 = ReadOpcodePosition(opcode_index+1,value1_mode)
            value2_mode = opcode[0][1]
            value2 = ReadOpcodePosition(opcode_index+2,value2_mode)
            value3_mode = opcode[0][0]
            value3 = ReadOpcodePosition(opcode_index+3,value3_mode)
            if DEBUG:
                print("Opcode {0}".format(opcode[1]))
                print("Opcode modes {0}".format(opcode[0]))
                print("Value 1: {0} Mode: {1}".format(value1, value1_mode))
                print("Value 2: {0} Mode: {1}".format(value2, value2_mode))
                print("Value 3: {0} Mode: {1}".format(value3, value3_mode))
                print("Code slice: [{0},{1},{2},{3}]".format(code[opcode_index],code[opcode_index+1],code[opcode_index+2],code[opcode_index+3]))
                print("Opcode index: {0}".format(opcode_index))
                print("Incrementor: {0}".format(incrementor))
            if(value1 == value2):
                WriteOpcodePosition(opcode_index+3, 1)
            else:
                WriteOpcodePosition(opcode_index+3, 0)
            opcode_index += incrementor

# Read input and place into code array
def ReadIntcode():
    input = file.read()
    for item in input.split(','):
        code.append(int(item))

ReadIntcode()

# Run the program
ExecuteIntcode()
