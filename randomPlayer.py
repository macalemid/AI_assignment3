import board
import search
import random
class Player:
    def __init__(self, board):
        self.b = board
        self.name = "Random_Player"
            
    def make_move(self,c):
        self.b.make_move(c)
    
    def get_move(self):
        col = random.randint(0, 6)
        while (self.b.board[5][col] != 0):
            col = random.randint(0, 6)
        print(str(col))
        return (0, col)
    
    def __str__(self):
        return (self.b.__str__())
