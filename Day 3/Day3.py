# Create a function to accept the current position and the slope, and return the new position
# Will return None if we are at the bottom
def new_coordinate (currentCoor, slope, rowLength, columnLength):
    xNewCoor = currentCoor[0] + slope[0]
    yNewCoor = currentCoor[1] + slope[1]
    if (xNewCoor >= rowLength):
        xNewCoor = xNewCoor % rowLength
    if (yNewCoor >= columnLength):
        return None
    return (xNewCoor, yNewCoor)


def calculate_num_trees (tobogganMap, slope):
    currentCoor = (0, 0)
    numTrees = 0
    rowLength = len(tobogganMap[0])
    columnLength = len(tobogganMap)
    while (currentCoor is not None):
            xCoor = currentCoor[0]
            yCoor = currentCoor[1]
            if (tobogganMap[yCoor][xCoor] == '#'):
                numTrees += 1
            currentCoor = new_coordinate(currentCoor, slope, rowLength, columnLength)
    return numTrees


def main():
    # Get the input and do some cleaning
    inputFile = open('Day3Input.txt', 'r') 
    tobogganMap = [row.strip() for row in inputFile.readlines()]

    # Define the part 1 slope
    part1Slope = (3, 1)
    print ("Answer to Part 1: ", calculate_num_trees(tobogganMap, part1Slope))

    # Define the part 2 slope, set up a for loop and calculate the answer
    part2Slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    part2Product = 1
    for slope in part2Slopes:
        part2Product *= calculate_num_trees(tobogganMap, slope)
    print ("Answer to Part 2: ", part2Product)


if __name__ == "__main__":
    main()

