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
    xcount = 0;
    ocount = 0;

    #check whether game is over
    if terminal(board):
        return "-1"

    #if game is not over, check the number of moves completed
    for row in board:
        for square in row:
            if square == X:
                xcount += 1
            elif square == O:
                ocount += 1

    #if x and o have had same number of moves, it is x's turn
    if xcount == ocount:
        return X

    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # checking whether game is over
    if terminal(board):
        return -1

    # set to store all possible actions
    action = set()

    for i in [0,1,2]:
        for j in [0,1,2]:
            if board[i][j] == EMPTY:
                tup = (i,j)
                action.add(tup)

    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    # checking whether the action is valid
    if board[i][j] != EMPTY:
        raise NameError('Invalid Action')

    # getting the current player
    playernow = player(board)

    # creating a copy of the board to preserve the original board
    boardcopy = copy.deepcopy(board)

    # updating the copied board with action
    boardcopy[i][j] = playernow

    return boardcopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check whether the game has been won
    if winner(board) != None:
        return True

    # check whether the game is in progress
    for row in board:
        for square in row:
            if square == EMPTY:
                return False
    # if game has not been won and the game is not in progress, the game has been drawn
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    if winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # base condition
    if terminal(board):
        return None

    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

