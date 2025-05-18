"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player_dict = {
        X: 0,
        O: 0,
        EMPTY: 0
    }

    for row in board:
        for col in row:
            player_dict[col] += 1

    if player_dict[X] < player_dict[O]:
        return X
    elif player_dict[O] < player_dict[X]:
        return O
    else: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_action = set()

    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            if board[i][j] == EMPTY:
                possible_action.add((i, j))

    return possible_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise RuntimeError("Invalid action")

    copy_of_board = copy.deepcopy(board)
    current_player = player(board)

    copy_of_board[action[0]][action[1]] = current_player
    return copy_of_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i, row in enumerate(board):
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

        X_amount_in_col = 0
        O_amount_in_col = 0
        for j in range(3):
            if board[j][i] == X:
                X_amount_in_col += 1
            elif board[j][i] == O:
                O_amount_in_col += 1

        if X_amount_in_col == 3:
            return X
        elif O_amount_in_col == 3:
            return O

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    has_winner = winner(board)
    possible_actions = actions(board)

    if (has_winner or len(possible_actions) == 0):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player_winner = winner(board)

    if (player_winner == X):
        return 1
    elif (player_winner == O):
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return None
    
    _, best_action = minimax_value(board)
    return best_action


def minimax_value(board):
    if terminal(board):
        return utility(board), None

    current_player = player(board)

    if current_player == X:
        best_value = float('-inf')
        best_action = None

        for action in actions(board):
            value, _ = minimax_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action

        return best_value, best_action

    else:
        best_value = float('inf')
        best_action = None

        for action in actions(board):
            value, _ = minimax_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

        return best_value, best_action