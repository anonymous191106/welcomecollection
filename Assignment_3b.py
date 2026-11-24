#Graph 
graph = {
    "Maharashtra": ["Gujarat", "Madhya Pradesh", "Goa",
                    "Karnataka", "Telangana", "Chhattisgarh"],

    "Gujarat": ["Maharashtra", "Madhya Pradesh", "Rajasthan"],

    "Madhya Pradesh": ["Gujarat", "Maharashtra",
                       "Rajasthan", "Chhattisgarh"],

    "Rajasthan": ["Gujarat", "Madhya Pradesh"],

    "Goa": ["Maharashtra", "Karnataka"],

    "Karnataka": ["Goa", "Maharashtra", "Telangana"],

    "Telangana": ["Maharashtra", "Karnataka", "Chhattisgarh"],

    "Chhattisgarh": ["Maharashtra", "Madhya Pradesh", "Telangana"]
}
states = list(graph.keys())
print(states)
colors = ["Red","Green","Blue","Yellow"]
assignment = {}

def isSafe(color,state, assignment, graph):
    for neighbor in graph[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False

    return True

def backtrack(colors,states,assignment,graph):
    if len(assignment)==len(graph):
        return True
    for state in states:
        if state not in assignment:
            break
    for color in colors:
        if isSafe(color, state, assignment, graph):
            assignment[state]=color
            if backtrack(colors,states,assignment,graph):
                return True
            del assignment[state]
    return False

#Main Program:
if backtrack(colors,states,assignment,graph):
    print("Map coloring Solution: ")
    for state in states:
        print(state, ":", assignment[state])
else:
    print("No valid coloring possible")