import Queue as Q

from abc import ABCMeta, abstractmethod


class Node:

    def __init__(self, state, cost=0):
        self.state = state
        self.cost  = cost


class Problem:
    __metaclass__ = ABCMeta

    def __init__(self, initialState, goal):
        self.initialState = initialState
        self.goal = goal

    def goalTest(self, node):
        return node.state == self.goal.state

    @abstractmethod
    def childrenOf(self, node):
        """
        Return a list of new nodes reachable from the current node
        """

    def h1(self, node):
        """
        Number of misplaced tiles
        """
        misplaced = 0

        for x, y in zip(node.state, self.goal.state):
            if x != y:
                misplaced += 1

        return misplaced

    def h2(self, node):
        """
        Manhattan distance to a tile's correct position
        """
        total = 0

        for i in range(len(node.state)):
            x = self.coordinates(node.state.index(i))
            y = self.coordinates(self.goal.state.index(i))
            total += abs(y[0] - x[0]) + abs(y[1] - x[1])

        return total

    @staticmethod
    def coordinates(n):
        return (n % 3, n / 3)

class EightPuzzle(Problem):

    def childrenOf(self, node):

        i = node.state.index(0)
        children = []

        # Empty tile moved left
        if (i % 3) - 1 >= 0:
            c = list(node.state)
            c[i]     = c[i - 1]
            c[i - 1] = 0
            children.append(Node(c, node.cost + 1))

        # Empty tile moved right
        if (i % 3) + 1 <= 2:
            c = list(node.state)
            c[i]     = c[i + 1]
            c[i + 1] = 0
            children.append(Node(c, node.cost + 1))

        # Empty tile moved up
        if i - 3 >= 0:
            c = list(node.state)
            c[i]     = c[i - 3]
            c[i - 3] = 0
            children.append(Node(c, node.cost + 1))

        # Empty tile moved down
        if i + 3 <= 8:
            c = list(node.state)
            c[i]     = c[i + 3]
            c[i + 3] = 0
            children.append(Node(c, node.cost + 1))

        return children


def AStar(problem, f):

    fringe = Q.PriorityQueue()
    fringe.put((0, problem.initialState))
    path = []

    while True:

        if fringe.empty():
            raise NoSolution

        cost, node = fringe.get()
        print "Selected state {} ({})".format(node.state, node.cost)
        #path.append(node)

        if problem.goalTest(node):
            return path

        for successor in problem.childrenOf(node):
            fringe.put((f(successor) + node.cost, successor))


def main():

    #init = Node([1,2,0,3,4,5,6,7,8])
    #goal = Node([0,1,2,3,4,5,6,7,8])

    #init = Node([1,2,3,4,0,5,6,7,8])
    #goal = Node([0,1,2,3,4,5,6,7,8])

    #init = Node([7,2,4,5,0,6,8,3,1])
    #goal = Node([0,1,2,3,4,5,6,7,8])

    #init = Node([1,6,4,8,7,0,3,2,5])
    #goal = Node([0,1,2,3,4,5,6,7,8])

    init = Node([8,1,7,4,5,6,2,0,3])
    goal = Node([0,1,2,3,4,5,6,7,8])

    puzzle = EightPuzzle(init, goal)

    solution = AStar(puzzle, puzzle.h2)
    print solution
    print len(solution)

if __name__ == "__main__":
    main()
