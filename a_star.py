import numpy as np
import heapq as pq

initial = np.array([[8, 5, 0], [3, 7, 1], [2, 6, 4]])
final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

initial_tuple = tuple(initial.flatten())
final_tuple = tuple(final.flatten())

MOVES = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

def get_h(state, goal, choice):
    if choice == '2':
        return sum(1 for a, b in zip(state, goal) if a != b and a != 0)
    else:
        dist = 0
        goal_map = {val: divmod(idx, 3) for idx, val in enumerate(goal)}
        for i, val in enumerate(state):
            if val != 0:
                r, c = divmod(i, 3)
                gr, gc = goal_map[val]
                dist += abs(r - gr) + abs(c - gc)
        return dist

def solve_astar(initial_tuple, final_tuple, choice):
    h_start = get_h(initial_tuple, final_tuple, choice)
    queue = [(h_start, 0, initial_tuple)]

    visited = {initial_tuple: 0}
    parent_map = {initial_tuple: None}
    nodes_explored = 0

    while queue:
        f_curr, g_curr, current_tuple = pq.heappop(queue)
        nodes_explored += 1

        if current_tuple == final_tuple:
            path = []
            while current_tuple is not None:
                path.append(current_tuple)
                current_tuple = parent_map[current_tuple]
            return path[::-1], nodes_explored

        blank_pos = current_tuple.index(0)
        for move in MOVES[blank_pos]:
            neighbor = list(current_tuple)
            neighbor[blank_pos], neighbor[move] = neighbor[move], neighbor[blank_pos]
            neighbor_tuple = tuple(neighbor)

            new_g = g_curr + 1

            if neighbor_tuple not in visited or new_g < visited[neighbor_tuple]:
                visited[neighbor_tuple] = new_g
                h_next = get_h(neighbor_tuple, final_tuple, choice)
                f_next = new_g + h_next
                parent_map[neighbor_tuple] = current_tuple
                pq.heappush(queue, (f_next, new_g, neighbor_tuple))

    return None, nodes_explored

choice = input("Select Heuristic (1: Manhattan, 2: Misplaced): ")
path, explored = solve_astar(initial_tuple, final_tuple, choice)

print(f"\nSolved in {len(path)-1} moves. Nodes explored: {explored}")
for i, state in enumerate(path):
    print(f"Step {i}:")
    print(np.array(state).reshape(3, 3))
