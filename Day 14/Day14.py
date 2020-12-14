from collections import namedtuple, OrderedDict

class Computer:
    def __init__ (self, instructions):
        self.instructions = instructions
        self.memory = {}
        self.bits = 36

    # Functions for Part 1
    def _generate_and_or_masks(self, mask):
        
        # In order to overwrite all values except the ones labelled "X", first isolate the values to overwrite by doing an "And" bitwise operation
        #   Only the "X" places will be given a value of "1", so that all of the values to overwrite become "0" after the "And" operation
        andMask = mask.replace("1", "0").replace("X", "1")

        # In order to overwrite all values with the numbers in mask, replace all instances of "X" with 0
        #   This way, when an "or" operation is done the places at "X" will be preserved. All other values will be overwritten because they were set to "0" with "andMask"
        orMask = mask.replace("X", "0")

        return andMask, orMask

    def do_instructions_change_in_values(self):
        for bitMask, operations in self.instructions.items():
            andMask, orMask = self._generate_and_or_masks(bitMask)
            for operation in operations:

                # To isolate the bits that should be overwritten, do an "and" where the bits to be overwritten are 0, and those that are not is 1
                finalNum = int(andMask, 2) & operation.writeValue
                
                # Now that all the bits to be overwritten are 0, do an "or" back so that the bits to be overwritten are flipped to the correct state
                finalNum = int(orMask, 2) | finalNum
                
                self.memory[operation.address] = finalNum

    # Functions for Part 2
    def _generate_possible_addresses(self, maskedAddress, variableIndices):

        # Generate all possible addresses. Chose to write an explicit while loop instead of a recursive function
        allAddresses = set()
        index = variableIndices.pop(0)
        allAddresses.add (maskedAddress[:index] + "0" + maskedAddress[index + 1:])
        allAddresses.add (maskedAddress[:index] + "1" + maskedAddress[index + 1:])
        while (len(variableIndices) > 0):
            newAddresses = set()
            index = variableIndices.pop(0)
            for address in allAddresses:
                newAddresses.add(address[:index] + "0" + maskedAddress[index + 1:])                
                newAddresses.add(address[:index] + "1" + maskedAddress[index + 1:])                
            allAddresses = allAddresses | newAddresses
        return allAddresses

    def do_instructions_change_in_address(self):
        for bitMask, operations in self.instructions.items():
            variableIndices = [i for i in range (0, len(bitMask)) if (bitMask[i]) == "X"]

            for operation in operations:

                # Apply the mask first, and get the binary representation of the resulting address
                maskedAddress = str(bin(int(bitMask.replace("X", "0"), 2) | operation.address)).replace("0b", "")

                # If there are 0 in the preceding bits, those 0's are truncated automatically. Add them back so that the binary string is 36 bits long again
                if (len(maskedAddress) < self.bits):
                    maskedAddress = "0"*(self.bits - len(maskedAddress)) + maskedAddress

                # Pass the masked address and all indexes of "X" to a function that generates all possible indices
                allAddresses = self._generate_possible_addresses (maskedAddress, variableIndices.copy())
                if (2 ** len(variableIndices) != len(allAddresses)):
                    print (bitMask, len(variableIndices), len(allAddresses))

                for address in allAddresses:
                    self.memory[int(address)] = operation.writeValue

    def memory_values_sum(self):
        valuesSum = 0
        for address, value in self.memory.items():
            valuesSum += value
        return valuesSum


def load_file():
    f = open("Day14Input.txt", "r")
    inputLines = [line.strip() for line in f.readlines()]
    memoryOper = namedtuple("MemoryOperation", ["address","writeValue"])

    # Using a dictionary to store the mask and the memory changed is possible because there are no duplicate masks in the input. OrderedDict is used in case order matters
    # Each dictionary entry will store the mask as the key, and a list of the MemoryOperation namedTuple as its values
    inputDict = OrderedDict()
    for line in inputLines:
        if (line.split()[0] == "mask"):
            mask = line.split()[-1]
            inputDict[mask] = []
        else:
            memoryAddress = line.split()[0].replace("mem[", "").replace("]", "")
            value = line.split()[-1]
            inputDict[mask].append(memoryOper(address=int(memoryAddress), writeValue=int(value)))
    return inputDict

def main():
    # Part 1
    computer = Computer(load_file())
    computer.do_instructions_change_in_values()
    print ("Answer to Part 1:", computer.memory_values_sum())

    # Part 2
    computer = Computer(load_file())
    computer.do_instructions_change_in_address()
    print ("Answer to Part 2:", computer.memory_values_sum())

if __name__ == "__main__":
    (main())


