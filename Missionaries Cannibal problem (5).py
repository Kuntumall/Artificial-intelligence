from collections import deque

def is_valid_state(m_left, c_left, m_right, c_right):
    return not (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0 or 
                (m_left > 0 and m_left < c_left) or 
                (m_right > 0 and m_right < c_right))

def get_next_states(state, boat_capacity, total_m, total_c):
    m_left, c_left, boat_pos = state
    m_right = total_m - m_left
    c_right = total_c - c_left
    next_states = []
    if boat_pos == 1:
        for m_move in range(boat_capacity + 1):
            for c_move in range(boat_capacity + 1 - m_move):
                if 1 <= m_move + c_move <= boat_capacity:
                    new_m_left = m_left - m_move
                    new_c_left = c_left - c_move
                    new_m_right = m_right + m_move
                    new_c_right = c_right + c_move
                    if is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                        next_states.append((new_m_left, new_c_left, 0))
    else:
        for m_move in range(boat_capacity + 1):
            for c_move in range(boat_capacity + 1 - m_move):
                if 1 <= m_move + c_move <= boat_capacity:
                    new_m_left = m_left + m_move
                    new_c_left = c_left + c_move
                    new_m_right = m_right - m_move
                    new_c_right = c_right - c_move
                    if is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                        next_states.append((new_m_left, new_c_left, 1))
    return next_states

def missionaries_cannibals(total_m, total_c, boat_capacity):
    start_state = (total_m, total_c, 1)
    goal_state = (0, 0, 0)
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [goal_state]
        for next_state in get_next_states(current_state, boat_capacity, total_m, total_c):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))
    return "No solution found."

if __name__ == "__main__":
    total_m = int(input("Enter the number of missionaries: "))
    total_c = int(input("Enter the number of cannibals: "))
    boat_capacity = int(input("Enter the boat's capacity: "))
    solution = missionaries_cannibals(total_m, total_c, boat_capacity)
    print("Solution Path:")
    if solution == "No solution found.":
        print(solution)
    else:
        for step in solution:
            print(step)
