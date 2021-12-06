#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:44:59 2021

@author: freddielloyd
"""


import numpy as np

 
class BoardClass:
    """A class to represent the board on which the game is played."""


    def __init__(self):
        
        self.m = self._ask_board_size("Enter the board size: >> ")

    
    def create_board(self):
        """Creates the initial board and returns it."""
                
        self.board = (
            np.array([[" " for x in range (self.m)] for y in range(self.m)])
            )
        
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
        """Prints the board to be displayed to the player(s)."""
        
        hash_array = np.array("#")
        
        # Row of hashes of length m to 'frame' top and bottom of output board
        hash_array_row = hash_array.repeat(self.m)
        
        print("#|" + "|".join(str(wall) for wall in hash_array_row) + "|#")
      
        for row in range(self.m):
            print("#|" + "|".join(str(num) for num in self.board[row]) + "|#")

        print("#|" + "|".join(str(wall) for wall in hash_array_row) + "|#\n")
        
        
        
            
    def _ask_board_size(self, prompt):
        """Ask player what board size they would like to play on.
        Raise exceptions if too large or small."""
        
        while True:
            try:
                result = int(input(prompt))
                if result <= 3 :
                    raise BoardTooSmallError
                elif result >= 15:
                    raise BoardTooLargeError
                    
            except ValueError:
                print ("\nBoard size must be an integer! "
                       "Please enter a different board size")
            except BoardTooSmallError:
                print("\nBoard size must be greater than 3! "
                      "Please enter a different board size")
            except BoardTooLargeError:
                print("\nBoard size must be less than 15! "
                      "Please enter a different board size")
            else:
                return result
            

                    
                
        
        
class Error(Exception):
    """Base class for other exceptions"""
    
class BoardTooSmallError(Error):
    """Raise when the board size input value is too small"""
    
class BoardTooLargeError(Error):
    """Raise when the board size input value is too large"""
    
