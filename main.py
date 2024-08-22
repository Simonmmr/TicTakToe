# Initialize the board with numbers 1 to 16
board = [str(num) for num in range(1, 17)]


def print_board():
    for num in range(0, 16, 4):
        print(f" {board[num]} | {board[num + 1]} | {board[num + 2]} | {board[num + 3]} ")
        if num < 12:
            print("-----------------")


def check_winner(player):
    winning_condition = [
        (0, 1, 2, 3), (4, 5, 6, 7),
        (8, 9, 10, 11), (12, 13, 14, 15),  # Horizontal wins
        (0, 4, 8, 12), (1, 5, 9, 13),
        (2, 6, 10, 14), (3, 7, 11, 15),  # Vertical wins
        (0, 5, 10, 15), (3, 6, 9, 12)  # Diagonal wins
    ]

    for condition in winning_condition:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == board[condition[3]] == player:
            return True
    return False


def play_game():
    current_player = "🔯"
    while any(space.isdigit() for space in board):  # Check if any moves are left
        print_board()
        try:
            move = int(input(f"Player '{current_player}', enter the number 1 to 16 to move: ")) - 1
            if move < 0 or move > 15:
                print("Invalid move. Please enter a number between 1 and 16.")
                continue
            if board[move] in ['🔯', '💀']:
                print("This spot is already taken. Please choose another spot.")
                continue
            board[move] = current_player
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = '💀' if current_player == '🔯' else '🔯'
        except ValueError:
            print("Invalid input. Please enter a number.")

    print_board()
    print("It's a draw!")


play_game()
