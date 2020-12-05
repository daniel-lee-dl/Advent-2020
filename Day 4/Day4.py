import re


def load_file():
    # Get the input file and create a list of dictionary, a dictionary represents a passport
    inputFile = open('Day4Input.txt', 'r')
    inputLines = inputFile.readlines()

    passports = [{}]
    i = 0

    for inputLine in inputLines:

        # If the inputline is a new line, then using split() will return an empty list
        inputLine = inputLine.split()

        # Check if the inputline is a new line or if the passports list is empty
        if (not inputLine):
            passports.append({})

        else:
            for i in inputLine:
                passports[-1][i.split(":")[0]] = i.split(":")[1]
    return passports

def part1(passports):
    validPassports = 0
    for passport in passports:
        if ((len(passport) == 8) or ((len(passport) == 7) and ('cid' not in passport.keys()))):
            validPassports += 1
    return validPassports

def part2 (passports):
    
    validFieldPassportsList = []
    # The criteria from part 1 still applies. Only consider the valid passports from part 1
    for passport in passports:
        if ((len(passport) == 8) or ((len(passport) == 7) and ('cid' not in passport.keys()))):
            validFieldPassportsList.append(passport)
    
    validPassports = len(validFieldPassportsList)
    
    for passport in validFieldPassportsList:
        if (int(passport['byr']) < 1920 or int(passport['byr']) > 2002):
            validPassports -= 1
        elif (int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020):
            validPassports -= 1
        elif (int(passport['eyr']) < 2010 or int(passport['eyr']) > 2030):
            validPassports -= 1
        elif (re.search("#[0-9]*[a-f]*", passport['hcl']) is None):
            validPassports -= 1
        elif (re.search("#[(0-9)|(a-f)]*", passport['hcl']).span() != (0, 7) or len(passport['hcl']) > 7):
            validPassports -= 1
        elif (passport['ecl'] not in (['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])):
            validPassports -= 1
        elif (len(passport['pid']) != 9):
            validPassports -= 1
        elif (re.search("cm|in", passport['hgt']) is None):
            validPassports -= 1
        else:
            heightField = passport['hgt']
            height = 0
            if ("cm" in heightField):
                height = int(heightField[:heightField.index("cm")])
            elif ("in" in heightField):
                height = int(heightField[:heightField.index("in")])
            
            if ("cm" in heightField and (height < 150 or height > 193)):
                validPassports -= 1
            elif ("in" in heightField and (height < 59 or height > 76)):
                validPassports -= 1
    return validPassports


passports = load_file()
print ("Answer to Part 1: ", part1(passports))
print ("Answer to Part 2: ", part2(passports))


