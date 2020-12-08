# load_ file and return a dictionary containing the bag and the bags it contains
def load_file():
    inputFile = open('Day7Input.txt', 'r')
    bags = []

    for line in inputFile.readlines():
        bagRule = line.split(" contain ")

        # Get the current bag
        currentbag = bagRule[0].replace(" bags", "")

        # Split the list of inner bags into a list
        innerbag = [i.strip().replace(".", "").replace(" bags", "").replace(" bag", "") for i in bagRule[1].split(",")]
        
        # Create a dictionary to keep count of the number of inner bags the current bag can have
        innerbag = {i[1:].strip(): int(i[0]) for i in innerbag if (i != "no other")}
        bags.append(BagRules(currentbag, innerbag))
    return bags

# Class to contain a single bag and a dictionary containing informatin on the {bag it can contain: number of bags}
# This class also determines if the bag has no more inner bags. This helps massively with the performance for part 2
class BagRules:
    def __init__ (self, bag, subBags):
        self.bagName = bag
        self.contains = subBags
        if (self.contains == {}):
            self.containsNone = True
        else:
            self.containsNone = False


# Function to search the entire list of bags for a single bag and return the bags that contain it
def searchForOuterBag (bagRules, searchString):
    containsBag = set()
    for rule in bagRules:
        if (searchString in rule.contains):
            containsBag.add(rule.bagName)
    return containsBag


# Function to return a list of inner bags given a single bag, as well as how many inner bags there are
# This function also returns if the results can no longer have inner bags
def searchForInnerBag (bagRules, searchString):
    for rule in bagRules:
        if (rule.bagName == searchString):
            return rule.contains, rule.containsNone


def part1(bagRules):
    searchList = set(["shiny gold"])
    containsList = set()
    while (True):
        searchResults = searchForOuterBag (bagRules, searchList.pop())
        for result in searchResults:
            searchList.add(result)
            containsList.add(result)
        if (len(searchList) == 0):
            break
    return len(containsList)


def part2(bagRules):
    searchList = ["shiny gold"]
    numBags = 0
    while (True):
        searchResults, noInnerBags = searchForInnerBag(bagRules, searchList.pop())
        for result in searchResults:
            if (noInnerBags == False):
                searchList.extend([result] * searchResults[result])
            numBags += searchResults[result]
        if (len(searchList) == 0):
            break
    return numBags

def main():
    print ("Answer to Part 1:", part1(load_file()))
    print ("Answer to Part 2:", part2(load_file()))
    
if __name__ == "__main__":
    main()


