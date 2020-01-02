class IntcodeComputer:
    # Declare variables to read input and execute the program
    code = []
    intcode = ""
    DEBUG = False
    output = 0
    INPUT_MODE = "USER"
    # Constructor for IntcodeComputer
    # Parameter intcode is a string of the incode with whitespace removed
    # DEBUG parameter to print debug statements
    def __init__(self, intcode, inMode="USER", DEBUG=False):
        self.intcode = intcode
        self.DEBUG = DEBUG
        self.ReadIntcode(self.intcode)
        self.INPUT_MODE = inMode

    # Outputs if the memory location is within the opcode
    # Requires integer arguments
    def CheckMemoryIndex(self, location, opcode_len):
        return location < opcode_len

    # Reads the position in the opcode
    # If mode '0', reads the value at the memory location indicated by the value in position
    # If mode '1', then reads the value at the position
    def ReadOpcodePosition(self, position, mode):
        if(mode == '0'):
            if(self.CheckMemoryIndex(self.code[position], len(self.code))):
                return self.code[self.code[position]]
            else:
                raise ValueError("Index out of bounds ReadOpcodePosition")
        if(mode == '1'):
            if(self.CheckMemoryIndex(position, len(self.code))):
                return self.code[position]
            else:
                raise ValueError("Index out of bounds ReadOpcodePosition")

    # Writes the integer value into the given position
    def WriteOpcodePosition(self, position, value):
        if(self.CheckMemoryIndex(position, len(self.code))):
            self.code[self.code[position]] = int(value) # Ensure it is an integer
        else:
            raise ValueError("Index out of bounds ReadOpcodePosition")

    # Reads the opcode from the current position
    # Code is an array of the opcode
    # Position is the instruction pointer
    # Returns a tupel
    def ReadOpcode(self, position):
        opcode_int = self.code[position]
        opcode_string = str(opcode_int).zfill(5)
        # The rule says that if the numbers dont exist for the opcode parameters, those numbers are 0
        # So, use the python function to pad the string with zeros to ensure the string length is 5
        return (opcode_string[:3], opcode_string[3:])

    def ExecuteIntcode(self, inputs=[]):
        opcode_index = 0
        incrementor = 0
        length = len(self.code)
        # Iterate through the code until the prgram terminates
        while self.ReadOpcode(opcode_index)[1] != '99':
            # Begin the loop by reading the opcode
            opcode = self.ReadOpcode(opcode_index)
            if self.DEBUG:
                print(self.code)
                print("Current Opcode: {0}".format(opcode[1]))
                input()
            # Add opcode
            if(opcode[1] == '01'):
                incrementor = 4
                # Third digit in mode portion
                value1_mode = opcode[0][2]
                value1 = self.ReadOpcodePosition(opcode_index+1, value1_mode)
                # Second digit in mode portion
                value2_mode = opcode[0][1]
                value2 = self.ReadOpcodePosition(opcode_index+2, value2_mode)
                # Dont need mode for storage value, thats always position mode
                sum = value1 + value2
                # Store the values at locations index plus 1 & 2 in index 3
                self.WriteOpcodePosition(opcode_index+3, sum)
                opcode_index += incrementor
            # Multiply opcode
            elif(opcode[1] == '02'):
                incrementor = 4
                # Third digit in mode portion
                value1_mode = opcode[0][2]
                value1 = self.ReadOpcodePosition(opcode_index+1, value1_mode)
                # Second digit in mode portion
                value2_mode = opcode[0][1]
                value2 = self.ReadOpcodePosition(opcode_index+2, value2_mode)
                # Dont need mode for storage value, thats always position mode
                m = value1 * value2
                # Store the values at locations index plus 1 & 2 in index 3
                self.WriteOpcodePosition(opcode_index+3, m)
                opcode_index += incrementor
            # Input opcode
            elif(opcode[1] == '03'):
                incrementor = 2
                if(self.INPUT_MODE == "USER"):
                    user_input = input("Enter a value: ")
                    input = int(user_input)  # Should probably error check
                elif(self.INPUT_MODE == "AUTO"):
                    input = inputs.pop(0)
                self.WriteOpcodePosition(opcode_index+1, input)
                opcode_index += incrementor
            # Output opcode
            elif(opcode[1] == '04'):
                incrementor = 2
                value1_mode = opcode[0][2]
                value = self.ReadOpcodePosition(opcode_index+1,value1_mode)
                self.output = value
                if(value == 0):
                    print("Program Output: {0}".format(value))
                else:
                    print("Program Output: {0}".format(value))
                opcode_index += incrementor
            # Jump if true opcode
            elif(opcode[1] == '05'):
                incrementor = 3
                value1_mode = opcode[0][2]
                value1 = self.ReadOpcodePosition(opcode_index+1,value1_mode)
                value2_mode = opcode[0][1]
                value2 = self.ReadOpcodePosition(opcode_index+2,value2_mode)
                if self.DEBUG:
                    print("Opcode {0}".format(opcode[1]))
                    print("Opcode modes {0}".format(opcode[0]))
                    print("Value 1: {0} Mode: {1}".format(value1, value1_mode))
                    print("Value 2: {0} Mode: {1}".format(value2, value2_mode))
                    print("Code slice: [{0},{1},{2}]".format(self.code[opcode_index],self.code[opcode_index+1],self.code[opcode_index+2]))
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
                value1 = self.ReadOpcodePosition(opcode_index+1,value1_mode)
                value2_mode = opcode[0][1]
                value2 = self.ReadOpcodePosition(opcode_index+2,value2_mode)
                if self.DEBUG:
                    print("Opcode {0}".format(opcode[1]))
                    print("Opcode modes {0}".format(opcode[0]))
                    print("Value 1: {0} Mode: {1}".format(value1, value1_mode))
                    print("Value 2: {0} Mode: {1}".format(value2, value2_mode))
                    print("Code slice: [{0},{1},{2}]".format(self.code[opcode_index],self.code[opcode_index+1],self.code[opcode_index+2]))
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
                value1 = self.ReadOpcodePosition(opcode_index+1,value1_mode)
                value2_mode = opcode[0][1]
                value2 = self.ReadOpcodePosition(opcode_index+2,value2_mode)
                value3_mode = opcode[0][0]
                value3 = self.ReadOpcodePosition(opcode_index+3,value3_mode)
                if self.DEBUG:
                    print("Opcode {0}".format(opcode[1]))
                    print("Opcode modes {0}".format(opcode[0]))
                    print("Value 1: {0} Mode: {1}".format(value1, value1_mode))
                    print("Value 2: {0} Mode: {1}".format(value2, value2_mode))
                    print("Value 3: {0} Mode: {1}".format(value3, value3_mode))
                    print("Code slice: [{0},{1},{2},{3}]".format(self.code[opcode_index],self.code[opcode_index+1],self.code[opcode_index+2],self.code[opcode_index+3]))
                    print("Opcode index: {0}".format(opcode_index))
                    print("Incrementor: {0}".format(incrementor))
                if(value1 < value2):
                    self.WriteOpcodePosition(opcode_index+3, 1)
                else:
                    self.WriteOpcodePosition(opcode_index+3, 0)
                opcode_index += incrementor
            # Equals
            elif(opcode[1] == '08'):
                incrementor = 4
                value1_mode = opcode[0][2]
                value1 = self.ReadOpcodePosition(opcode_index+1,value1_mode)
                value2_mode = opcode[0][1]
                value2 = self.ReadOpcodePosition(opcode_index+2,value2_mode)
                value3_mode = opcode[0][0]
                value3 = self.ReadOpcodePosition(opcode_index+3,value3_mode)
                if self.DEBUG:
                    print("Opcode {0}".format(opcode[1]))
                    print("Opcode modes {0}".format(opcode[0]))
                    print("Value 1: {0} Mode: {1}".format(value1, value1_mode))
                    print("Value 2: {0} Mode: {1}".format(value2, value2_mode))
                    print("Value 3: {0} Mode: {1}".format(value3, value3_mode))
                    print("Code slice: [{0},{1},{2},{3}]".format(self.code[opcode_index],self.code[opcode_index+1],self.code[opcode_index+2],self.code[opcode_index+3]))
                    print("Opcode index: {0}".format(opcode_index))
                    print("Incrementor: {0}".format(incrementor))
                if(value1 == value2):
                    self.WriteOpcodePosition(opcode_index+3, 1)
                else:
                    self.WriteOpcodePosition(opcode_index+3, 0)
                opcode_index += incrementor

    # Resets intcode to original state
    def ResetIntcode(self):
        self.code = []
        self.ReadIntcode(self.intcode)

    # Returns the intcode string
    def GetIntcodeString(self):
        return self.intcode

    # Returns the intcode code array
    def GetIntcodeArray(self):
        return self.code

    # Returns the value currently stored in the program output variable
    def GetCurrentOutput(self):
        return self.output

    # Read input and place into code array
    def ReadIntcode(self, intcode):
        for item in intcode.split(','):
            self.code.append(int(item))

    # Reads new intcode file and stores the input into the intcode variable
    def ReadIntcodeFile(self, file):
        input = file.read()
        for item in input.split(','):
            self.code.append(int(item))

if __name__ == '__main__':
    # TODO: Fix this
    ReadIntcode()

    # Run the program
    ExecuteIntcode()
