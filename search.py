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
    def __init__(self, isMaxNode, board):
        self.parent = None
        self.child = None
        self.isMaxNode = isMaxNode
        self.depth = 0
        self.board = board

        if isMaxNode:
            self.value = float('inf')
        else:
            self.value = float('-inf')

    def get_grandparents_value(self):
        if self.parent != None:
            if self.parent.parent != None:
                return self.parent.parent.value
            # checks type of node. if max returns -inf else inf
        elif self.isMaxNode: # if self.type == true this is a max node
            float("-inf")
        else:
            float("inf")


    '''
        createChild: Creates a child and self and makes sure the parent and child pointers are aligned correctly
       @return a new Node that is the child of self 
    '''
    def createChild(self):
        child = copy.deepcopy(self)
        child.parent = self
        self.child = child
        return child



def expand(frontier):
    current = frontier.pop()
    moves = current.generate_moves()
    for move in moves:
        child = current.creatChild()
        child.board.make_move(move)
        if child.type:     ############
            child.type = False
            child.value = float('-inf')  ######change this for get value of grandparent
        else:
            child.type = False
            child.value = float('inf') ############
        frontier.insert(0, child)
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





