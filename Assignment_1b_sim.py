
import heapq

# Input
n = int(input("Enter N: "))

start = []
for i in range(n):
    start += list(map(int, input().split()))

start = tuple(start)
goal = tuple(list(range(1, n*n)) + [0])


# Manhattan Distance
def heuristic(state):
    h = 0

    for i, tile in enumerate(state):
        if tile != 0:
            j = goal.index(tile)
            h += abs(i//n - j//n) + abs(i%n - j%n)

    return h


# Generate Neighbors
def neighbors(state):
    zero = state.index(0)
    r, c = zero//n, zero%n

    result = []

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r+dr, c+dc

        if 0 <= nr < n and 0 <= nc < n:
            new = list(state)
            pos = nr*n + nc

            new[zero], new[pos] = new[pos], new[zero]
            result.append(tuple(new))

    return result


# A* Algorithm
def astar(start, goal):

    pq = [(heuristic(start), 0, start)]
    cost = {start: 0}
    parent = {start: None}
    expanded = 0

    while pq:

        f, g, current = heapq.heappop(pq)
        expanded += 1

        if current == goal:

            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], expanded

        for next_state in neighbors(current):

            new_g = g + 1

            if new_g < cost.get(next_state, float('inf')):

                cost[next_state] = new_g
                parent[next_state] = current

                h = heuristic(next_state)
                heapq.heappush(pq, (new_g+h, new_g, next_state))

    return None, expanded


# Main
path, expanded = astar(start, goal)

if path:

    print("Minimum moves:", len(path)-1)

    for step, state in enumerate(path):

        print("\nStep:", step)

        for i in range(0, n*n, n):
            print(state[i:i+n])

        g = step
        h = heuristic(state)
        print("g =", g, "h =", h, "f =", g+h)

    print("Nodes expanded:", expanded)

else:
    print("No solution found")
