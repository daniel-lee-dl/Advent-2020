import copy
from collections import namedtuple
import time

class seating_grid:
    def __init__(self, grid):
        self.grid = grid
        self.numRows = len(grid)
        self.numColumns = len(grid[0])

    def _is_empty(self, rowNum, colNum):
        if (self.grid[rowNum][colNum] == "L"):
            return True
        else:
            return False

    def _is_occupied(self, rowNum, colNum):
        if (self.grid[rowNum][colNum] == "#"):
            return True
        else:
            return False

    def _is_floor(self, rowNum, colNum):
        if (self.grid[rowNum][colNum] == "."):
            return True
        else:
            return False

    # Used for Part 1 solution - looks at all of the seat's neighbours and returns the number of occupied seats
    def _evaluate_adjacent_seats(self, rowNum, colNum):
        occupiedEqSeats = 0
        equivalentRows = [row for row in range (rowNum - 1, rowNum + 2) if 0 <= row < self.numRows]
        equivalentColumns = [col for col in range (colNum - 1, colNum + 2) if 0 <= col < self.numColumns]
        for row in equivalentRows:
            for column in equivalentColumns:
                if (row == rowNum and column == colNum):
                    pass
                elif (self._is_occupied(row, column)):
                    occupiedEqSeats += 1
        return occupiedEqSeats

    # Used for Part 1 solution - if there are no occupied adjacent seats then occupy the seat, if there are more than 4 occupied seats empty the seat
    def occupy_by_adjacent_seats(self):
        seatsStable = True
        updatedSeats = copy.deepcopy(self.grid)
        for row in range (0, self.numRows):
            for column in range (0, self.numColumns):
                occupiedEqSeats = self._evaluate_adjacent_seats(row, column)
                if (self._is_empty(row, column) and occupiedEqSeats == 0):
                    updatedSeats[row][column] = "#"
                    seatsStable = False
                elif (self._is_occupied(row, column) and occupiedEqSeats >= 4):
                    updatedSeats[row][column] = "L"
                    seatsStable = False

        self.grid = updatedSeats
        return seatsStable


    # Used for Part 2 solution
    def _evaluate_directional_seats (self, rowNum, colNum):
        Direction = namedtuple('Direction', ['row', 'column'])
        occupiedSeats = 0

        directions = []
        
        for rowDirection in (-1, 0, 1):
            for columnDirection in (-1, 0, 1):
                if (rowDirection == 0 and columnDirection == 0):
                    pass
                else:
                    directions.append(Direction(row = rowDirection, column = columnDirection))
        
        for direction in directions:
            continueSearching = True
            step = 1
            while (continueSearching):
                row = rowNum + direction.row * step
                column = colNum + direction.column * step
                if (row < 0 or row >= self.numRows or column < 0 or column >= self.numColumns):
                    continueSearching = False
                elif (self._is_empty (row, column)):
                    continueSearching = False
                elif (self._is_occupied(row, column)):
                    occupiedSeats += 1
                    continueSearching = False
                step += 1

        return occupiedSeats

    # Used for Part 2 solution
    def occupy_by_directional_seats(self):
        seatsStable = True
        updatedSeats = copy.deepcopy(self.grid)
        for row in range (0, self.numRows):
            for column in range (0, self.numColumns):
                occupiedEqSeats = self._evaluate_directional_seats(row, column)
                if (self._is_empty(row, column) and occupiedEqSeats == 0):
                    updatedSeats[row][column] = "#"
                    seatsStable = False
                elif (self._is_occupied(row, column) and occupiedEqSeats >= 5):
                    updatedSeats[row][column] = "L"
                    seatsStable = False
        self.grid = updatedSeats
        return seatsStable
        

    def number_of_occupied_seats(self):
        occupiedSeats = 0
        for row in self.grid:
            occupiedSeats += row.count('#')
        return occupiedSeats



# load_ file and return a dictionary containing the bag and the bags it contains
def load_file():
    inputFile = open("Day11Input.txt", "r")
    numbers = [list(line.strip()) for line in inputFile.readlines()]
    return numbers

def main():
    seats = seating_grid(load_file())
    seats_stable = False
    while (seats_stable == False):
        seats_stable = seats.occupy_by_adjacent_seats()
    print ("Answer to part 1:", seats.number_of_occupied_seats())


    seats = seating_grid(load_file())
    seats_stable = False
    while (seats_stable == False):
        seats_stable = seats.occupy_by_directional_seats()
    print ("Answer to part 2:", seats.number_of_occupied_seats())


if __name__ == "__main__":
    (main())

