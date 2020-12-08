from re import search
from collections import namedtuple

# load_ file and return a dictionary containing the bag and the bags it contains
def load_file():
    inputFile = open("Day8Input.txt", "r")
    
    # Regular Expression search strings
    opReg = r"[a-z]*"
    argReg = r"\+\d+|\-\d+"

    # Each namedtuple will  indicate the operation (op) and the argument(arg)
    instruction = namedtuple("Ins", ["op", "arg"])

    # Return a list of namedtuple, one namedtuple for eac instruction
    instructions = [instruction(op=search(opReg, line).group(0), arg=search(argReg, line).group(0)) for line in inputFile.readlines()]

    return instructions


# Function to do all of the instructions
def doInstructions(instructions):
    # Keep a set of visited indices
    visitedIndex = set()
    index = 0
    # Accumulator is the product of the instructions
    accumulator = 0
    infiniteLoop = False
    maxIndex = len(instructions)

    # The instructions should exit in one of two conditions. If the instructions have completed (index < maxIndex), or if there is an infinite loop (index in visitedIndeX)
    while (index < maxIndex and index not in visitedIndex):
        visitedIndex.add(index)
        instruction = instructions[index]
        if (instruction.op == "nop"):
            index += 1
        elif (instruction.op == "acc"):
            accumulator += int(instruction.arg)
            index += 1
        elif (instruction.op == "jmp"):
            index += int(instruction.arg)

        if (index in visitedIndex):
            infiniteLoop = True

    return accumulator, visitedIndex, infiniteLoop


# For Part 2, each instruction in the visited index must be changed, until an instruction set that does not result in an infinite loop is found
def findNonInfiniteInstructions(instructions, visitedIndex):
    modifiedInstruction = namedtuple("Ins", ["op", "arg"])
    finalAccumulator = 0

    for i in visitedIndex:
        modifiedInstructions = instructions.copy()
        
        # As per the problem definition, switch the operations from nop to jmp or vice versa, and do nothing if the operation is acc
        if (modifiedInstructions[i].op == "jmp"):
            modifiedInstructions[i] = (modifiedInstruction(op="nop", arg=modifiedInstructions[i].arg))
        elif (modifiedInstructions[i].op == "nop"):
            modifiedInstructions[i] = (modifiedInstruction(op="jmp", arg=modifiedInstructions[i].arg))

        # If the operation is acc, then do not do the instructions
        if (modifiedInstructions[i].op in ("jmp", "nop")):
            accumulator, visitedIndex, infiniteLoop = doInstructions(modifiedInstructions)

            # If the infiniteLoop indicator returns a False, we found the correct instruction set. Set the finalAccumulatro and break out of the loop
            if (infiniteLoop == False):
                finalAccumulator = accumulator
                break

    return finalAccumulator


def main():
    instructions = load_file()
    accumulator, visitedIndices, infiniteLoop = doInstructions(instructions)
    print ("Answer to Part 1:", accumulator)
    if (infiniteLoop == True):
        print ("Answer to Part 2:", findNonInfiniteInstructions(instructions, visitedIndices))


if __name__ == "__main__":
    main()
