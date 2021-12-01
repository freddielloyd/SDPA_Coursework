#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:58:15 2021

@author: freddielloyd
Part 1: Software Developtment (45%)
This program creates a text-based version of the Tron arcade game
"""


import numpy as np

from player import Player1Class
from player import Player2Class


class TronGame:

    def run_game(self):
        """Function creating and managing Tron game"""
        
        self.m = int(input("Enter the board size: "))
        
        while self.m <= 3:
            print("Board needs to be of size 4 or greater! Please enter another size.")
            self.m = int(input("Enter the board size: "))

        
        self.board = np.array([[" " for x in range (self.m)] for y in range(self.m)])
        
        # Default starting position of player 1 - top left corner
        self.board[0][0] = 1
        # Default starting position of player 2 - bottom right corner
        self.board[self.m-1][self.m-1] = 2
                
        #   = space not been to,
        # 1 = space of player 1
        # 2 = space of player 2
        # X = space visited by player 1 or player 2
        
        print(">> Board of size " + "(" + str(self.m) + "x" + str(self.m) + ") created with default locations. The initial board is: ")
        
        print(self.board)
        
          
        self.player1 = Player1Class(self)
        self.player2 = Player2Class(self)


        game_active = True
        
        # Loop for each round of moves within the game
        while game_active == True:
            
            if self.player1.p1_moves() == "Crash":
                print("Player 2 Wins!")
                game_active = False
                    
         
            else:
                print(self.board)
                
                # Update index of current position of player 1 after moving -
                # But before player 2's move in case they collide
                index1 = list(np.where(self.board == "1"))
    
                if self.player2.p2_moves() == "Crash":
                    print("Player 1 Wins!")
                    game_active = False
    
                else:
                    print(self.board)
                    
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
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
