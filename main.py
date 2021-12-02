#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:58:15 2021

@author: freddielloyd
Part 1: Software Developtment (45%)
This program creates a text-based version of the Tron arcade game
"""


import numpy as np

from board import BoardClass

from player import Player1Class
from player import Player2Class


class TronGame:

    def run_game(self):
        """Function creating and managing Tron game"""
        
        self.m = int(input("Enter the board size: "))
        
        while self.m <= 3:
            print("Board needs to be of size 4 or greater! Please enter another size.")
            self.m = int(input("Enter the board size: "))
            
            
        self.board_class = BoardClass(self)
        
        self.board = self.board_class.create_board()
        
        self.output_board = self.board_class.output_board(self.board)
        
          
        self.player1 = Player1Class(self)
        self.player2 = Player2Class(self)


        game_active = True
        
        # Loop for each round of moves within the game
        while game_active == True:
            
            if self.player1.p1_moves() == "Crash":
                print("Player 2 Wins!")
                game_active = False
                    
         
            else:
                self.output_board = self.board_class.output_board(self.board)
                
                # Update index of current position of player 1 after moving -
                # But before player 2's move in case they collide
                index1 = list(np.where(self.board == "1"))
    
                if self.player2.p2_moves() == "Crash":
                    print("Player 1 Wins!")
                    game_active = False
    
                else:
                    self.output_board = self.board_class.output_board(self.board)
                    
                    # Update index of current position of player 2 after moving
                    index2 = list(np.where(self.board == "2")) 
                    
                    # Check indexes after both moves: have players collided?
                    if index1 == index2:
                        print("Players Collide! It's a Draw! Taking you back to game menu!")
                        game_active = False
                                

                    
 
 
                    
if __name__ == '__main__':
    #create an instance of the game and then call run_game()
    tron = TronGame()
    tron.run_game()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
