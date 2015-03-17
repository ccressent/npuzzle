from math import sqrt

from npuzzle.astar import Node
from npuzzle.solver import EightPuzzle


def beautify_state(state):
    size = int(sqrt(len(state)))
    s = ""

    for index, value in enumerate(state):

        if index % size == 0 and index != 0:
            s += "\n"

        if value == 0:
            s += ". "

        else:
            s += "{} ".format(value)

    return s


def main():

    init = Node([8,2,1,
                 0,3,5,
                 4,7,6])

    goal = Node([0,1,2,
                 3,4,5,
                 6,7,8])

    solution = EightPuzzle(init, goal).solve()

    print "Initial state:"
    print beautify_state(init.state)
    print ""
    print "Solution found in {} steps:".format(len(solution))
    print ""

    for i, node in enumerate(solution):
        print "Step {}:".format(i + 1)
        print beautify_state(node.state)
        print ""

if __name__ == "__main__":
    main()
