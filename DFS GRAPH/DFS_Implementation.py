graph = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}



def dfs(graph, start, end):
    visited = []
    stack = [start]
    found = False

    while stack:
        node = stack.pop()

        if node == end:
            found = True
            visited.append(node)
            break

        if node not in visited:
            visited.append(node)

            # Reverse the order to maintain the same order as the stack
            neighbors = reversed(graph.get(node, []))

            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

    if found:
        print("Path from", start, "to", end, ":", visited)
    else:
        print("No path found from", start, "to", end)

# Example usage:
start_node = 'Arad'
end_node = 'Bucharest'
print("DFS Path:")
dfs(graph, start_node, end_node)