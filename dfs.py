import numpy as np

initial = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
final = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

initial_tuple = tuple(initial.flatten())
final_tuple = tuple(final.flatten())

MOVES = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

def get_direction(old_idx, new_idx):
    diff = new_idx - old_idx
    if diff == 1: return "Right"
    if diff == -1: return "Left"
    if diff == 3: return "Down"
    if diff == -3: return "Up"
    return ""

def solve_dls(start, goal, limit):
    stack = [(start, [("Initial State", start)], 0)]
    visited = {start: 0}

    while stack:
        current_state, path, depth = stack.pop()

        if current_state == goal:
            return path

        if depth < limit:
            blank_idx = current_state.index(0)

            for move_to in MOVES[blank_idx]:
                new_state = list(current_state)
                new_state[blank_idx], new_state[move_to] = new_state[move_to], new_state[blank_idx]
                new_state_tuple = tuple(new_state)

                if new_state_tuple not in visited or depth + 1 < visited[new_state_tuple]:
                    visited[new_state_tuple] = depth + 1
                    direction = get_direction(blank_idx, move_to)
                    stack.append((new_state_tuple, path + [(direction, new_state_tuple)], depth + 1))

    return None

depth_limit = 10
print(f"Searching for solution using DLS (Limit: {depth_limit})...")
solution_path = solve_dls(initial_tuple, final_tuple, depth_limit)

if solution_path:
    print(f"Goal reached! Total moves: {len(solution_path) - 1}\n")
    for i, (direction, state) in enumerate(solution_path):
        if i == 0:
            print(f"Step {i}: {direction}")
        else:
            print(f"Step {i}: Move {direction}")
        print(np.array(state).reshape(3, 3))
        print("-" * 15)
else:
    print(f"No solution found within depth limit {depth_limit}.")

