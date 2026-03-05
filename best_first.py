import numpy as np
import heapq as pq

initial = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

initial_tuple = tuple(initial.flatten())
final_tuple = tuple(final.flatten())

MOVES = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

def misplaced_tiles(current_tuple, final_tuple):
    h_mt = sum(1 for a, b in zip(current_tuple, final_tuple) if a != b and a != 0)
    return h_mt

def manhattan_distance(current_tuple, final_tuple):
    h_md = 0
    goal_map = {val: divmod(idx, 3) for idx, val in enumerate(final_tuple)}
    for i, value in enumerate(current_tuple):
        if value != 0:
            row, col = divmod(i, 3)
            goal_row, goal_col = goal_map[value]
            h_md += abs(row - goal_row) + abs(col - goal_col)
    return h_md

def solve_greedy(initial_tuple, final_tuple, choice):
    if choice == '1':
        h_start = manhattan_distance(initial_tuple, final_tuple)
    else:
        h_start = misplaced_tiles(initial_tuple, final_tuple)

    queue = [(h_start, initial_tuple)]
    visited = {initial_tuple}
    parent_map = {initial_tuple: None}
    nodes_explored = 0
    while queue:
        h_current, current_tuple = pq.heappop(queue)
        nodes_explored += 1

        if current_tuple == final_tuple:
            path = []
            state = current_tuple
            while state is not None:
                path.append(state)
                state = parent_map[state]
            return path[::-1], nodes_explored

        blank_pos = current_tuple.index(0)

        print(f"\nCurrent State (H-Cost: {h_current}):")
        print(np.array(current_tuple).reshape(3, 3))
        print("Possible moves from this state:")

        for move in MOVES[blank_pos]:
            neighbor = list(current_tuple)
            neighbor[blank_pos], neighbor[move] = neighbor[move], neighbor[blank_pos]
            neighbor_tuple = tuple(neighbor)

            if choice == '1':
                h_neighbor = manhattan_distance(neighbor_tuple, final_tuple)
            else:
                h_neighbor = misplaced_tiles(neighbor_tuple, final_tuple)

            if neighbor_tuple not in visited:
                print(f"-> Move tile {current_tuple[move]}: New H-Cost = {h_neighbor}")
                visited.add(neighbor_tuple)
                parent_map[neighbor_tuple] = current_tuple
                pq.heappush(queue, (h_neighbor, neighbor_tuple))
            else:
                print(f"-> Move tile {current_tuple[move]}: New H-Cost = {h_neighbor} (Already Visited)")

    return None, nodes_explored

print("Experiment 3: Best First Search (Greedy)")
print("1. Manhattan distance")
print("2. Misplaced tiles")
user_choice = input("Select which heuristic to use (1 or 2): ")

if user_choice not in ['1', '2']:
    print("Invalid input. Defaulting to Manhattan Distance.")
    user_choice = '1'

final_path, total_explored = solve_greedy(initial_tuple, final_tuple, user_choice)

print("\n" + "="*30)
print("FINAL SOLUTION PATH")
print("="*30)
for i, step in enumerate(final_path):
    if user_choice == '1':
        h_val = manhattan_distance(step, final_tuple)
    else:
        h_val = misplaced_tiles(step, final_tuple)

    print(f"Step {i} (Selected Heuristic Cost: {h_val})")
    print(np.array(step).reshape(3, 3))
    print()

print(f"Total nodes explored during search: {total_explored}")
print(f"Total moves in final path: {len(final_path) - 1}")
