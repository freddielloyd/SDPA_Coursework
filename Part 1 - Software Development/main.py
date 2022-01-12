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
            "Do you want to play a simultaneous game? (y/n) >> "
            )
        
        self.board_class = BoardClass(self)

        self.board = self.board_class.create_board()

        self.board_class.output_board() # Display initial board
        
        self.human_player = HumanPlayer(self)
        
        if game_type == "computer":
            
            self.cpu_player = ComputerPlayer(self)
            
            difficulty = self._ask_cpu_difficulty(
                "Enter difficulty level of computer player "
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
         
            elif p1_move_outcome == "legal":
                
                if self.simultaneous == "no" or self.simultaneous == "n":
                
                    # Only print board after p1 move if not simultaneous game
                    self.board_class.output_board() 
                    
                elif self.simultaneous == "yes" or self.simultaneous == "y":
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
                    

    def run_hex_game(self,
                     game_type):
        """
        Runs the Tron game in the console.
        
        Parameters:
            game_type - Game against player or computer
        """

        self.m = self._ask_hex_board_size("Enter the hexagon board size: >> ")
        
        self.simultaneous = self._ask_simultaneous(
            "Do you want to play a simultaneous game? (y/n) >> "
            )
        
        self.board_class = BoardClass(self)

        self.board = self.board_class.create_hex_board()
        
        self.board_class.output_hex_board() # Display initial board
      
        self.human_player = HumanPlayer(self)
        
        if game_type == "computer":
            
            self.cpu_player = ComputerPlayer(self)
            
            difficulty = self._ask_cpu_difficulty(
                "Enter difficulty level of computer player "
                                "(easy/medium/hard): >> "
                )
              
        game_active = True    
        
        # Loop for each round of moves within the game
        while game_active == True:
            
            players_turn = "p1"
            
            p1_move_direction = self.human_player.player_hex_move(players_turn)
            
            p1_move_outcome = self.board_class.process_hex_move(players_turn, 
                                                                p1_move_direction)
            
            if p1_move_outcome == "crash":
                
                self.board_class._crash_event(players_turn,
                                              game_type)
                Tron() # Exit to game menu
         
            elif p1_move_outcome == "legal":
                
                if self.simultaneous == "no" or self.simultaneous == "n":
                
                    # Only print board after p1 move if not simultaneous game
                    self.board_class.output_hex_board()
                    
                elif self.simultaneous == "yes" or self.simultaneous == "s":
                    pass

            print() # Creates a space between hexagons
                                    
            if game_type == "player":
                
                players_turn = "p2"
                p2_move_direction = self.human_player.player_hex_move(players_turn)
                
            elif game_type == "computer":
                
                players_turn = "cpu"
                p2_move_direction = self.cpu_player.cpu_hex_move(self.board,
                                                                 difficulty)
                
            p2_move_outcome = self.board_class.process_hex_move(players_turn,
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
                
                self.board_class.output_hex_board()
                
                
    def startup_menu(self):
        """Displays the game's start-up menu, allows player to select
        the desired type of game"""

        print(
            """
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
            
            game_type = "player"
            
            hexagon = self._ask_hexagon("\nDo you want to play on a hexagon board? (y/n) >> ")
            
            if hexagon == "no" or hexagon == "n":

                print("\nYou will now play a regular 2-player game!")
                
                Tron.run_game(self,
                              game_type)
                
            elif hexagon == "yes" or hexagon == "y":
                
                print("\nYou will now play a 2-player hexagon game!")
                
                Tron.run_hex_game(self, 
                                  game_type)

            
            print("\nYou will now play a 2-Player Game!") 
        
            Tron.run_game(self,
                          game_type)
        
        elif selection == "2":
            
            game_type = "computer"
            
            hexagon = self._ask_hexagon("\nDo you want to play on a hexagon board? (y/n) >> ")
            
            if hexagon == "no" or hexagon == "n":

                print("\nYou will now play a regular game against the computer!")
                
                Tron.run_game(self,
                              game_type)
                
            elif hexagon == "yes" or hexagon == "y":
                
                print("\nYou will now play a hexagon game against the computer!")
            
                
                Tron.run_hex_game(self, 
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
                        raise YesNoError              
            except YesNoError:
                print("\nPlease enter yes or no!")
            else:
                return simultaneous
            
            
    def _ask_hexagon(self, prompt):
        """
        Ask player whether they would like to play a hexagon game,
        raise exception if invalid answer given.
        
        Parameters: 
            prompt - The question to be asked to the player
            
        Returns:
            hexagon - Whether they would like to play on a hexagon grid.
        """   
        while True:
            try:
                hexagon = input(prompt).lower()
                if (hexagon != "yes" and hexagon != "y"
                    and hexagon != "no" and hexagon != "n"):
                        raise YesNoError          
            except YesNoError:
                print("\nPlease enter yes or no!")
            else:
                return hexagon
            
                
    def _ask_hex_board_size(self, prompt):
        """
        Ask player what hexagon board size they would like to play on,
        raise exceptions if too small, large or not an odd number.
                
        Parameters: 
            prompt - The question to be asked to the player
            
        Returns:
            board_size - The desired size of the hex board
        """      
        while True:
            try:
                board_size = int(input(prompt))
                if board_size % 2 == 0:
                    raise EvenNumberError
                if board_size < 5 :
                    raise BoardTooSmallError
                elif board_size > 13:
                    raise BoardTooLargeError       
            except ValueError:
                print ("\nBoard size must be an integer! "
                       "Please enter a different board size!")
            except EvenNumberError:
                print("\nBoard size must be an odd integer! "
                      "Please enter a different board size!")
            except BoardTooSmallError:
                print("\nBoard size must be greater than 5! "
                      "Please enter a different board size!")
            except BoardTooLargeError:
                print("\nBoard size must be 11 or less  ! "
                      "Please enter a different board size!")
            else:
                return board_size
            
            
class Error(Exception):
    """Base class for other exceptions"""
    
class EvenNumberError(Error):
    """Raise when the board size input value is an even number"""
    
class BoardTooSmallError(Error):
    """Raise when the board size input value is too small"""
    
class BoardTooLargeError(Error):
    """Raise when the board size input value is too large"""
    
class InvalidCpuDifficulty(Error):
    """Raise when input cpu difficulty is invalid"""   
    
class YesNoError(Error):
    """Raise when the input was yes or no"""
         
                    


    
if __name__ == '__main__':
    Tron() # Run Tron
 
 
 
 
 
 
