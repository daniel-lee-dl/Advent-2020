# Get the input and do some cleaning
inputFile = open('Day2Input.txt', 'r') 

rawInput = inputFile.readlines()

entries = []

for entry in rawInput:
    entries.append(entry.split())
    entries[-1][1] = entries[-1][1].replace(":", "")
    entries[-1][0] = [int(integer) for integer in entries[-1][0].split("-")]

# Part 1
validPass = 0

for entry in entries:
    letterCount = entry[2].count(entry[1])
    if (letterCount >= entry[0][0] and letterCount <= entry[0][1]):
        validPass += 1
 
print ("Answer to Part 1: ", validPass)

# Part 2
validPass = 0

for entry in entries:
    password = entry[2]
    character = entry[1]
    indexes = [index - 1 for index in entry[0]]
    if (password[indexes[0]] == character and password[indexes[1]] != character):
        validPass += 1
    elif (password[indexes[0]] != character and password[indexes[1]] == character):
        validPass += 1

print ("Answer to Part 2: ", validPass)
