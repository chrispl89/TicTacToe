def init_board():
    return [" " for _ in range(9)]


def show_board(board):
    print("-------------")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
        print("-------------")


board = init_board()


def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)


def is_board_full(board):
    return " " not in board


def player_move(board, player):
    move = int(input(f"Enter your move (1-9) for {player}: ")) - 1
    if board[move] == " ":
        board[move] = player
    else:
        print("This space is already occupied!")
        player_move(board, player)


def minimax(board, is_maximizing):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def ai_move(board):
    best_score = -float("inf")
    best_move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"


def main():
    board = init_board()
    while True:
        show_board(board)
        if is_winner(board, "X"):
            print("X wins!")
            break
        elif is_winner(board, "O"):
            print("O wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        player_move(board, "X")
        if is_board_full(board) or is_winner(board, "X"):
            continue

        ai_move(board)


if __name__ == "__main__":
    main()
