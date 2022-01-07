#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:58:15 2021

@author: Freddie Lloyd

Part 1: Software Development

Play the Tron 2D board game in the console.

"""

import sys

from board import BoardClass

from player import HumanPlayer
from player import ComputerPlayer


class Tron:
    """A class to represent the Tron 2D board game."""
    
    def __init__(self):
        """Initializes the Tron game's start up screen."""
        
        self.startup_menu()

    def run_game(self,
                 game_type):
        """
        Runs the Tron game in the console.
        
        Parameters:
            game_type - Game against player or computer
        """

        self.m = self._ask_board_size("Enter the board size: >> ")
        
        self.simultaneous = self._ask_simultaneous(
            "Do you want to play a simultaenous game? (yes/no): >> "
            )
        
        self.board_class = BoardClass(self)

        self.board = self.board_class.create_board()

        self.board_class.output_board() # Display initial board
        
        self.human_player = HumanPlayer(self)
        
        if game_type == "computer":
            
            self.cpu_player = ComputerPlayer(self)
            
            difficulty = self._ask_cpu_difficulty(
                "Enter difficulty level of cpu player "
                            "(easy/medium/hard): >> "
                )
                    
            
        
        game_active = True    
        
        # Loop for each round of moves within the game
        while game_active == True:
            
            players_turn = "p1"
            
            p1_move_direction = self.human_player.player_move(players_turn)
            
            p1_move_outcome = self.board_class.process_move(players_turn,
                                                            p1_move_direction)
            
            if p1_move_outcome == "crash":
                
                self.board_class._crash_event(players_turn,
                                              game_type)
                Tron() # Exit to game menu
         
            if p1_move_outcome == "legal":
                
                if self.simultaneous == "no" or self.simultaneous == "n":
                
                    # Only print board after p1 move if not simultaneous game
                    self.board_class.output_board() 
                    
                else:
                    pass
                                        
                if game_type == "player":
                    
                    players_turn = "p2"
                    p2_move_direction = self.human_player.player_move(players_turn)
                    
                elif game_type == "computer":
                    
                    players_turn = "cpu"
                    p2_move_direction = self.cpu_player.cpu_move(self.board,
                                                                 difficulty)
                    
                p2_move_outcome = self.board_class.process_move(players_turn,
                                                                p2_move_direction)
                 
                if p2_move_outcome == "crash":   
                    
                    self.board_class._crash_event(players_turn,
                                                  game_type)
                    Tron()
                    
                elif p2_move_outcome == "potential_draw":
                    
                    if self.simultaneous == "yes" or self.simultaneous == "y":
                        
                        self.board_class._draw_outcome()
                    
                        Tron()
                    
                    elif self.simultaneous == "no" or self.simultaneous == "n":
                        
                        self.board_class._crash_event(players_turn,
                                                      game_type)
                        
                        Tron()
                    
         
                elif p2_move_outcome == "legal":   
                    
                    self.board_class.output_board()





    def startup_menu(self):
        """Displays the game's start-up menu, allows player to select
        the desired type of game"""

        print("""
         ---------- Tron 2D -----------
        |                              |
        |  1. 2-Player Game            |
        |  2. Game vs Computer         |
        |  Press any other key to exit | 
        |                              |
         ------------------------------
          """                          
          )
          
                  
        selection = input("Enter selection: >> ")
            
        if selection == "1":
            
            print("\nYou will now play a 2-Player Game!") 
            
            game_type = "player"
        
            Tron.run_game(self,
                          game_type)
        
        elif selection == "2":
            
            print("\nYou will now play a game against the computer!")
            
            game_type = "computer"
            
            Tron.run_game(self,
                          game_type)

        elif selection != "1" and selection != "2":
            
            print("\nThank you for playing! Have a good day!")         
            
            sys.exit() # Terminates program
    

                      
    def _ask_board_size(self, prompt):
        """
        Ask player what board size they would like to play on,
        raise exceptions if too small or too large.
                
        Parameters: 
            prompt - The question to be asked to the player
            
        Returns:
            board_size - The desired size of the board
        """      
        while True:
            try:
                board_size = int(input(prompt))
                if board_size <= 3 :
                    raise BoardTooSmallError
                elif board_size > 20:
                    raise BoardTooLargeError
                    
            except ValueError:
                print ("\nBoard size must be an integer! "
                       "Please enter a different board size!")
            except BoardTooSmallError:
                print("\nBoard size must be greater than 3! "
                      "Please enter a different board size!")
            except BoardTooLargeError:
                print("\nBoard size must be less than 20! "
                      "Please enter a different board size!")
            else:
                return board_size
            
    def _ask_cpu_difficulty(self, prompt):
        """
        Ask player what difficulty they would like to play against,
        raise exception if invalid answer given.
        
        Parameters: 
            prompt - The question to be asked to the player
            
        Returns:
            difficulty - The desired difficulty of the computer player
        
        """
        while True:
            try:
                difficulty = input(prompt).lower() #.lower so case wont matter
                if (difficulty != "easy" and difficulty != "e" 
                    and difficulty != "medium" and difficulty != "m" 
                    and difficulty != "hard" and difficulty != "h"):
                        raise InvalidCpuDifficulty
                    
            except InvalidCpuDifficulty:
                print("\n Difficulty must be easy, medium or hard! "
                      "Please enter a valid difficulty!")    
            else:
                return difficulty
            
    def _ask_simultaneous(self, prompt):
        """
        Ask player whether they would like to play a simultaneous game,
        raise exception if invalid answer given.
        
        Parameters: 
            prompt - The question to be asked to the player
            
        Returns:
            simultaneous - The desired simultaneousness of the game
        """   
        while True:
            try:
                simultaneous = input(prompt).lower()
                if (simultaneous != "yes" and simultaneous != "y"
                    and simultaneous != "no" and simultaneous != "n"):
                        raise SimultaneousError    
                        
            except SimultaneousError:
                print("\nPlease enter yes or no!")
            else:
                return simultaneous
            

            
class Error(Exception):
    """Base class for other exceptions"""
    
class BoardTooSmallError(Error):
    """Raise when the board size input value is too small"""
    
class BoardTooLargeError(Error):
    """Raise when the board size input value is too large"""
    
class InvalidCpuDifficulty(Error):
    """Raise when input cpu difficulty is invalid"""   
    
class SimultaneousError(Error):
    """Raise when the simultaneous input is not yes or no"""
         
                    


    

Tron() # Run Tron
 
 
 
 
 
 
