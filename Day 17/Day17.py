from __future__ import annotations

from typing import List, Tuple
import numpy as np
from time import time

# The layout of the numpy array is organized to match the puzzle examples
# That is, the first index will select the z value, the second index will select the y value, and the third index will select the x value
class ConwayCubes:
    def __init__(self, initialState, fourthDimension):
        self.state = np.array(initialState)
        self.fourthDimension: bool = fourthDimension

    def _add_dimensions(self):
        for dim in range(0, len(self.state.shape)):
            shape = list(self.state.shape)
            shape = tuple(shape[:dim] + [1] + shape[dim + 1 :])
            self.state = np.concatenate(
                [np.zeros(shape), self.state, np.zeros(shape)], axis=dim
            )

    def _get_neighbours(self, multiIndex):

        z: int = multiIndex[-3]
        y: int = multiIndex[-2]
        x: int = multiIndex[-1]

        # Create a "sliding window" to return neighbours
        if self.fourthDimension == True:
            w: int = multiIndex[-4]

            neighbours = self.state[
                max(0, w - 1) : w + 2,
                max(0, z - 1) : z + 2,
                max(0, y - 1) : y + 2,
                max(0, x - 1) : x + 2,
            ]

        else:
            neighbours = self.state[
                max(0, z - 1) : z + 2, max(0, y - 1) : y + 2, max(0, x - 1) : x + 2
            ]

        return neighbours

    def cycle_state(self):
        self._add_dimensions()

        changeToActive: List[int] = []
        changeToInactive: List[int] = []

        with np.nditer(self.state, flags=["multi_index"], op_flags=["writeonly"]) as it:
            for x in it:
                activeCellCount: int = np.sum(self._get_neighbours(it.multi_index))
                if x == 0 and activeCellCount == 3:
                    changeToActive.append(it.multi_index)
                elif x == 1 and (activeCellCount - 1 != 2 and activeCellCount - 1 != 3):
                    changeToInactive.append(it.multi_index)

        for index in changeToActive:
            self.state[index] = 1
        for index in changeToInactive:
            self.state[index] = 0


# Load all of the input file data into data structures
def load_file(fourthDimension):
    f = open("Day17Input.txt", "r")

    # Change the input so that 0 represents an inactive cube (".") and 1 represents an active cube ("#")
    initialState: List[List[int]] = [
        [
            [int(num) for num in list(line.strip().replace(".", "0").replace("#", "1"))]
            for line in f.readlines()
        ]
    ]

    if fourthDimension:
        initialState = [initialState]

    return initialState


def main():
    # Code for Part 1 of the problem
    initialState = load_file(fourthDimension=False)
    initialState = np.array(initialState)
    conwayCubes = ConwayCubes(initialState, fourthDimension=False)
    for _ in range(0, 6):
        conwayCubes.cycle_state()
    print("Answer to Part 1:", int(np.sum(conwayCubes.state)))

    # Unfortunately, the approach I took doesn't scale very well for part 2, which changes the input into a hypercube with a 4th dimension
    # Decided to just add an indicator to indicate if the fourth dimension exists or not
    initialState = load_file(fourthDimension=True)
    initialState = np.array(initialState)
    conwayCubes = ConwayCubes(initialState, fourthDimension=True)
    for _ in range(0, 6):
        conwayCubes.cycle_state()
    print("Answer to Part 2:", int(np.sum(conwayCubes.state)))


if __name__ == "__main__":
    (main())
