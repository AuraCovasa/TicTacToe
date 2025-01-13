import random


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("\nCurrent board: ")
    for row in board:
        print(" | ".join(str(cell) for cell in row))
        print("-" * 9)  # Separator between rows


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("Enter you move (between 1 and 9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9")
                continue

            row = (move - 1) // 3
            column = (move - 1) % 3
            if board[row][column] in ['X', 'O']:
                print("That square is already occupied. Choose another. ")
            else:
                board[row][column] = '0'
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):
                free_fields.append((i, j))

    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    # Check rows, columns and diagonals

    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):  # Checks diagonals
        return True

    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        # Get a random index from the range of available free fields
        random_index = random.randrange(len(free_fields))
        row, col = free_fields[random_index]  # Access the row and column using the random index
        board[row][col] = 'X'  # Place 'X' on the board


def main():
    # Initialize the board with numbers from 1 to 9
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Computer's first move
    board[1][1] = 'X'  # Place 'X' in the middle
    display_board(board)

    while True:
        enter_move(board)
        if victory_for(board, '0'):
            print("Congratulations! You won!!!")
            break
        if victory_for(board, 'X'):
            print("Computer wins! Better luck next time.")
            break
        display_board(board)

        if not make_list_of_free_fields(board):
            # Check for tie befoew computer's move
            print("It's a tie!")
            break

        draw_move(board)
        if victory_for(board, '0'):
            print("Congratulations! You won!!!")
            break
        if victory_for(board, 'X'):
            print("Computer wins! Better luck next time.")
            break
        display_board(board)


        if not make_list_of_free_fields(board):  # Check for tie befoew computer's move
            print("It's a tie!")
            break


if __name__ == "__main__":
    main()






