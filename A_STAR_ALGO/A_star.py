import math


#  creating the every Node of the Graph acording to Constructor.
class Node:
    def __init__(self, state, parent, actions, heuristic, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.heuristic = heuristic  # Eculidean Distance.
        self.totalCost = totalCost


# Graph on which we will traverse with A* Algo.
graph = {
    "A": Node("A", None, [("F", 1)], (0, 0), 0),
    "B": Node("B", None, [("C", 1), ("G", 1)], (0, 2), 0),
    "C": Node("C", None, [("B", 1), ("D", 1)], (0, 3), 0),
    "D": Node("D", None, [("C", 1), ("E", 1)], (0, 4), 0),
    "E": Node("E", None, [("D", 1)], (0, 5), 0),
    "F": Node("F", None, [("A", 1), ("H", 1)], (1, 0), 0),
    "G": Node("G", None, [("B", 1), ("J", 1)], (1, 2), 0),
    "H": Node("H", None, [("F", 1), ("I", 1), ("M", 1)], (2, 0), 0),
    "I": Node("I", None, [("N", 1), ("J", 1)], (2, 1), 0),
    "J": Node("J", None, [("G", 1), ("I", 1)], (2, 2), 0),
    "K": Node("K", None, [("L", 1), ("P", 1)], (2, 4), 0),
    "L": Node("L", None, [("K", 1), ("Q", 1)], (2, 5), 0),
    "M": Node("M", None, [("H", 1), ("N", 1), ("R", 1)], (3, 0), 0),
    "N": Node("N", None, [("I", 1), ("M", 1), ("S", 1)], (3, 1), 0),
    "O": Node("O", None, [("P", 1), ("U", 1)], (3, 3), 0),
    "P": Node("P", None, [("Q", 1), ("O", 1)], (3, 4), 0),
    "Q": Node("Q", None, [("L", 1), ("P", 1), ("V", 1)], (3, 5), 0),
    "R": Node("R", None, [("M", 1), ("S", 1)], (4, 0), 0),
    "S": Node("S", None, [("N", 1), ("R", 1), ("T", 1)], (4, 1), 0),
    "T": Node("T", None, [("S", 1), ("U", 1), ("W", 1)], (4, 2), 0),
    "U": Node("U", None, [("O", 1), ("T", 1)], (4, 3), 0),
    "V": Node("V", None, [("Q", 1), ("Y", 1)], (4, 5), 0),
    "W": Node("W", None, [("T", 1)], (5, 2), 0),
    "X": Node("X", None, [("Y", 1)], (5, 4), 0),
    "Y": Node("Y", None, [("V", 1), ("X", 1)], (5, 5), 0),
}


def findMin(frontier):
    minNode = None
    minCost = float("inf")
    for node, (parent, cost) in frontier.items():
        if cost < minCost:
            minNode = node
            minCost = cost
    return minNode


def actionSequence(graph, initialState, goalState):
    sequence = []
    currentNode = goalState
    while currentNode != initialState:
        parent = graph[currentNode].parent
        for action, _ in graph[parent].actions:
            if action == currentNode:
                sequence.insert(0, action)
                break
        currentNode = parent
    return sequence


def solutionAstar(graph, initialState, goalState):
    frontier = {}
    explored = {}

    heuristicCost = math.sqrt(
        (graph[goalState].heuristic[0] - graph[initialState].heuristic[0]) ** 2
        + (graph[goalState].heuristic[1] - graph[initialState].heuristic[1]) ** 2
    )
    print(round(heuristicCost,2))

    frontier[initialState] = (None, heuristicCost)

    while frontier:
        currentNode = findMin(frontier)
        currentCost = frontier[currentNode][1]
        del frontier[currentNode]

        if currentNode == goalState:
            return actionSequence(graph, initialState, goalState)

        explored[currentNode] = (graph[currentNode].parent, currentCost)

        for child, actionCost in graph[currentNode].actions:
            childCost = currentCost + actionCost
            heuristicCost = math.sqrt(
                (graph[goalState].heuristic[0] - graph[child].heuristic[0]) ** 2
                + (graph[goalState].heuristic[1] - graph[child].heuristic[1]) ** 2
            )
            print(round(heuristicCost,2))

            if child in explored:
                if (
                    graph[child].parent == currentNode
                    or child == initialState
                    or explored[child][1] <= childCost + heuristicCost
                ):
                    continue

            if child not in frontier or childCost < frontier[child][1]:
                graph[child].parent = currentNode
                frontier[child] = (graph[child].parent, childCost + heuristicCost)
                print(round(heuristicCost,2))

    return None  # No solution found



initialState = "A"
goalState = "Y"

solution = solutionAstar(graph, initialState, goalState)
print(solution)