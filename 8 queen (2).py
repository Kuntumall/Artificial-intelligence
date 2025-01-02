def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append(["".join("Q" if cell else "." for cell in row) for row in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_n_queens_problem(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

if __name__ == "__main__":
    try:
        n = int(input("Enter the board size (n x n): "))
        if n < 4:
            print("The 8-Queen problem requires a board of at least 4x4.")
        else:
            solutions = solve_n_queens_problem(n)
            print(f"Total solutions for {n}-Queens problem: {len(solutions)}\n")
            for idx, solution in enumerate(solutions, 1):
                print(f"Solution {idx}:")
                for row in solution:
                    print(row)
                print()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
