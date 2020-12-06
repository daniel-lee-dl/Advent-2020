def load_file():
    inputFile = open('Day6Input.txt', 'r')
    answers = [i.strip() for i in inputFile.readlines()]
    return answers

def part_1(answers):
    numAnswers = 0

    distinctAnswers = set()
    # Create a set to store all the answers in, because a set cannot contain duplicates
    for answer in answers:
        # An empty string will indicate that there is a newline character. This indicates the end of the answers for one group
        if (answer == ""):
            numAnswers += len(distinctAnswers)
            distinctAnswers.clear()
        else:
            for letter in answer:
                distinctAnswers.add(letter)

    # If the last element is not a newline, then the final answer set would be missed, so check for that:
    if (answers[-1] != ""):
        numAnswers += len(distinctAnswers)

    return numAnswers


def part_2 (answers):
    numAnswers = 0

    # Create a set to store all the answers in, because a set cannot contain duplicates
    distinctAnswers = set()

    # For part 2, if there are more than one consecutive answers, only the letter in all answers matter
    # Create an indicator to detect if the answer is the first one in the entire group
    firstAnswer = True
    
    for answer in answers:
        # An empty string will indicate that there is a newline character. This indicates the end of the answers for one group
        # Also, an empty string indicates that the current group of answers is at its end. So set the first answer indicator to true
        if (answer == ""):
            numAnswers += len(distinctAnswers)
            distinctAnswers.clear()
            firstAnswer = True
        else:
            if (firstAnswer == True):
                for letter in answer:
                    distinctAnswers.add(letter)
                    firstAnswer = False
            # If any of the answers from the first entry in the group is not found in any subsequent answers, remove them from the set
            else:
                distinctAnswersCopy = distinctAnswers.copy()
                for letter in distinctAnswersCopy:
                    if (letter not in answer):
                        distinctAnswers.remove(letter)

    # If the last element is not a newline, then the final answer set would be missed, so check for that:
    if (answers[-1] != ""):
        numAnswers += len(distinctAnswers)
    
    return numAnswers

def main():
    answers = load_file()
    print ("Answer to Part 1:", part_1(answers))
    print ("Answer to Part 2:", part_2(answers))
    

if __name__ == "__main__":
    main()
