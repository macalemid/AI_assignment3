# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:34:05 2016

@author: Ajinkya
"""
#import search
#import numpy as np
import copy


blank = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

class Board:
    def __init__(self):
        self.state = copy.deepcopy(blank) # the state of the game starts out as blank
        self._turn = 1 # 1 for player one. 2 for player
        self._previous_move_col = [] # list containing the column where the piece was inserted for use in backtracking




#CHECK
    def generate_moves(self): # satisfies
        '''
         generate_moves(self)
         Generate moves creates a list of all possible moves from current state and returns
         @return
        '''
        return_values = []
        for i in range(len(self.state[0])):
            if self.state[0][i] == 0: # looks at top layer
                return_values.append(i)
        return return_values



    def _shouldGoToNextRow(self, row, col):
        try:
            if self.state[row + 1][col] == 0:
                return True
        except IndexError:
            return False
        return False


    def _switchTurns(self):
        if self._turn == 1:
            self._turn = 2
        elif self._turn == 2:
            self._turn = 1
        else: raise ValueError("turn is equal to a number other than 1 or two");

    # make_move: places a piece into a specified column, for the specific player whose turn it is
    # @param col represents the column that that we want to drop our piece into
    def make_move(self, col): # satisfies
        for row in range (0, len(self.state[0])):
            currentElement = self.state[row][col]
            if currentElement == 0 and not self._shouldGoToNextRow(row, col):
                self.state[row][col] = self._turn
                self._previous_move_col.append(col);
                self._switchTurns()
                return
        raise ValueError("Either the make move function has gone wrong, or you have tried to insert into a full column")

    # input void. output void.
    # returns the depth of the most recently inserted item
    def find_y(self):
        depth = 0 # used to count depth
        for x in self.state[self._previous_move_col[0]]: # iterates through the column of the most recently inserted item
            if x != 0: # first non zero number will be the most recently inserted
                return depth # returns the depth of the most recently inserted
            else:
                depth += 1 # adds one to the depth



    # unmake_last_move: reverses the game one step
    # because they told us to
    def unmake_last_move(self): # satisfies
        if self._previous_move_col != []:
            col = self._previous_move_col.pop() # a number represing column of previous insertion
            for row in range(0, len(self.state)): # iterate through columns
                if self.state[row][col] != 0:
                    self.state[row][col] = 0
                    self._switchTurns()
                    return
        raise ValueError("It seems that you have tried to undo a move when there are no moves to be undone, or there is an error in your function")




    #last_move_won: checks to see if the the most recent move made a sequence of 4,
    # in which case the game has been won by whoever's turn it is NOT
    def last_move_won(self):
        x = self._previous_move_col[0] # x index of the most recently inserted item
        y = self.find_y()   # y index of the most recently item
        in_a_row = 0 # used to count number of items in a row
        value = self.state[x][y]   # most recently inserted item
        column = self.state[self._previous_move_col[0]]

        # checks for 4 in a row bellow
        for num in range(y, len(column)): # check if it should be + 1 or not
            if column[num] == value: # we find a sequence
                in_a_row +=1 # add one to the number of pieces in a row that we have seen
            else:
                break # break because the sequence was broken
        if in_a_row == 4: # if we saw a sequence of 4 return true
            return True
        else: # else reset the number of same peices in a row to zero
            in_a_row = 0


        #checks for 4 in a row left
        for num in range(x, -1, -1): # moves left through columns of the matrix
            if self.state[num][y] == value: # checks if the value is the value of most recently inserted
                in_a_row +=1 # invrease number of items we've seen in a row
                if in_a_row == 4: # if there was 4 in a row, return true
                    return True
            else:
                break  # when we find a value that is not the same as the most recently inserted

        for num in range(x +1,len(self.state)): # checking to the right
            if self.state[num][y] == value: # check if the value matches
                in_a_row +=1  # increment the number of items weve seen
                if in_a_row == 4: # check if weve seen 4
                    return True # if so return true
            else:
                break # else there were not four in a row, so return


        in_a_row = 0

        #checks for 4 in a row diagonal, right up
        tempx = x # used to iterate through the matrix and keep x and y
        tempy = y
        while tempx < len(self.state) and tempy > -1:
            if self.state[tempx][tempy] == value:
                in_a_row += 1
                tempx += 1
                tempy -= 1
                if in_a_row == 4:
                    return True

            else:
                break

                # checks for 4 in a row diagonal, right up
        tempx = x  # used to iterate through the matrix and keep x and y
        tempy = y

        while tempx  >-1 and tempy < len(column): # left down
            if self.state[tempx][tempy] == value:
                in_a_row += 1
                tempx -= 1
                tempy += 1
                if in_a_row == 4:
                    return True
            else:
                tempx -= 1
                tempy += 1
                in_a_row = 0

        in_a_row = 0

        tempx = x  # used to iterate through the matrix and keep x and y
        tempy = y
        while tempx < len(self.state) and tempy > -1:
            if self.state[tempx][tempy] == value:
                in_a_row += 1
                tempx += 1
                tempy -= 1
                if in_a_row == 4:
                    return True

            else:
                break

                # checks for 4 in a row diagonal, right up
        tempx = x  # used to iterate through the matrix and keep x and y
        tempy = y

        while tempx > -1 and tempy < len(column):
            if self.state[tempx][tempy] == value:
                in_a_row += 1
                tempx -= 1
                tempy += 1
                if in_a_row == 4:
                    return True
            else:
                tempx -= 1
                tempy += 1
                in_a_row = 0


        in_a_row = 0


        tempx = x  # used to iterate through the matrix and keep x and y
        tempy = y
        # left and up
        while tempx > -1 and tempy > -1:
            if self.state[tempx][tempy] == value:
                in_a_row += 1
                tempx -= 1
                tempy -= 1
                if in_a_row == 4:
                    return True
            else:
                break


                # checks for 4 in a row diagonal, right up
        tempx = x  # used to iterate through the matrix and keep x and y
        tempy = y

        # right and down
        while tempx < len(self.state) and tempy < len(column):
            if self.state[tempx][tempy] == value:
                in_a_row += 1
                tempx += 1
                tempy += 1
                if in_a_row == 4:
                    return True
            else:
                tempx += 1
                tempy += 1
                in_a_row = 0
        return False

    def __str__(self):
        string = ""
        for row in self.state:
            string += str(row) + "\n"
        return string


# board = Board()
#
# board.make_move(0)
# print (board)
#
#
# board2 = Board()
# board2.state = full2
# board2.make_move(3)
# print (board2.last_move_won())
#
# board3 = Board()
# board3.state = full3
# board3.make_move(0)
# print (board3.last_move_won())
#
# board4 = Board()
# board4.state = full4
# board4.make_move(3)
# print (board4.last_move_won())
#
# board5 = Board()
# board5.state = full5
# board5.make_move(2)
# print (board5.last_move_won())
#
# board6 = Board()
# board6.state = full6
# board6.make_move(2)
# print (board6.last_move_won())
#
#
# print (board)
#
#
#
# board7 = Board()
# board7.make_move(0)
# print (board7.last_move_won())
# print (board7.previous_moves[0])
# print (board7)

    
