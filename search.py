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
            self.value = float('-inf')
        else:
            self.value = float('inf')

    # takes nothing, returns nothing.
    # if there is a granparent, self.value is changed to that of its grandparent.
    # if there is not a grandparent, then self.value is set to either inf or -inf depending on whether or not it is max, or min
    def get_grandparents_value(self): #
        if self.parent != None: # checks if the parent is not null
            if self.parent.parent != None: # checks if the grandparent (parent of parent) is not null
               self.value = self.parent.parent.value # changes self.value to that of its grandparent

            elif self.isMaxNode:  # checks if node is max
                self.value = float("-inf")  # changes node's value to be -infinity

            else:
                self.value = float("inf")  # changes node's value to be infinity

        elif self.isMaxNode: # checks if node is max
            self.value = float("-inf") # changes node's value to be -infinity

        else:
            self.value =float("inf") # changes node's value to be infinity



    '''
        createChild: Creates a child and self and makes sure the parent and child pointers are aligned correctly
       @return a new Node that is the child of self 
    '''
    def createChild(self):
        child = copy.deepcopy(self)
        child.parent = self
        self.child = child
        child.depth = self.depth + 1
        if child.isMaxNode:
            child.isMaxNode = False
        else:
            child.isMaxNode = True
        return child

    # return None. input None
    # looks at the child node.
    # if the value of the child node is better the parent nodes value is updated to be the child's
    def update_value(self):
        if self.child is not None:
            if self.isMaxNode:   # if this node is a max node
              if self.child.value > self.value: # if the value of child is greater
                 self.value = self.child.value # update the height to be that of child's
            elif self.child.value < self.value: # if this node is a min node and the value of child's is less
             self.value = self.child.value # this nodes value is updated to be that of child's




def expand(frontier):
    current = frontier.pop()
    moves = current.board.generate_moves()
    for move in moves:
        child = current.createChild()
        child.board.make_move(move)
        child.get_grandparents_value()
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





