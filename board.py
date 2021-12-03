#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:44:59 2021

@author: freddielloyd
"""


import numpy as np

 
class BoardClass:
    """Board class containing attributes to store game states (in 2d array) 
    and players information. Also contains method to print the board."""
    
    
    def __init__(self, tron_game):
        
        self.m = tron_game.m
    
    
    def create_board(self):
                
        self.board = np.array([[" " for x in range (self.m)] for y in range(self.m)])
        
        #   = space not been to,
        # 1 = space of player 1
        # 2 = space of player 2
        # X = space visited by player 1 or player 2

        # Default starting position of player 1 - top left corner
        self.board[0][0] = 1
        # Default starting position of player 2 - bottom right corner
        self.board[self.m-1][self.m-1] = 2
        
        print("\nBoard of size (" + str(self.m) + "x" + str(self.m) + 
              ") created with default locations.")
              
        print("\nThe initial board is: ")
        
        return self.board
        
        
    def output_board(self):
        
        hash_array = np.array("#")
        
        # Row of hashes of length m to 'frame' top and bottom of output board
        hash_array_row = hash_array.repeat(self.m)
        
        print("#|" + "|".join(str(wall) for wall in hash_array_row) + "|#")
      
        for row in range(self.m):
            print("#|" + "|".join(str(num) for num in self.board[row]) + "|#")

        print("#|" + "|".join(str(wall) for wall in hash_array_row) + "|#")
    

