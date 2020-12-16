from __future__ import annotations
from collections import OrderedDict, namedtuple
from typing import Dict, List, Tuple, OrderedDict, Set
from functools import reduce


class TicketChecker:

    # self.fields is an ordered dictionary with the field name as the key, and a list of tuples where each tuple represents the range of numbers allowed for each field
    # self.myTicket contains the list of numbers specified for myTicket
    # self.nearbyTickets is a list of integer list, where each integer list contains numbers specified for one nearby ticket
    def __init__(self, fields, myTicket, nearbyTickets):
        self.fields: OrderedDict[str, List[Tuple(int, int)]] = fields
        self.myTicket: List[int] = myTicket
        self.nearbyTickets: List[List[int]] = nearbyTickets

    # This function will check if a number is valid for a particular field. A number is valid if it is in the given value ranges for each field
    def _value_is_valid(self, number, valueRanges):
        if (
            valueRanges[0].low <= number <= valueRanges[0].high
            or valueRanges[1].low <= number <= valueRanges[1].high
        ):
            return True
        else:
            return False

    # This function verifies whether there are any values that are not valid for all fields. The sum of the invalid values is returned
    # If removeInvalidTickets is set to true, all tickets containing invalid numbers will be removed
    def get_invalid_numbers(self, removeInvalidTickets):
        invalidValues: List[int] = []
        invalidTickets: set(int) = set()

        for index, ticket in enumerate(self.nearbyTickets):
            for number in ticket:
                validForAllFields: bool = False
                for valueRanges in self.fields.values():
                    if self._value_is_valid(number, valueRanges):
                        validForAllFields = True
                        break
                if validForAllFields == False:
                    invalidValues.append(number)
                    invalidTickets.add(index)

        if removeInvalidTickets == True:
            for index in sorted(invalidTickets, reverse=True):
                del self.nearbyTickets[index]

        return invalidValues

    # This function is for Part 2 of the exercise. This function determines what order the fields appear in
    def map_values_to_fields(self):
        self.fieldToValueMap: {str, int} = {}

        # To make things easier, provide all values occurring in an index as its own list
        valuesByIndex: List[List[int]] = [[] for i in self.myTicket]
        for ticket in self.nearbyTickets:
            for index, number in list(enumerate(ticket)):
                valuesByIndex[index].append(number)

        # fieldToIndex will store each field and the possible indices it can occur in. A list of all possible indices is necessary for tie-breaking
        fieldToIndex: Dict[str, List[int]] = {field: [] for field in self.fields.keys()}

        for index, valuesList in list(enumerate(valuesByIndex)):
            for field, ranges in self.fields.items():
                valuesMatchFieldRange: bool = True
                for value in valuesList:
                    if self._value_is_valid(value, ranges) == False:
                        valuesMatchFieldRange = False
                        break
                if valuesMatchFieldRange == True:
                    fieldToIndex[field].append(index)

        # All possible indexes for each field has now been captured. Now, resolve ties between the fields
        while len(fieldToIndex) > 0:
            guaranteedField = None
            guaranteedIndex: int = None
            for field, indexList in fieldToIndex.items():
                if len(indexList) == 1:
                    self.fieldToValueMap[field] = indexList[0]
                    guaranteedField = field
                    guaranteedIndex = indexList[0]

            del fieldToIndex[guaranteedField]
            for indexList in fieldToIndex.values():
                if guaranteedIndex in indexList:
                    indexList.remove(guaranteedIndex)
        return

    # This function accepts the ticket fields as input and returns the value of those fields for self.myTicket
    def get_my_ticket_fields(self, fields):
        results = []

        for field in fields:
            results.append(self.myTicket[self.fieldToValueMap[field]])

        return results


# Load all of the input file data into data structures
def load_file():
    f = open("Day16Input.txt", "r")

    # Knowing the fields is not required for part 1, but I'm assuming that the fields, as well as the order, is important
    fieldsStr, myTicketStr, nearbyTicketsStr = f.read().split("\n\n")

    # Transform a line such as "class: 1-3 or 5-7" into a dict entry of {[class]: [(1,3),(5,7)]}
    fields = OrderedDict()
    fieldRange: namedtuple(int, int) = namedtuple("FieldRange", ["low", "high"])
    fields: OrderedDict[str, List[Tuple(int, int)]] = {
        line.split(":")[0].strip(): [
            fieldRange(
                low=int(numRanges.split("-")[0]), high=int(numRanges.split("-")[1])
            )
            for numRanges in line.split(":")[1].strip().split(" or ")
        ]
        for line in fieldsStr.split("\n")
    }

    # Transform a line such as "your ticket: \n7,1,14" into a list of [7, 1, 14]
    myTicket: List[int] = [
        int(num)
        for line in myTicketStr.split("\n")
        for num in line.split(",")
        if ("your ticket" not in line)
    ]

    # Transform a line such as "nearby tickets: \n7,3,47\n 40,4,50" into a list of [[7,3,47],[40,4,50]]
    nearbyTickets: List[List[int]] = [
        [int(num) for num in line.split(",")]
        for line in nearbyTicketsStr.split("\n")
        if ("nearby tickets" not in line)
    ]

    return fields, myTicket, nearbyTickets


def main():
    fields, myTicket, nearbyTickets = load_file()
    ticketChecker = TicketChecker(fields, myTicket, nearbyTickets)
    print(
        "Answer to Part 1:",
        sum(ticketChecker.get_invalid_numbers(removeInvalidTickets=True)),
    )
    ticketChecker.map_values_to_fields()
    departure_fields = [
        "departure location",
        "departure station",
        "departure platform",
        "departure track",
        "departure date",
        "departure time",
    ]

    print(
        "Answer to Part 2:",
        reduce(
            lambda x, y: x * y, ticketChecker.get_my_ticket_fields(departure_fields)
        ),
    )


if __name__ == "__main__":
    (main())
