# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:00:29 2016

@author: Ajinkya
"""
import board
#import numpy as np
import math
import copy



'''
parent
parent node

children
children nodes

value
value of the min or max node

board
holds a instance of board

type 
min or max

'''

class Node:

    # type = bool
    def __init__(self, type, board):
        self.parent = None
        self.child = None
        self.type = type
        if type:
            self.value = float('inf')
        else:
            self.value = float('-inf')
        self.state = board



def expand(frontier):
    current = frontier.pop()
    moves = current.generate_moves()
    for move in moves:
        current.board.make_move(move)
        child_to_current = copy.deepcopy(current)
        child_to_current.parent = current
        if child_to_current.type:
            child_to_current.type = False
            child_to_current.value = float('-inf')
        else:
            child_to_current.type = False
            child_to_current.value = float('inf')
        frontier.insert(0, child_to_current)
    return frontier





def minimax(b,depth):
    frontier = []
    pass
    


def minimax_root(b,depth):
    pass



def find_win(b,depth):
    pass



def alphabeta_minimax(b,depth,a,be):
    pass
    
def negamax_root_alphabeta(b, depth):
    pass





