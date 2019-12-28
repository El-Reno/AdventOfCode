import sys

# Range for the passwords is 248345-746315
low = 248345
high = 746315

# Generates the list of possible passowrds
# Input is the starting point and endpoint
# Create them all since there is a small list
def GeneratePasswords(low, high):
    passwords = []
    for num in range(low, high, 1):
        passwords.append(num)
    return passwords

# Gets the nth digit from an integer
def GetDigit(number, n):
    return number // 10**n % 10

# Returns true if the the number contains adjacent digits
def ContainsAdjacentDigits(number):
    for i in range(1, 6, 1):
        if(GetDigit(number, i) == GetDigit(number, i-1)):
            return True
    return False

# Returns true if the number contains digits that are increasing in size or remain the same
def IncreaseOrEqual(number):
    valid = True
    for i in range(5, -1, -1):
        if(GetDigit(number, i) > GetDigit(number, i-1)):
            valid = False
    return valid

# Returns list of adjacent digits
# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444)
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22)
# 248889
def WtfCriteriaWordingIsBad(prevValidPass):
    valid = True
    patterns = []
    sub = ""
    i = 5
    while i >= 0:
        sub = str(GetDigit(prevValidPass, i))
        #print("Outer: " + sub)
        j = i - 1
        while j >= 0:
            #print("Inner: {0}:{1}".format(GetDigit(prevValidPass, i),GetDigit(prevValidPass, j)))
            if(GetDigit(prevValidPass, i) == GetDigit(prevValidPass, j)):
                sub += str(GetDigit(prevValidPass, j))
            else:
                break
            j -= 1
        patterns.append(sub)
        i = j
    return patterns

# Generates a list of passwords that meet the criteria in problem 4 part 1 from a list of passwords
# Criteria
# Two adjacent digits are the same (like 22 in 122345)
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)
def ValidPasswords(list):
    validPasswords = []
    for num in list:
        if(ContainsAdjacentDigits(num) and IncreaseOrEqual(num)):
            validPasswords.append(num)
    return validPasswords

def GoodPattern(pattern):
    return (len(pattern) == 2)

passwords = GeneratePasswords(low, high)
validPasswords = ValidPasswords(passwords)
print("Number of valid passwords pt1 rules: {0}".format(len(validPasswords)))
new_validPasswords = []

# Get the new valid passwords with stupidly worded requirements
for p in validPasswords:
    patterns = WtfCriteriaWordingIsBad(p)
    valid = False
    for pattern in patterns:
        if GoodPattern(pattern):
            valid = True
    if(valid):
        new_validPasswords.append(p)

print("Number of valid passwords pt2 rules: {0}".format(len(new_validPasswords)))
