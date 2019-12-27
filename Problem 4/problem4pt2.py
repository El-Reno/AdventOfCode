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
    print(prevValidPass)
    valid = True
    
    return valid

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

passwords = GeneratePasswords(low, high)
validPasswords = ValidPasswords(passwords)
print(validPasswords)
print("Number of valid passwords pt1 rules: {0}".format(len(validPasswords)))
new_validPasswords = []
for prevValidPass in validPasswords:
    if(WtfCriteriaWordingIsBad(prevValidPass)):
        new_validPasswords.append(prevValidPass)
print("Number of valid passwords pt2 rules: {0}".format(len(new_validPasswords)))
print(new_validPasswords)
#print(WtfCriteriaWordingIsBad(248888))
