# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:00:29 2016

@author: Ajinkya
"""
import copy
import evalFunction



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
        self.children = []
        self.isMaxNode = isMaxNode
        self.depth = 0
        self.board = copy.deepcopy(board)

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
        child = Node(not self.isMaxNode, self.board)
        child.parent = self
        child.depth = self.depth + 1
        child.get_grandparents_value()
        self.children.append(child)   #grandparents_value() get the value of nearest min/max node ancestor, also updates
        return child



    def setParentBetter(self):
        if self.parent.isMaxNode:
            if self.value > self.parent.value:
                self.parent.value = self.value
                return
            return
        elif not self.parent.isMaxNode: #then min node
            if self.parent.value < self.value:
                self.parent.value = self.value
                return
            return
        raise ValueError("There is an error in the setParentBetter function")


    def update_all_values(self):
        if self.parent != None:
            self.setParentBetter()
            self.parent.update_all_values()
        return



    # return None. input None
    # looks at the child node.
    # if the value of the child node is better the parent nodes value is updated to be the child's
    def update_value(self):
        if self.children is not []:
            for child in self.children:
                if self.isMaxNode:   # if this node is a max node
                    if child.value > self.value: # if the value of child is greater
                        self.value = child.value # update the height to be that of child's
                elif child.value < self.value: # if this node is a min node and the value of child's is less
                    self.value = child.value # this nodes value is updated to be that of child's




def expand(frontier):
    current = frontier.pop(0) #remove first element
    moves = current.board.generate_moves() #moves: list from 0, 6
    for move in moves:
        child = current.createChild()
        child.board.make_move(move)
        frontier.insert(0, child)


# input: max depth(depth), list of node (frontier)
# this goes through the entire tree and gives values to the nodes
# this iterates throught frontier expanding and exploring in a depth first style until it reaches the maximum depth.
#  when a max depth is reached, the evalFunction is called and values are updated.
# def explore(depthLimit, frontier):
#     while frontier != []:
#         while frontier[0].depth < depthLimit:
#             expand(frontier)
#
#         bottom = frontier.pop(0)
#         bottom.value = evalFunction.evalFunction(bottom.board.transpose())
#         if bottom.parent != None:
#             bottom.parent.update_value()



def updateEnds(largestNodeSeen, smallestNodeSeen, bottom):
    if largestNodeSeen == None:
        largestNodeSeen = bottom
    elif largestNodeSeen.value < bottom.value:
        largestNodeSeen = bottom

    if smallestNodeSeen == None:
        smallestNodeSeen = bottom
    elif smallestNodeSeen.value > bottom.value:
        smallestNodeSeen = bottom
    return (largestNodeSeen, smallestNodeSeen)



def minimax(board, depthLimit):
    start = Node(board.turn == 1, board) #if turn is 1 its a max node, if its 2 its a min node
    frontier = [start]

    largestNodeSeen = None
    smallestNodeSeen = None

    while frontier != []:
        if frontier[0].depth >= depthLimit: #depth protection
            bottom = frontier.pop(0)
            bottom.value = evalFunction.evalFunction(bottom.board.transpose())
            bottom.update_all_values()
            big_small = updateEnds(largestNodeSeen, smallestNodeSeen, bottom)

            largestNodeSeen = big_small[0]
            smallestNodeSeen = big_small[1]
        else:
            expand(frontier)

    if start.isMaxNode:
        if largestNodeSeen != None:
            if largestNodeSeen.value == 1:
                return 1
            elif largestNodeSeen.value == -1:
                return -1
            else:
                return largestNodeSeen.board.previous_moves.pop()
    else:
        if smallestNodeSeen != None:
            if smallestNodeSeen.value == 1:
                return 1
            elif smallestNodeSeen.value == -1:
                return -1
            else:
                return smallestNodeSeen.board.previous_moves.pop()
    raise ValueError("There seems to have been an error in minimax... nice try though")




def minimax_root(b,depth):
    result = minimax(b, depth)
    if result == -1 or result == 1:
        return (result, None)
    else:
        return (0, result)




def find_win(b,depth):
    pass



def alphabeta_minimax(b,depth,a,be):
    pass

def negamax_root_alphabeta(b, depth):
    pass





