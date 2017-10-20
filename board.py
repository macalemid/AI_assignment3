# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:34:05 2016

@author: Ajinkya
"""
#import search
#import numpy as np

blank = [[0,0,0,0,0,0],[0,0,0,0,0,0]
        ,[0,0,0,0,0,0],[0,0,0,0,0,0],
         [0,0,0,0,0,0],[0,0,0,0,0,0],
         [0,0,0,0,0,0]]

full =  [[0,0,0,2,2,1]
        ,[0,0,0,1,2,2]
        ,[0,0,0,0,1,2]
        ,[0,0,0,0,0,1]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]]

full2 = [[0,0,1,2,2,1]
        ,[0,0,0,1,2,2]
        ,[0,0,0,0,1,2]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]]

full3 = [[0,0,0,0,0,0]
        ,[0,0,0,0,1,2]
        ,[0,0,0,1,2,2]
        ,[0,0,1,1,2,1]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]]

full4 = [[0,0,0,0,0,1]
        ,[0,0,0,0,1,2]
        ,[0,0,0,1,2,2]
        ,[0,0,0,1,2,1]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]]

full5 = [[0,0,0,0,0,1]
        ,[0,0,0,0,1,2]
        ,[0,0,0,0,2,2]
        ,[0,0,1,1,2,1]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]]

full6 = [[0,0,1,2,2,1]
        ,[0,0,0,1,2,2]
        ,[0,0,0,0,0,2]
        ,[0,0,0,0,0,1]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]
        ,[0,0,0,0,0,0]]

class Board:
    def __init__(self):
        self.state = full #blank
        self.turn = 1
        self.moves_player1 = []
        self.moves_player2 = []

    def generate_moves(self): # satisfies
        return_values = []
        for x in range(len(self.state)):
            if self.state[x][0] == 0:
                return_values.append(x)
        return return_values

    def make_move(self,c): # satisfies
        insert_to = self.state[c]
        x = 0
        while x < len(insert_to):


            if insert_to[x] != 0:
                insert_to[x -1] = self.turn
                if self.turn == 1:
                    self.turn = 2;
                    self.moves_player1.insert(0,c)

                    return
                else:
                    self.turn = 1
                    #self.moves_player2.insert(0,c)
                    self.moves_player1.insert(0,c)
                    return

            elif x == len(insert_to) -1:
                insert_to[x] = self.turn
                if self.turn == 1:
                    self.turn = 2;
                    self.moves_player1.insert(0,c)
                    return
                else:
                    self.turn = 1
                    #self.moves_player2.insert(0,c)
                    self.moves_player1.insert(0,c)
                    return

            else:
                x +=1






    def unmake_last_move(self): # satisfies
        to_delete_from = self.state[self.moves_player1.pop()]
        for x in range(0, len(to_delete_from)):
            if to_delete_from[x] != 0:
                to_delete_from[x] = 0;
                return



    def last_move_won(self):
        x = self.moves_player1[0] # x index of the most recently inserted item
        y = 0 # y index of the most recently item
        in_a_row = 0 # used to count number of items in a row
        value = 0   # most recently inserted item
        column = self.state[self.moves_player1[0]]
        for num in range(0, len(column)):
            if column[num] != 0:
                value = column[num]
                y = num
                break

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

        while tempx  >-1 and tempy < len(column):
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
        string = " "
        for y in range(0, len(self.state[0])):
            for x in range(0, len(self.state)):
                string += " " + str(self.state[x][y])
            string += "\n "
        return string


# board = Board()
#
# board.make_move(0)
# print board.last_move_won()
#
#
# board2 = Board()
# board2.state = full2
# board2.make_move(3)
# print board2.last_move_won()
#
# board3 = Board()
# board3.state = full3
# board3.make_move(0)
# print board3.last_move_won()
#
# board4 = Board()
# board4.state = full4
# board4.make_move(3)
# print board4.last_move_won()
#
# board5 = Board()
# board5.state = full5
# board5.make_move(2)
# print board5.last_move_won()
#
# board6 = Board()
# board6.state = full6
# board6.make_move(2)
# print board6.last_move_won()
#
#
# print board.__str__()
#






    
