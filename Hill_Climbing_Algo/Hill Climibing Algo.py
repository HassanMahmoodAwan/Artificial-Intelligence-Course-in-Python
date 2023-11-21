import math

class Node:
    def __init__(self, state, parent, actions, heuristic, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.heuristic = heuristic  # Euclidean Distance.
        self.totalCost = totalCost

# Define the get_neighbors, value, and state functions specific to your problem

def get_neighbors(node):
    return [graph[action[0]] for action in node.actions]

def value(node):
    return node.heuristic

def state(node):
    return node.state

# Hill Climbing Algorithm Function
def hill_climbing(graph, initial_state, goal_state):
    current = graph[initial_state]

    while current.state != goal_state:
        neighbors = get_neighbors(current)

        if not neighbors:
            return None  # No solution found

        # Find the neighbor with the highest heuristic value
        neighbor = max(neighbors, key=lambda node: value(node))

        if value(neighbor) <= value(current):
            return None  # Local maximum reached

        current = neighbor

    return current.state

if __name__ == "__main__":
    # Define your graph based on the provided nodes and actions
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

    initial_state = "A"
    goal_state = "Y"

    solution = hill_climbing(graph, initial_state, goal_state)

    if solution is not None:
        print("Solution found:", solution)
    else:
        print("No solution found or local maximum reached.")