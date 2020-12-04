# Get the input and do some cleaning
inputFile = open('Day1Input.txt', 'r') 

entries = inputFile.readlines()

for i in range (0, len(entries)):
    entries[i] = entries[i].strip()
    entries[i] = int(entries[i])

# Sort the list
entries.sort()

# Answer to Solution 1:
i = len(entries) - 1

product = 0

while (product == 0):
    maxNum = entries[i]
    for entry in entries:
        if (maxNum + entry > 2020):
            break
        elif (maxNum + entry == 2020):
            product = maxNum * entry
            break
    i -= 1

print ("Solution 1: ", product)

# Answer to solution 2

product = 0

while (product == 0):
    maxNum = entries[i]
    for entry1 in entries:
        for entry2 in entries:
            if (maxNum + entry1 + entry2 > 2020):
                break
            elif (maxNum + entry1 + entry2 == 2020):
                product = maxNum * entry1 * entry2
                break
    i -= 1

print ("Solution 2: ", product)

