from math import sqrt


def misplaced_tiles(state, goalState):
    """
    Number of misplaced tiles in the given state, compared to the goal state.
    """
    misplaced = 0

    for x, y in zip(state, goalState):
        if x != y:
            misplaced += 1

    return misplaced


def manhattan_distance(state, goalState):
    """
    Manhattan distance to a tile's position in the goal state.
    The 2 states need to be "squares".
    """
    total = 0

    def coordinates(n):
        x = int(sqrt(len(state)))
        return (n % x, n / x)

    for i in range(len(state)):
        x = coordinates(state.index(i))
        y = coordinates(goalState.index(i))
        total += abs(y[0] - x[0]) + abs(y[1] - x[1])

    return total
