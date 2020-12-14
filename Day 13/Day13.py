def do_Chinese_Remainder_Theorem (busList):

    index = [busList.index(bus) for bus in busList if (bus != "x")]
    busList = [int(bus) for bus in busList if (bus != "x")]

    # Start of Chinese Remainder Theorem

    # We need the remainder of each "timestamp % busID" to fall on the index
    # To do this, set up the remainder such that the "remainder = busID - index" 
    remainders = []
    for i in range (0, len(busList)):
        remainders.append((busList[i] - index[i])%busList[i])
    
    # Calculate the lowest common multiple for buses. This is guaranteed to be the product of all bus IDs because all bus IDs are prime numbers
    busLCM = 1
    for bus in busList:
        busLCM *= bus

    # Step 1: Calculate the product of all other bus IDs for each bus. To do this simply divide the busLCM by the current bus ID
    # We are guaranteed that the busLCM = product of all busIDs because all buses are prime numbers (in all the test cases and the input)
    busIDProducts = [busLCM // bus for bus in busList]

    # Step 2: Calculate the remainder of each of the products calculated above with each busID
    busIDRemainder = [busIDProducts[i] % busList[i] for i in range (0, len(busList))]

    # Step 3: Now we need to find a number x such that "(busIDRemainder[i] * x) % busID[i] = index[i]"
    # These numbers will be stored in "multiplyByList"
    multiplyByList = []
    for i in range (0, len(busList)):    
        multiplyBy = 1
        remainder = busIDRemainder[i]
        while ((remainder * multiplyBy) % busList[i] != remainders[i]):
            multiplyBy += 1
        multiplyByList.append ((remainder * multiplyBy) // busIDRemainder[i])

    # Step 4: Get the sum of "busIDProducts[i] * multiplyByList[i]" for all elements
    totalSum = 0
    for i in range (0, len(multiplyByList)):
        totalSum += multiplyByList[i] * busIDProducts[i]


    # Step 5: The remainder from the total sum after dividing by the lowest common multiple will give us our answer
    finalNum = totalSum % busLCM

    return int(finalNum)



def find_earliest_bus(timestamp, busList):
    minTimeUntilNextDeparture = None
    minBus = None

    busList = [int(num) for num in busList if (num != "x")]

    for bus in busList:
        timeFromLastDeparture = timestamp % bus
        timeUntilNextDeparture = bus - timeFromLastDeparture
        if (minTimeUntilNextDeparture is None or minTimeUntilNextDeparture > timeUntilNextDeparture):
            minTimeUntilNextDeparture = timeUntilNextDeparture
            minBus = bus

    return minTimeUntilNextDeparture, minBus

def load_file():
    f = open("Day13Input.txt", "r")
    inputLines = [line.strip() for line in f.readlines()]
    timestamp = int(inputLines[0])
    busList = [num for num in inputLines[1].split(",")]
    return timestamp, busList

def main():
    timestamp, busList = load_file()
    minWaitTime, minBus = find_earliest_bus(timestamp, busList)
    print ("Answer to Part 1:", minWaitTime * minBus)
    print ("Answer to Part 2:", do_Chinese_Remainder_Theorem(busList))
    do_Chinese_Remainder_Theorem(busList)
if __name__ == "__main__":
    (main())


