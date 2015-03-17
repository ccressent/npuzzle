import random
import unittest

from npuzzle.heuristics import misplaced_tiles, manhattan_distance


class TestMisplacedTiles(unittest.TestCase):

    def test1(self):
        """
        The number of misplaced tiles between a given state and itself should
        be zero.
        """
        x = range(random.randint(1,32))
        random.shuffle(x)
        self.assertEqual(misplaced_tiles(x, x), 0)

    def test2(self):
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        y = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertEqual(misplaced_tiles(x, y), len(x))


class TestManhattanDistance(unittest.TestCase):

    def test1(self):
        """
        The distance between a given state and itself should be zero.
        """
        n = random.choice([x**2 for x in range(2,9)])
        x = range(n)
        random.shuffle(x)
        self.assertEqual(manhattan_distance(x, x), 0)

    def test2(self):
        x = [1,0,2,
             3,4,5,
             6,7,8]
        y = [0,1,2,
             3,4,5,
             6,7,8]
        self.assertEqual(manhattan_distance(x, y), 2)

    def test3(self):
        x = [8,7,6,
             5,4,3,
             2,1,0]
        y = [0,1,2,
             3,4,5,
             6,7,8]
        self.assertEqual(manhattan_distance(x, y), 24)


if __name__ == "__main__":
    unittest.main()
