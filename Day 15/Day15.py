from time import time

class Memory_Game:
    def __init__(self, initialNumbers):
        # NumbersHist will keep track of the numbers that were spoke already (key) and the turns that they were spoken (values)
        self.numbersHist = {}
        self.currentTurn = 0
        self.lastNumber = 0

        for number in initialNumbers:
            self._add_number(number)

    def _add_number(self, number):
        self.currentTurn += 1
        
        if (number not in self.numbersHist):
            self.numbersHist[number] = [self.currentTurn]
        else:
            self.numbersHist[number].append(self.currentTurn)
        
        self.lastNumber = number
    
    def _take_turn(self):
        numberHist = self.numbersHist[self.lastNumber]
        if (len(self.numbersHist[self.lastNumber]) == 1):
            self._add_number(0)
        else:
            self._add_number(numberHist[-1] - numberHist[-2])

    # This function will play the game until a given turn, and return the number spoken at the turn
    def play_game(self, turn):
        while (self.currentTurn < turn):
            self._take_turn()
        return self.lastNumber

def load_file():
    f = open("Day15Input.txt", "r")

    numbers = [[int(number) for number in line.strip().split(",")] for line in f.readlines()]    
    
    return numbers

def main():
    for numberSet in load_file():
        start = time()
        game = Memory_Game(numberSet)
        print ("Answer to part 1: ", game.play_game(2020))
        end = time()
        print ("Time taken for part 1 (in seconds): ", end - start)

        start = time()
        game = Memory_Game(numberSet)
        print ("Answer to Part 2: ", game.play_game(30000000))
        end = time()
        print ("Time taken for part 2 (in seconds):", end - start)

if __name__ == "__main__":
    (main())


