#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:58:15 2021

@author: freddielloyd
Part 1: Software Developtment (45%)
This program creates a text-based version of the Tron arcade game
"""

import sys

import numpy as np

from board import BoardClass

from player import PlayerClass
from player import HumanPlayer
from player import ComputerPlayer


class Tron:
    
    def __init__(self):
        """Initialize the game's start up screen."""
          
        print("""
                  -------- Tron 2D --------
                  1. 2-Player Game
                  2. Game vs Computer
                  Press any other key to exit
                  """)
                  
        selection = input("Enter selection: ")
            
        if selection == "1":
            print("\nYou will now play a 2-Player Game!")       
            
            Tron.run_2player_game(self)
        
        elif selection == "2":
            print("\nYou will now play a game against the computer!")
            
            Tron.run_computer_game(self)
        
        
        elif selection != "1" and selection != "2":
            print("\nThank you for playing! Have a good day!")         
            
            sys.exit() #terminates program


    def run_2player_game(self):
        """Function creating and managing 2-player Tron game"""
        
        opponent = "player"
        
        self.m = int(input(">> Enter the board size: "))
        
        # while self.m <= 3:
        #     print("\nBoard needs to be of size 4 or greater! "
        #           "Please enter another size.")
        #     self.m = int(input("Enter the board size: "))
            
        self.board_class = BoardClass(self)
        
        self.board = self.board_class.create_board()
        
        self.output_board = self.board_class.output_board() #to return initial board
          
        self.player = PlayerClass(self)

        game_active = True    
        
        # # take initial indexes so can compare after player 1's first move
        index1 = list(np.where(self.board == "1"))
        index2 = list(np.where(self.board == "2")) 
        
        # Loop for each round of moves within the game
        while game_active == True:
            
            players_turn = "p1"
            
            # if self.player.player_move(players_turn) == "Crash":
            p1_move = self.player.player_move(players_turn)
            
            if p1_move == "Crash":                
                self._crash_event(players_turn,
                                  opponent)
         
            elif p1_move == "Legal":               
                self.board_class.output_board()
                                       
                # Update index of current position of player 1 after moving -
                # But before player 2's next move in case they collided
                index1 = list(np.where(self.board == "1"))
                
                self._check_players_collision(players_turn, 
                                              index1, 
                                              index2,
                                              opponent)                
                    
                players_turn = "p2"
                
                p2_move = self.player.player_move(players_turn)
    
                if p2_move == "Crash":                
                    self._crash_event(players_turn,
                                      opponent)
         
                elif p2_move == "Legal":                
                    self.board_class.output_board()
                    
                    # Update index of current position of player 2 after moving -
                    # But before player 1's next move in case they collided
                    index2 = list(np.where(self.board == "2"))
                    
                    self._check_players_collision(players_turn, 
                                                  index1, 
                                                  index2,
                                                  opponent)
    
    
    def run_computer_game(self):
        """Function creating and managing computer Tron game"""
        
        opponent = "cpu"
        
        self.m = int(input(">> Enter the board size: "))
        
        
        
        # Difficulties: 
        # Easy = random move
        # Medium = random non-suicidal move
        # Hard = best non-suicidal move
        
        
        self.difficulty = input(">> Enter difficulty level of cpu player "
                                "(easy/medium/hard): ")
        
        
        # while self.m < 3:
        #     print("\nBoard needs to be of size 4 or greater! "
        #           "Please enter another size.")
        #     self.m = int(input("Enter the board size: "))
            
        self.board_class = BoardClass(self)
        
        self.board = self.board_class.create_board()
        
        self.board_class.output_board() #to return initial board
          
        self.human_player = HumanPlayer(self)
        
        self.cpu_player = ComputerPlayer(self)

        game_active = True    
        
        # # take initial indexes so can compare after player 1's first move
        index1 = list(np.where(self.board == "1"))
        index2 = list(np.where(self.board == "2")) 
        
        # Loop for each round of moves within the game
        while game_active == True:
            
            players_turn = "p1"
            
            # if self.player.player_move(players_turn) == "Crash":
            p1_move = self.human_player.human_move()
                        
            if p1_move == "Crash":                
                self._crash_event(players_turn,
                                  opponent)
         
            elif p1_move == "Legal":               
                self.board_class.output_board()
                                       
                # Update index of current position of player 1 after moving -
                # But before player 2's next move in case they collided
                index1 = list(np.where(self.board == "1"))
                
                self._check_players_collision(players_turn, 
                                              index1, 
                                              index2,
                                              opponent)                
                    
                players_turn = "cpu"
                
                # CPU MOVE RETURNS BOARD AND OUTCOME
                self.board, cpu_move_outcome = self.cpu_player.cpu_move()
                
    
                if cpu_move_outcome == "Crash":                
                    self._crash_event(players_turn,
                                      opponent)
                    
                elif cpu_move_outcome == "Legal":             
                    self.board_class.output_board()
         
            
         
                # Update index of current position of player 2 after moving -
                # But before player 1's next move in case they collided
                index2 = list(np.where(self.board == "2"))
                    
                self._check_players_collision(players_turn, 
                                                  index1, 
                                                  index2,
                                                  opponent)
         
                    

                    
                # else:
                #     print("WRONG")

    
    
      
    def _crash_event(self, 
                     players_turn,
                     opponent):
        """Display output message if a player has crashed out of bounds,
        or into the trail of either player"""
                
        if players_turn == "p1":
            
            if opponent == "player":
                print("\nPlayer 1 crashed! Player 2 wins!"
                      "\nTaking you back to game menu!")

            elif opponent == "cpu":
                print("\nPlayer 1 crashed! Computer wins!"
                      "\nTaking you back to game menu!")
            
        elif players_turn == "p2":
            print("\nPlayer 2 crashed! Player 1 wins!"
                  "\nTaking you back to game menu!")

        elif players_turn == "cpu":
            print("\nComputer crashed! Player 1 wins!"
                  "\nTaking you back to game menu!")
        Tron()               
     
    def _check_players_collision(self, 
                                 players_turn, 
                                 index1, 
                                 index2,
                                 opponent):
        """Check equality of current player indices after each move
        and end game if equal"""

        # Check indexes after each move: do they match?
        if index1 == index2:
            
            if players_turn == "p1":
                
                if opponent == "player":
                    print ("\nPlayer 1 crashed into Player 2! Player 2 wins!" 
                           "\nTaking you back to game menu!")
                
                elif opponent == "cpu":
                    print ("\nPlayer 1 crashed into the computer! Computer wins!"
                           "\nTaking you back to game menu!")
                
            elif players_turn == "p2":
                print ("\nPlayer 2 crashed into Player 1! Player 1 wins!" 
                       "\nTaking you back to game menu!")
                
            elif players_turn == "cpu":
                print ("\nComputer crashed into Player 1! Player 1 wins!" 
                       "\nTaking you back to game menu!")
                
            Tron()
            
            
        
        
        
 
                    
#if __name__ == '__main__':
Tron()
 
 
 
 
 
 
