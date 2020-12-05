def load_file():
    inputFile = open('Day5Input.txt', 'r')
    seats = [i.strip() for i in inputFile.readlines()]
    return seats

def find_row(rowSequence, finalRow):
    maxRows = 127
    rowRange = [0, maxRows]
    finalRowNumber = 0
    
    for i in rowSequence:
        
        # If the character is "F", take the lower half. 
        # The lower half of 127 is defined as 0 to 63
        #   So if the first character is F, we can do: round ((max - min)/2 + min) - 1
        #   Ex: For the first split: round((127-0)/2) = 64. Subtract 1 to get 63 
        if (i == "F"):
            rowRange[1] = round ((rowRange[1] - rowRange[0])/2 + rowRange[0]) - 1

        # If the character is "B", take the upper half. 
        # The latter half of 127 is defined as 64 to 127
        #   So if the first character is B, we can do: ((max - min)//2 + min) + 1
        #   Ex: For the first split: ((127-0)//2) = 63. Add 1 to get 64 
        elif (i == "B"):
            rowRange[0] = ((rowRange[1] - rowRange[0])//2 + rowRange[0]) + 1
        # print (rowRange, rowSequence, finalRow)

    if (finalRow == 'F'):
        finalRowNumber = rowRange[0]
    elif (finalRow == 'B'):
        finalRowNumber = rowRange[1]
    
    return finalRowNumber

def find_column(colSequence, finalCol):
    maxCols = 7
    colRange = [0, maxCols]
    finalColNumber = 0

    for i in colSequence:
        if (i == "L"):
            colRange[1] = round ((colRange[1] - colRange[0])/2 + colRange[0]) - 1
        elif (i == "R"):
            colRange[0] = ((colRange[1] - colRange[0])//2 + colRange[0]) + 1

    if (finalCol == 'L'):
        finalColNumber = colRange[0]
    elif (finalCol == 'R'):
        finalColNumber = colRange[1]
    return  finalColNumber

def main():
    seatID = []
    seats = load_file()
    
    # Generate a list of the seat ID's and sort them
    for i in seats:
        seatID.append(find_row(i[0:6], i[6]) * 8 + find_column(i[7:9], i[9]))
    seatID.sort()
    
    # Answer to part 1 is the max seat ID. Since we've sorted already just return the last item on the list
    print ("Answer to Part 1: ",  seatID[-1])

    # Answer to part 2 is to find the two elements that do not increase by 1 and return the number in between
    mySeatID = 0
    for i in range (0, len(seatID) - 1):
        if (seatID[i] + 1 != seatID[i + 1]):
            mySeatID = seatID[i] + 1

    print ("Answer to Part 2: ", mySeatID)

if __name__ == "__main__":
    main()
