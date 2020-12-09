from re import search
from collections import namedtuple

class cypher:
    def __init__ (self, numbersList, preambleCount):
        self.numbers = numbersList
        self.preambleCount = preambleCount
            
    def _getPreambleSums(self, index, preambleCount):
        preambleSums = set()

        # Get the sume of any 2 numbers in the preamble list
        for i in range (index - preambleCount, index):
            for j in range (i + 1, index):
                preambleSums.add(self.numbers[i] + self.numbers[j])
        return preambleSums


    def findInvalidNumber(self):
        # For each number, get the set of preamble sums and check if the current number is in the set
        for index in range (self.preambleCount, len(self.numbers)):
            if (self.numbers[index] not in self._getPreambleSums(index, self.preambleCount)):
                return self.numbers[index]
        return None


    def findContiguousSum(self, number):
        # Find the continuous range of numbers that add up to the given number
        contiguousSum = 0
        startIndex = 0
        contiguousNumbers = set()
        while (contiguousSum != number):

            # Add all contiguous numbers starting from the first number until the number is found, or the continuous sum is greater than the number
            for index in range(startIndex, len(self.numbers)):
                if (contiguousSum >= number):
                    break
                contiguousSum += self.numbers[index]
                contiguousNumbers.add(self.numbers[index])
            
            # If the sum of contiguous numbers is greater than the number, reset everything and increment the start index by 1
            if (contiguousSum > number):
                contiguousSum = 0
                contiguousNumbers.clear()
                startIndex += 1

        # If we find the contiguous set that adds up to number, return the sum of the maximum and minimum numbers in the set
        if (contiguousSum == number):
            return min(contiguousNumbers) + max(contiguousNumbers)
        # If we cannot find a contiguous set that adds up to the number, return none (as the contiguousNumbers set will be empty)
        else:
            return None
    

# load_ file and return a dictionary containing the bag and the bags it contains
def load_file():
    inputFile = open("Day9Input.txt", "r")

    # The test example had preambleCount of 5
    # preambleCount = 5
    preambleCount = 25

    numbers = [int(number) for number in inputFile.readlines()]

    return numbers, preambleCount


def main():
    numbers, preambleCount = load_file()
    xmasCypher = cypher(numbers, preambleCount)

    part1Answer = xmasCypher.findInvalidNumber()
    print ("Answer to part 1:", part1Answer)
    
    part2Answer = xmasCypher.findContiguousSum(part1Answer)
    print ("Answer to part 2:", part2Answer)

if __name__ == "__main__":
    (main())
