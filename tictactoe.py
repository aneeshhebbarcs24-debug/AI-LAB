board = [" "] * 9
total_cost = 0

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6,7,8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

def path_cost(move):
    costs = {
        0: 2, 1: 3, 2: 2,
        3: 3, 4: 1, 5: 3,
        6: 2, 7: 3, 8: 2
    }
    return costs[move]

def ai_move():
    global total_cost

    available = [i for i in range(9) if board[i] == " "]
    best_move = min(available, key=path_cost)

    board[best_move] = "O"
    total_cost += path_cost(best_move)

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Choose a number from 1 to 9.")
            elif board[move] != " ":
                print("That position is already occupied.")
            else:
                board[move] = "X"
                break

        except ValueError:
            print("Enter a valid number.")

def game():
    print("TIC-TAC-TOE")
    print("You = X, AI = O")

    for turn in range(9):
        display()

        if turn % 2 == 0:
            player_move()

            if check_winner("X"):
                display()
                print("You win!")
                break

        else:
            ai_move()

            if check_winner("O"):
                display()
                print("AI wins!")
                break

    else:
        display()
        print("It's a draw!")

    print("Total Path Cost:", total_cost)

game()