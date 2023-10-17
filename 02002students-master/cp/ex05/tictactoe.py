"""Exercise 5.12-5-16. TicTacToe."""


def get_game_state(board: list) -> str:
    """Check if a player has won the game, if it's a draw, or if it's ongoing.

    :param board: List of lists of strings representing the game board.
    :return: A string which is 'X' if player 'X' won, 'O' if player 'O' has won, 'Draw' if the game is a draw, or '-' if the game is ongoing.
    """
    # TODO: Code has been removed from here.
    x = ["-"]
    first_row = board[0]
    second_row = board[1]
    third_row = board[2]
    first_col = [board[0][0], board[1][0], board[2][0]]
    second_col = [board[0][1], board[1][1], board[2][1]]
    third_col = [board[0][2], board[1][2], board[2][2]]
    first_diag = [board[0][0], board[1][1], board[2][2]]
    second_diag = [board[2][0], board[1][1], board[0][2]]
    if (
        x[0] not in first_row
        and x[0] not in second_row
        and x[0] not in third_row
        and x[0] not in first_col
        and x[0] not in second_col
        and x[0] not in third_col
        and x[0] not in first_diag
        and x[0] not in second_diag
    ):
        return "Draw"
    elif (
        first_row[0] == first_row[1]
        and first_row[1] == first_row[2]
        and x[0] not in first_row
    ):
        return first_row[0]
    elif (
        second_row[0] == second_row[1]
        and second_row[1] == second_row[2]
        and x[0] not in second_row
    ):
        return second_row[0]
    elif (
        third_row[0] == third_row[1]
        and third_row[0] == third_row[2]
        and x[0] not in third_row
    ):
        return third_row[0]
    elif (
        first_col[0] == first_col[1]
        and first_col[1] == first_col[2]
        and x[0] not in first_col
    ):
        return first_col[0]
    elif (
        second_col[0] == second_col[1]
        and second_col[1] == second_col[2]
        and x[0] not in second_col
    ):
        return second_col[0]
    elif (
        third_col[0] == third_col[1]
        and third_col[1] == third_col[2]
        and x[0] not in third_col
    ):
        return third_col[0]
    elif (
        first_diag[0] == first_diag[1]
        and first_diag[1] == first_diag[2]
        and x[0] not in first_diag
    ):
        return first_diag[0]
    elif (
        second_diag[0] == second_diag[1]
        and second_diag[1] == second_diag[2]
        and x[0] not in second_diag
    ):
        return second_diag[0]
    else:
        return "-"


def update_board(board: list, player: str, position: list) -> list:
    """Update the game board with the player's move.

    :param board: List of lists of strings representing the game board.
    :param player: Player making the move ('X' or 'O').
    :param position: List containing two integer indices [row, column] indicating the position to make a move.
    :return: Updated game board after the move.
    """
    # TODO: Code has been removed from here.
    updated_board = board
    if board[position[0]][position[1]] == "-":
        updated_board[position[0]][position[1]] = player
    else:
        print("Invalid move!")
    return updated_board


def print_board(board: list):
    """Print the current state of the game board.

    :param board: List of lists of strings representing the game board.
    """
    # TODO: Code has been removed from here.
    first_line = board[0]
    second_line = board[1]
    third_line = board[2]

    print(
        f"{first_line[0]}{first_line[1]}{first_line[2]}\n"
        f"{second_line[0]}{second_line[1]}{second_line[2]}\n"
        f"{third_line[0]}{third_line[1]}{third_line[2]}"
    )


def tictactoe(board: list, player: str, position: list) -> list:
    """Play a move in the Tic-Tac-Toe game and determine the winner.

    :param board: List of lists of strings representing the game board.
    :param player: Player making the move ('X' or 'O').
    :param position: List containing two integer indices [row, column] indicating the position to make a move.
    :return: Updated game board after the move.
    """
    # TODO: Code has been removed from here.
    while True:
        print_board(update_board(board, player, position))
        if get_game_state(board) == "X" or get_game_state(board) == "O":
            print(f"Player {get_game_state(board)} won!")
            break

    return board


if __name__ == "__main__":
    tictactoe([["X", "X", "-"], ["-", "O", "-"], ["O", "-", "-"]], "O", [0, 2])
