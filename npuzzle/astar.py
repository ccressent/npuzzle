import Queue as Q

from abc import ABCMeta, abstractmethod


class Node:

    def __init__(self, state, cost=0, parent=None):
        self.state  = state
        self.cost   = cost
        self.parent = parent


class Problem:
    __metaclass__ = ABCMeta

    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState

    def isGoalState(self, node):
        """
        Return True if the state of the given node correspond to a goal state.
        """
        return node.state == self.goalState.state

    @abstractmethod
    def childrenOf(self, node):
        """
        Return a list of new nodes reachable from the current node.
        """

    @abstractmethod
    def heuristic(self, node):
        """
        Return an estimate of the cost to reach the goal state from the given
        node. A* will only find an optimal solution if the heuristic used is
        admissible, that is it always underestimate the true cost to reach the
        goal.
        """

    def solve(self):
        """
        Attempt to solve the problem, using A*.
        """

        def reconstruct_path(node):

            path = []

            while node.parent is not None:
                path.append(node)
                node = node.parent

            path.reverse()
            return path

        fringe = Q.PriorityQueue()
        fringe.put((0, self.initialState))

        while True:

            if fringe.empty():
                raise NoSolution

            cost, node = fringe.get()
            #print "Selected state {} ({})".format(node.state, node.cost)

            if self.isGoalState(node):
                return reconstruct_path(node)

            for successor in self.childrenOf(node):
                successor.parent = node
                fringe.put((self.heuristic(successor) + successor.cost, successor))
