from astar import Problem, Node
from heuristics import manhattan_distance


class EightPuzzle(Problem):

    def heuristic(self, node):
        return manhattan_distance(node.state, self.goalState.state)

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


