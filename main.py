#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:58:15 2021

@author: freddielloyd
Part 1: Software Developtment (45%)
This program creates a text-based version of the Tron arcade game
"""

import sys

#import numpy as np

from board import BoardClass

from player import HumanPlayer
from player import ComputerPlayer


class Tron:
    
    def __init__(self):
        """Initialize the game's start up screen."""
          
        self.startup_menu()


    def run_game(self):
        """Creates and manages a Tron game."""

        self.m = self._ask_board_size("Enter the board size: >> ")
        
        self.board_class = BoardClass(self)
        
        self.board = self.board_class.create_board()
        
        self.board_class.output_board() # Display initial board after ask for cpu difficulty
        
        self.human = HumanPlayer(self)
        
        if self.opponent == "cpu":
                    
            self.cpu_player = ComputerPlayer(self)


        game_active = True    
        
        # Loop for each round of moves within the game
        while game_active == True:
            
            players_turn = "p1"
            
            p1_move_direction = self.human.player_move(players_turn)
            
            p1_outcome = self.board_class.process_move(self, 
                                                       players_turn,
                                                       p1_move_direction,
                                                       self.opponent)
            
            if p1_outcome == "Crash":
                self.board_class._crash_event(players_turn,
                                              self.opponent)
                Tron() # Exit to game menu
         
            if p1_outcome == "Legal":
                self.board_class.output_board()
                        
                             
                    
                if self.opponent == "player":
                    players_turn = "p2"
                    p2_move_direction = self.human.player_move(players_turn)
                    
                elif self.opponent == "cpu":
                    players_turn = "cpu"
                    
                    # cpu_move METHOD RETURNS BOARD AND OUTCOME
                    p2_move_direction = self.cpu_player.cpu_move()


                p2_outcome = self.board_class.process_move(self, 
                                                           players_turn,
                                                           p2_move_direction,
                                                           self.opponent)
                    
                if p2_outcome == "Crash":                
                    self.board_class._crash_event(players_turn,
                                                  self.opponent)
                    Tron() # Exit to game menu
         
                elif p2_outcome == "Legal":                
                    self.board_class.output_board()

    
  

    def startup_menu(self):
        """Displays the game's start-up menu and allows player to select 
        the desired type of game."""

        print("""
          -------- Tron 2D --------
          1. 2-Player Game
          2. Game vs Computer
          Press any other key to exit
          """)
                  
        selection = input("Enter selection: >> ")
            
        if selection == "1":
            print("\nYou will now play a 2-Player Game!") 
            
            #self.players = ("p1", "p2")
            self.opponent = "player"
            
            #Tron.run_2player_game(self)
            Tron.run_game(self)
        
        elif selection == "2":
            print("\nYou will now play a game against the computer!")
            
            #self.players = ("p1", "cpu")
            self.opponent = "cpu"
            
            #Tron.run_computer_game(self)
            Tron.run_game(self)
        
        
        elif selection != "1" and selection != "2":
            print("\nThank you for playing! Have a good day!")         
            
            sys.exit() #terminates program
    

        
    # def _check_players_collision(self, 
    #                              players_turn, 
    #                              index1, 
    #                              index2,
    #                              opponent):
    #     """Check equality of current player indices after each move
    #     and end game if equal"""

    #     # Check indexes after each move: do they match?
    #     if index1 == index2:
            
    #         if players_turn == "p1":
                
    #             if opponent == "player":
    #                 print ("\nPlayer 1 crashed into Player 2! Player 2 wins!" 
    #                        "\nTaking you back to game menu!")
                
    #             elif opponent == "cpu":
    #                 print ("\nPlayer 1 crashed into the computer! Computer wins!"
    #                        "\nTaking you back to game menu!")
                
    #         elif players_turn == "p2":
    #             print ("\nPlayer 2 crashed into Player 1! Player 1 wins!" 
    #                    "\nTaking you back to game menu!")
                
    #         elif players_turn == "cpu":
    #             print ("\nComputer crashed into Player 1! Player 1 wins!" 
    #                    "\nTaking you back to game menu!")
                
    #         Tron()
            
    
    def _ask_board_size(self, prompt):
        """Ask player what board size they would like to play on.
        Raise exceptions if too large or small."""
        
        while True:
            try:
                result = int(input(prompt))
                if result <= 1 :
                    raise BoardTooSmallError
                elif result >= 20:
                    raise BoardTooLargeError
                    
            except ValueError:
                print ("\nBoard size must be an integer! "
                       "Please enter a different board size")
            except BoardTooSmallError:
                print("\nBoard size must be greater than 3! "
                      "Please enter a different board size")
            except BoardTooLargeError:
                print("\nBoard size must be less than 20! "
                      "Please enter a different board size")
            else:
                return result
            
            
    

            
class Error(Exception):
    """Base class for other exceptions"""
    
class BoardTooSmallError(Error):
    """Raise when the board size input value is too small"""
    
class BoardTooLargeError(Error):
    """Raise when the board size input value is too large"""
         
                    
#if __name__ == '__main__':
Tron()
 
 
 
 
 
 
