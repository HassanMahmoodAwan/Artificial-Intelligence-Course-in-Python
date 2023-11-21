class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

def uniform_cost_search(graph, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    open_list.append(start_node)

    while open_list:
        open_list.sort(key=lambda node: node.cost)
        current_node = open_list.pop(0)

        if current_node.state == goal:
            return build_path(current_node)

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state]:
            if neighbor not in closed_set:
                child = Node(neighbor, current_node, current_node.cost + cost)
                open_list.append(child)

    return None

def build_path(node):
    path = []
    cost = []
    while node:
        path.append(node.state)
        cost.append(node.cost)
        node = node.parent
    return list(reversed(path)), list(reversed(cost))

# Example usage:
# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('A', 1), ('D', 2)],
#     'C': [('A', 4), ('D', 3)],
#     'D': [('B', 2), ('C', 3), ('E', 1)],
#     'E': [('D', 1)]
# }

graph = {
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Rimnicu': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

start_node = 'Arad'
goal_node = 'Bucharest'

result = uniform_cost_search(graph, start_node, goal_node)

if result:
    print(f"Shortest Path from {start_node} to {goal_node}: {result[0]}")
    print(f"Total Cost: {result[1]}")
else:
    print(f"No path found from {start_node} to {goal_node}")