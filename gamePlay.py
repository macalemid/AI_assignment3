import sys
#import time
#import getopt
import board as BOARD

from copy import deepcopy

def opponent(x):
    """ Given a string representing a color (must be either "B" or "W"),
    return the opposing color """ 
    if x == "red" or x == "Red":
        return "Blue"
    elif x == "blue" or x == "Blue":
        return "Red"
    else:
        return "."
    

def valid(b, move):
    """ Given a board, a string
    representing the player, and a number representing the position,
    return true if the position is a valid
    move """
    return validPos(move) and b.state[5][move] == 0


def validPos(x):
    """ Returns true if the position is within the board column space"""
    return x >= 0 and x <= 6


def doMove(board, pos):
    """ Given a 2D array representing a board and a position,
    implement the move on the board. """
    if valid(board, pos):
        board.make_move(pos)

def printBoard(board):
    """ Prints a board, using "R" for red pieces and "B" for blue pieces"""
    print(board.board)

def gameOver(board):
    return board.last_move_won() 

def playGame(p1, p2):
    """ Takes as input two functions p1 and p2 (each of which
    calculates a next move given a board and player color),
    and returns either a tuple containing the score for black,
    score for white, and final board (for a normal game ending)
    or a tuple containing the final score for black, final score
    for white, and the invalid move (for a game that ends with
    and invalid move """ 
    board = p1.b
    players = (p1, p2)
    while not gameOver(board):   
        print(board)
        tmpBoard = deepcopy(board)
        move = players[0].get_move()
        if (move[0] == -1):
            winner = players[1].name
            print(winner + " forced a win!")
            return
        elif (move[0] == 1):
            winner = players[0].name
            print(winner + " forced a win")
            return
        elif valid(board, move[1]):
            players[0].make_move(move[1])
        else:
            print(board)
            print("Bad Move")
            print(str(move))
            return 
        players = (players[1], players[0])
    print("Game Over!")
    winner = players[1].name
    print(winner + " won.")
    print("Final Board:")
    return board

if __name__ == "__main__":
    exec("import " + sys.argv[1] + " as p1")
    exec("import " + sys.argv[2] + " as p2")
    board = BOARD.Board()
    player1 = p1.Player(board)
    player2 = p2.Player(board)
    playGame(player1, player2)
