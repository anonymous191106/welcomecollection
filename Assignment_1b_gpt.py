#Assignment-1B
import heapq

# Take board size
n = int(input("Enter board size N: "))

if n < 2:
    raise ValueError("Board size must be at least 2")

# Take initial board
start = []

print("Enter initial board row by row:")

for i in range(n):
    row = list(map(int, input().split()))

    if len(row) != n:
        raise ValueError("Each row must contain N numbers")

    start.extend(row)

start = tuple(start)

# Generate goal state
goal = tuple(list(range(1, n*n)) + [0])

# Validate board
if sorted(start) != list(range(n*n)):
    raise ValueError("Invalid board! Enter numbers 0 to N*N-1 once.")


# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            j = goal.index(tile)

            distance += abs(i // n - j // n)
            distance += abs(i % n - j % n)

    return distance


# Check solvability
def solvable(state):

    arr = [x for x in state if x != 0]

    inversions = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1

    if n % 2 == 1:
        return inversions % 2 == 0

    blank_row = n - state.index(0) // n
    return (inversions + blank_row) % 2 == 1


# Generate neighboring states
def get_neighbors(state):

    zero = state.index(0)
    row, col = zero // n, zero % n

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < n and 0 <= c < n:

            new_pos = r * n + c

            board = list(state)
            board[zero], board[new_pos] = board[new_pos], board[zero]

            neighbors.append(tuple(board))

    return neighbors


# A* Search Algorithm
def astar(start, goal):

    pq = [(heuristic(start), 0, start)] #(f,g,state) 

    cost = {start: 0}
    parent = {start: None}

    expanded = 0

    while pq:

        f, g, current = heapq.heappop(pq)

        if g != cost[current]:
            continue

        expanded += 1

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], expanded

        for neighbor in get_neighbors(current):

            new_cost = g + 1

            if new_cost < cost.get(neighbor, float('inf')):

                cost[neighbor] = new_cost
                parent[neighbor] = current

                h = heuristic(neighbor)

                heapq.heappush(
                    pq, (new_cost + h, new_cost, neighbor)
                )

    return None, expanded


# Main program
if start == goal:

    print("Puzzle is already solved!")

elif not solvable(start):

    print("Puzzle is not solvable!")

else:

    path, expanded = astar(start, goal)

    if path:

        print("\nSolution found!")
        print("Minimum moves:", len(path) - 1)

        for step, state in enumerate(path):

            print("\nStep", step)

            for i in range(0, n*n, n):
                print(state[i:i+n])

            g = step
            h = heuristic(state)
            f = g + h

            print("g =", g, "h =", h, "f =", f)

        print("\nNodes expanded:", expanded)

    else:
        print("No solution found!")
