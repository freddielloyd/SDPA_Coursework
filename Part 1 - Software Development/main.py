#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:58:15 2021

@author: freddielloyd
Part 1: Software Developtment (45%)
This program creates a text-based version of the Tron arcade game
"""

import sys

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
        
        self.simultaneous = self._ask_simultaneous("Do you want to play a simultaenous game? (yes/no): >> ")
        
        self.board_class = BoardClass(self)
        

        
        self.board = self.board_class.create_board()
        
        if self.opponent == "cpu":
            
            self.difficulty = self._ask_cpu_difficulty(
                "Enter difficulty level of cpu player "
                            "(easy/medium/hard): >> "
                )
                    
            self.cpu_player = ComputerPlayer(self,
                                             )
            
            # self.difficulty = self.cpu_player.difficulty
            

            
        
        self.board_class.output_board()
        
        self.human = HumanPlayer(self)
        

        



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
                
                if self.simultaneous == "no" or self.simultaneous == "n":
                
                    # Only print board after p1 move if not simultaneous game
                    self.board_class.output_board() 
                    
                else:
                    
                    pass
                        
                             
                #print(self.board)  
                    
                if self.opponent == "player":
                    players_turn = "p2"
                    p2_move_direction = self.human.player_move(players_turn)
                    
                elif self.opponent == "cpu":
                    players_turn = "cpu"
                    
                    #print(self.board)
                    
                    p2_move_direction = self.cpu_player.cpu_move(self.board)
                    
                p2_outcome = self.board_class.process_move(self, 
                                                           players_turn,
                                                           p2_move_direction,
                                                           self.opponent)
                
                print(p2_outcome)
                    
                if p2_outcome == "Crash":                
                    self.board_class._crash_event(players_turn,
                                                  self.opponent)
                    Tron() # Exit to game menu
                    
                elif p2_outcome == "Draw":
                    
                    if self.simultaneous == "yes" or self.simultaneous == "y":
                        self.board_class._draw_outcome()
                    
                        Tron()
                    
                    else:
                        self.board_class.output_board()
                    
         
                elif p2_outcome == "Legal":                
                    self.board_class.output_board()

    
  

    def startup_menu(self):
        """Displays the game's start-up menu and allows player to select 
        the desired type of game."""

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
                size = int(input(prompt))
                if size <= 1 :
                    raise BoardTooSmallError
                elif size >= 20:
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
                return size
            
    def _ask_cpu_difficulty(self, prompt):
        """Ask player what difficulty they would like to play against,
        raise exception if invalid."""
        while True:
            try:
                difficulty = input(prompt).lower() #.lower so case wont matter
                if (difficulty != "easy" and difficulty != "e" 
                    and difficulty != "medium" and difficulty != "m" 
                    and difficulty != "hard" and difficulty != "h"):
                        raise InvalidCpuDifficulty
                    
            except InvalidCpuDifficulty:
                print("\n Difficulty must be easy, medium or hard! "
                      "Please enter a valid difficulty")
                
            else:
                return difficulty
            
    def _ask_simultaneous(self, prompt):
        """Ask player whether they would like to play a simultaneous game.
        Raise exceptions if too large or small."""
        
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
         
                    
#if __name__ == '__main__':
Tron()
 
 
 
 
 
 
