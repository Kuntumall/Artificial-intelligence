import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.board.index(0)
        self.cost = self.moves + self.manhattan_distance()

    def __lt__(self, other):
        return self.cost < other.cost

    def manhattan_distance(self):
        distance = 0
        for i, value in enumerate(self.board):
            if value != 0:
                target_row, target_col = divmod(value - 1, 3)
                current_row, current_col = divmod(i, 3)
                distance += abs(target_row - current_row) + abs(target_col - current_col)
        return distance

    def neighbors(self):
        neighbors = []
        row, col = divmod(self.blank_pos, 3)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_pos = new_row * 3 + new_col
                new_board = self.board[:]
                new_board[self.blank_pos], new_board[new_pos] = new_board[new_pos], new_board[self.blank_pos]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __str__(self):
        return "\n".join([" ".join(map(str, self.board[i:i + 3])) for i in range(0, 9, 3)])


def solve_puzzle(initial_board):
    initial_state = PuzzleState(initial_board)
    priority_queue = []
    heapq.heappush(priority_queue, initial_state)
    visited = set()

    while priority_queue:
        current_state = heapq.heappop(priority_queue)
        if current_state.is_goal():
            return current_state
        visited.add(tuple(current_state.board))
        for neighbor in current_state.neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(priority_queue, neighbor)
    return None


def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.previous
    path.reverse()
    for step in path:
        print(step)
        print()
    print(f"Total cost : {len(path) - 1}")


if __name__ == "__main__":
    initial_board = []

    for i in range(3):
        try:
            row = input(f"Enter row {i + 1} (space-separated): ").strip().split()
            if len(row) != 3:
                raise ValueError("Each row must contain exactly 3 numbers.")
            initial_board.extend(map(int, row))
        except ValueError as e:
            print(f"Invalid input: {e}")
            exit()

    if len(initial_board) != 9 or set(initial_board) != set(range(9)):
        print("Invalid input. Please enter numbers 0 to 8 exactly once.")
    else:
        solution = solve_puzzle(initial_board)
        if solution:
            print("Solution found!")
            print_solution(solution)
        else:
            print("No solution exists.")
