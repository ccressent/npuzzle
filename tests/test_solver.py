import unittest

from npuzzle.astar import Node
from npuzzle.solver import EightPuzzle


class TestEightPuzzle(unittest.TestCase):

    def test1(self):
        """
        If the initial state and the goal state are the same, an empty solution
        is returned.
        """
        init = Node([0,1,2,3,4,5,6,7,8])
        goal = Node([0,1,2,3,4,5,6,7,8])

        solution = EightPuzzle(init, goal).solve()
        self.assertEqual(len(solution), 0)

    def test2(self):

        init = Node([1,2,0,
                     3,4,5,
                     6,7,8])

        goal = Node([0,1,2,
                     3,4,5,
                     6,7,8])

        solution = EightPuzzle(init, goal).solve()
        self.assertEqual(len(solution), 2)

    def test3(self):
        init = Node([3,1,2,
                     6,4,5,
                     0,7,8])

        goal = Node([0,1,2,
                     3,4,5,
                     6,7,8])

        solution = EightPuzzle(init, goal).solve()
        self.assertEqual(len(solution), 2)
