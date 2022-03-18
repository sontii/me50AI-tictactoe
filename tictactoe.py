"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math


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
    #raise NotImplementedError

    # count X and O cells
    XCell = 0
    OCell = 0
    for i in board:
        for j in i:
            if j == X :
                XCell += 1
            elif j == O:
                OCell += 1
    
    # if only empty then X; if equal X and O still X
    if (XCell + OCell) == 0:
        return X
    elif XCell == OCell:
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError

    possible_moves = set()
    for indexi, i in enumerate(board):
        for indexj, j in enumerate(i):
            if j == None:
                possible_moves.add((indexi, indexj))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError

    modified_board = deepcopy(board)
  
    if modified_board[action[0]][action[1]] != EMPTY:
        raise Exception('Not valid move!')
    else:
        modified_board[action[0]][action[1]] = player(board)
    
    return modified_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    
    # row check  
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
    
    # colummn check
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # diagonal up to down check
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
        
    # diagonal down to up check
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError

    #empty cell count
    emptycell = 0

    #loop checking remaining empty cell
    for i in board:
        for j in i:
            if j == EMPTY:
                emptycell += 1
    
    # in no remaining empty cell = True
    if emptycell == 0 or winner(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    
    if terminal(board):
        return None

    elif player(board) == X:
        optimal_move = None
        value = -math.inf

        for action in actions(board):
            minimize_value = minimize(result(board, action))

            if minimize_value > value:
                value =  minimize_value
                optimal_move = action

        return optimal_move
        
    elif player(board) == O:
        optimal_move = None
        value = math.inf

        for action in actions(board):
            maximize_value = maximize(result(board, action))

            if maximize_value < value:
                value = maximize_value
                optimal_move = action
  
        return optimal_move


def maximize(board):
    """
    Returns max value of minimize.
    """
    if terminal(board):
        return utility(board)

    value = -math.inf

    for action in actions(board):
        value = max(value, minimize(result(board, action)))
    return value


def minimize(board):
    """
    Returns min value of maximize.
    """
    if terminal(board):
        return utility(board)

    value = math.inf

    for action in actions(board):
        value = min(value, maximize(result(board, action)))
    return value
