from math import cos, sin, radians
from collections import namedtuple

class FerryPart1:
    def __init__(self, instructions):
        self.currentPosition = [0,0]
        self.instructions = instructions

        # The direction "East" lies on 0 degrees pointing left. "North" lies on 90 degrees, "West" on the 180 degrees, "South" on the 270 degrees 
        self.orientationDegrees = 0

    def _navigate_in_direction(self, direction, value):
        if (direction == "N"):
            self.currentPosition[1] += value
        if (direction == "S"):
            self.currentPosition[1] -= value
        if (direction == "E"):
            self.currentPosition[0] += value
        if (direction == "W"):
            self.currentPosition[0] -= value

    def _go_forward(self, value):
        orientationCoordinate = (round(cos(radians(self.orientationDegrees))), round(sin(radians(self.orientationDegrees))))
        change = [orientationCoordinate[0] * value, orientationCoordinate[1] * value]
        self.currentPosition[0] += change[0]
        self.currentPosition[1] += change[1]

    def _change_direction (self, direction, degrees):
        if (direction == "L"):
            self.orientationDegrees += degrees
        elif (direction == "R"):
            self.orientationDegrees -= degrees
    
    def navigate_instructions(self):
        for instruction in self.instructions:
            if (instruction.action in ("N","S","E","W")):
                self._navigate_in_direction(instruction.action, instruction.value)
            elif (instruction.action in ("L","R")):
                self._change_direction(instruction.action, instruction.value)
            elif (instruction.action == "F"):
                self._go_forward(instruction.value)
    
    def get_current_position(self):
        return self.currentPosition

class FerryPart2:
    def __init__(self, instructions):
        self.currentPosition = [0,0]
        self.instructions = instructions

        # Initial coordinates were already given in the problem
        self.wayPoint = [10, 1]

    def _move_waypoint(self, direction, value):
        if (direction == "N"):
            self.wayPoint[1] += value
        if (direction == "S"):
            self.wayPoint[1] -= value
        if (direction == "E"):
            self.wayPoint[0] += value
        if (direction == "W"):
            self.wayPoint[0] -= value

    def _go_forward(self, value):
        self.currentPosition[0] += self.wayPoint[0] * value
        self.currentPosition[1] += self.wayPoint[1] * value

    def _rotate_waypoint (self, direction, degrees):
        if (direction == "R"):
            degrees *= -1
        # Rotating relative positions is as follows:
        #   newX = x*cos(degrees) - y*sin(degrees)
        #   newY = x*sin(degrees) + y*cos(degrees)
        newX = self.wayPoint[0] * round(cos(radians(degrees))) - self.wayPoint[1] * round(sin(radians(degrees)))
        newY = self.wayPoint[0] * round(sin(radians(degrees))) + self.wayPoint[1] * round(cos(radians(degrees)))
        self.wayPoint = [newX, newY]

    def navigate_instructions(self):
        for instruction in self.instructions:
            if (instruction.action in ("N","S","E","W")):
                self._move_waypoint(instruction.action, instruction.value)
            elif (instruction.action in ("L","R")):
                self._rotate_waypoint(instruction.action, instruction.value)
            elif (instruction.action == "F"):
                self._go_forward(instruction.value)

    def get_current_position(self):
        return self.currentPosition



def load_file():
    f = open("Day12Input.txt", "r")
    instruction = namedtuple("Instruction", ("action", "value"))
    inputLines = [instruction(action = line[0], value = int(line[1:].strip())) for line in f.readlines()]
    return inputLines

def main():
    ferry = FerryPart1(load_file())
    ferry.navigate_instructions()
    currentPosition = ferry.get_current_position()
    print ("Answer to Part 1:", abs(currentPosition[0]) + abs(currentPosition[1]))
    
    ferry = FerryPart2(load_file())
    ferry.navigate_instructions()
    currentPosition = ferry.get_current_position()
    print ("Answer to Part 1:", abs(currentPosition[0]) + abs(currentPosition[1]))
    

if __name__ == "__main__":
    (main())
