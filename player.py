# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:21:51 2016

@author: Ajinkya
"""
import board
import search
class Player:
    def __init__(self, board, name):
        self.board = board
        self.name = name
        # TODO
        
    def make_move(self, c):
        self.board.make_move(c)

    def get_move(self):
        pass
        # TODO
    
    def __str__(self):
        return "name: %s", self.name
