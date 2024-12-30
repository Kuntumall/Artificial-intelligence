def print_board(board):
    print("\n")
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=" | " if col < 2 else "")
        print("\n" + "-" * 5)

def check_winner(board, player):
    
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all([board[row][col] != ' ' for row in range(3) for col in range(3)])

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  
    while True:
        print_board(board)
        
        print(f"Player {current_player}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
            if board[row][col] != ' ':
                print("Cell is already occupied. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")
            continue
        board[row][col] = current_player
       
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    tic_tac_toe()
