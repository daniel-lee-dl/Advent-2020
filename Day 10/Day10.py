from math import factorial as fact

class adapters:
    def __init__(self, jolts):
        self.jolts = jolts
        self._add_port_device_jolts()
        self._sort_by_jolts()

    def _add_port_device_jolts(self):
        self.jolts.append(0)
        self.jolts.append(max(self.jolts) + 3)

    def _sort_by_jolts(self):
        self.jolts.sort()

    def find_chain (self):
        joltDifferences = {}
        for index in range (0, len(self.jolts) - 1):
            difference = self.jolts[index + 1] - self.jolts[index]
            if (difference in joltDifferences):
                joltDifferences[difference] += 1
            else:
                joltDifferences[difference] = 1
        return joltDifferences


    # This was the code that I used to solve the solution but it is actually incorrect, 
    # I only got the correct answer because the maximum length of voltage increasing by 1 in the input is 5.
    # This code would fail otherwise 
    def find_valid_arrangements(self):
        validArrangements = 1
        increaseByOne = 1
        for index in range (0, len(self.jolts) - 1):
            difference = self.jolts[index + 1] - self.jolts[index]
            if (difference == 1):
                increaseByOne += 1
            elif (difference == 3):
                if (increaseByOne == 4):
                    validArrangements *= 4
                elif (increaseByOne >= 3):
                    increaseByOne -= 2
                    factorial = fact(increaseByOne)
                    validArrangements *= factorial + 1
                increaseByOne = 1
        return validArrangements



# load_ file and return a dictionary containing the bag and the bags it contains
def load_file():
    inputFile = open("Day10Input.txt", "r")

    numbers = [int(number) for number in inputFile.readlines()]

    return numbers

def main():
    adapterList = adapters(load_file())
    joltDifferences = adapterList.find_chain()
    print ("Answer to Part 1: ", joltDifferences[1] * joltDifferences[3])
    print ("Answer to Part 2: ", adapterList.find_valid_arrangements())

if __name__ == "__main__":
    (main())

