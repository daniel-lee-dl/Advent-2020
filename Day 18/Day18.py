from __future__ import annotations

from typing import List, Tuple


class IncorrectMath:
    def __init__(self, problems):
        self.problems: List[List[str]] = problems
        self.answers: List[str] = []

    # This function will accept two numbers and an operation ("+" or "*") and will either add or multiply the numbers
    def _add_or_multiply_numbers(self, num1: str, num2: str, oper: str):
        if oper == "+":
            return int(num1) + int(num2)
        if oper == "*":
            return int(num1) * int(num2)

    # If an operation (+ or *) is specified to be of higher priority, do those operations first
    def _evaluate_priority_operations(self, problem: List[str], priOper: str):
        index: int = 0
        while index < len(problem):
            if problem[index] == priOper:
                problem[index - 1] = self._add_or_multiply_numbers(
                    num1=problem[index - 1],
                    oper=problem.pop(index),
                    num2=problem.pop(index),
                )
            index += 1
        return problem

    # If the problem has par, reduce everything within the par (including inner par)
    # into a singe number, and return an updated problem (with no par included)
    def _evaluate_parenthesis(self, problem: str, priOper: str):

        par: List[str] = []

        openBrackets: int = 0
        closeBrackets: int = 0

        # Extract the portion of the problem contained in par
        while openBrackets != closeBrackets or openBrackets == 0:
            var = problem.pop(0)
            par.append(var)
            if var == "(":
                openBrackets += 1
            elif var == ")":
                closeBrackets += 1

        # Because everything in par is guaranteed to have an opening bracket as
        # its first element and a closing bracket as its last element, remove those from the list
        par.pop(0)
        par.pop(-1)

        while len(par) != 1:
            # If any additional brackets are found, recurseively call the function
            if "(" in par:
                par = par[: par.index("(")] + self._evaluate_parenthesis(
                    par[par.index("(") :], priOper
                )
            # If there are priority operations in par, evaluate those first
            elif priOper in par:
                par = self._evaluate_priority_operations(problem=par, priOper=priOper)
            # For the first three items, which will be a number, an operation, and a second number,
            # calculate the product and replace the first element with it
            else:
                par[0] = self._add_or_multiply_numbers(
                    num1=par[0],
                    oper=par.pop(1),
                    num2=par.pop(1),
                )

        return par + problem

    def _solve_problem(self, problem, priOper):
        index = 0
        # Follow the following steps:
        #   Look at the first three variables from the equation at all times, which will be the set of (num, oper, num). Ex: 3 * 3
        #   If there is a par at any one of the num spots, call self._evaluate_parenthesis(),
        #       which will evaluate everything within the paranthesis and return a number
        while index < len(problem):
            if problem[index] == "(":
                problem = problem[:index] + self._evaluate_parenthesis(
                    problem[index:], priOper=priOper
                )
            index += 1

        # If a priority operation is specified, do the priority operations first
        while len(problem) != 1:
            if priOper in problem:
                problem = self._evaluate_priority_operations(
                    problem=problem, priOper=priOper
                )
            else:
                problem[0] = self._add_or_multiply_numbers(
                    num1=problem[0], oper=problem.pop(1), num2=problem.pop(1)
                )

        return problem[0]

    def solve_all_problems(self, priOper: str = ""):
        # For all problems in the list self.problems, call self._solve_problem
        for problem in self.problems:
            self.answers.append(self._solve_problem(problem=problem, priOper=priOper))
        return self.answers


def load_file():
    f = open("Day18Input.txt", "r")

    problems: List[List[int]] = [
        list(line.strip().replace(" ", "")) for line in f.readlines()
    ]
    return problems


def main():
    problemSolver = IncorrectMath(load_file())
    print("Answer to Part 1: ", sum(problemSolver.solve_all_problems()))
    problemSolver = IncorrectMath(load_file())
    print(
        "Answer to Part 2: ",
        sum(problemSolver.solve_all_problems(priOper="+")),
    )


if __name__ == "__main__":
    (main())
