def get_neighbors(state, current_cost):
    neighbors = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)
    
    moves = [(-1, 0, "UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")] 
    
    for dr, dc, direction in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            neighbor_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_idx], new_state[neighbor_idx] = new_state[neighbor_idx], new_state[blank_idx]
       
            neighbors.append((tuple(new_state), current_cost + 1, direction))      
    return neighbors

def solve_8_puzzle_dfs(start_state, goal_state, max_depth):
   
    stack = [(start_state, 0, 0, [])]
    visited = set([start_state])
    
    while stack:
        state, cost, depth, path = stack.pop()
        
        if state == goal_state:
            return cost, cost, path
            
        if depth >= max_depth:
            continue
            
        for neighbor, next_cost, direction in get_neighbors(state, cost):
            if neighbor not in visited:
                visited.add(neighbor)
               
                stack.append((neighbor, next_cost, depth + 1, path + [direction]))           
    return None, None, None

initial_board = (1, 2, 3, 0, 4, 6, 7, 5, 8)
goal_board    = (1, 2, 3, 4, 5, 6, 7, 8, 0)
max_depth = 50

total_steps, path_cost, move_sequence = solve_8_puzzle_dfs(initial_board, goal_board, max_depth)

if total_steps is not None:
    print(f"Total number of steps: {total_steps}")
    print(f"Path cost: {path_cost}")
    print(f"Sequence of transitions (Blank Space Moves): {' -> '.join(move_sequence)}")
else:
    print("No solution found within the depth limit.")

# The theoretical branching factor equation provided in your snippet
b = ((4*1) + (4*2) + (4*3)) / 9    
print("Time complexity(O(b^m))=O(", b, "^", max_depth, ")")    
print("NAME:ANEESH HEBBAR")
print("USN:1WN24CS038")
 

