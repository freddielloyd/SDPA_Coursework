#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:45:17 2021

@author: freddielloyd
"""

import numpy as np

import random as random


class PlayerClass:
    """A class to represent a player of the game"""
    
    def __init__(self, tron_game):
                
        self.m = tron_game.m
        
        self.board = tron_game.board
        

        
    def _ask_player_move(self, prompt):
        """Ask player for move and raise exception if move invalid."""
        while True:
            try:
                player_move = input(prompt).lower() #.lower so case wont matter
                if (player_move != "left" and player_move != "l"
                    and player_move != "right" and player_move != "r"
                    and player_move != "up" and player_move != "u"
                    and player_move != "down" and player_move != "d"):
                        raise InvalidDirectionError
                    
            except InvalidDirectionError:
                print("\nDirection must be left, right, up or down! "
                      "Please enter a valid direction")
                
            else:
                return player_move
            

    
class HumanPlayer(PlayerClass):
    """A class representing a human player in the game"""
    
    def __init__(self, tron_game):
        super().__init__(tron_game)
        
        
    
    def player_move(self, players_turn):
        """Process player move on the board and return its legality."""
        
        if players_turn == "p1":
            
            player_move = self._ask_player_move(
                "Player 1: What is your move? >> "
                )

        elif players_turn == "p2":
            
            player_move = self._ask_player_move(
                "Player 2: What is your move? >> "
                )
            
        return player_move
            


        

class ComputerPlayer(PlayerClass):
    """A class representing a non-human player in the game"""
        
    def __init__(self, tron_game):
        super().__init__(tron_game)
        
        self.difficulty = self._ask_cpu_difficulty(
                "Enter difficulty level of cpu player "
                            "(easy/medium/hard): >> "
                )
        
        
    def cpu_move(self):
        """Process computer move based on the difficulty chosen."""
        
        current_index = np.where(self.board == "2")

        #new_index = np.copy(current_index)

        # RANDOM MOVE
        if self.difficulty == "easy":
            
            cpu_move = random.choice(('left','right','up','down'))
            
            return cpu_move
        
        
        # 'RANDOM NON-SUICIDAL MOVE'
        elif self.difficulty == "medium":
            
            number_legal_moves, possible_moves = self._legal_moves_info()
            
            if number_legal_moves > 0:
            
                cpu_move = random.choice(possible_moves)

                return cpu_move
            
            
            elif number_legal_moves == 0:
                
                cpu_move = random.choice(('left','right','up','down'))

                return cpu_move
            
        
        # Smart non-suicidal move - 
        # move in direction with most available spaces
        elif self.difficulty == "hard":
            
            number_legal_moves, possible_moves = self._legal_moves_info()
            
            print("Number of legal moves is: " + str(number_legal_moves))
            print(possible_moves)
            

            if number_legal_moves == 0: # Crash in random direction
                
                cpu_move = random.choice(('left','right','up','down'))

                return cpu_move

            
            elif number_legal_moves == 1: # Move in only available direction
                
                cpu_move = possible_moves[0]
            
                return cpu_move



            elif number_legal_moves > 1:
                
                current_index = np.where(self.board == "2")
                
                current_row = int(current_index[0])
                
                current_column = int(current_index[1])
                
                
                number_pos_moves_left = (
                np.count_nonzero(self.board[current_row, :current_column] == " ")
                ) - (
                np.count_nonzero(self.board[current_row, :current_column] == "X")
                )
                
                number_pos_moves_right = (
                np.count_nonzero(self.board[current_row, current_column+1:] == " ")
                ) - (
                np.count_nonzero(self.board[current_row, current_column+1:] == "X")
                )
                
                number_pos_moves_up = (
                np.count_nonzero(self.board[:current_row, current_column] == " ")
                ) - (
                np.count_nonzero(self.board[:current_row, current_column] == "X")
                )
                
                number_pos_moves_down = (
                np.count_nonzero(self.board[current_row+1:, current_column] == " ")
                ) - (
                np.count_nonzero(self.board[current_row+1:, current_column] == "X")
                )
                
                
                # Check for trails left and right of current position
                if current_column > 0 and current_column < self.m - 1:
                
                    if (self.board[current_row][current_column - 1] == "X"
                    or self.board[current_row][current_column - 1] == "1"):
                        number_pos_moves_left = 0
                    
                                
                    if (self.board[current_row][current_column + 1] == "X"
                    or self.board[current_row][current_column + 1] == "1"):
                        number_pos_moves_right = 0
                        
                # Check for trails left of final column
                elif current_column == self.m - 1:
                    
                    if (self.board[current_row][current_column - 1] == "X"
                    or self.board[current_row][current_column - 1] == "1"):
                        number_pos_moves_left = 0
                        
                # Check for trails above and below current position
                if current_row > 0 and current_row < self.m - 1:
             
                    if (self.board[current_row - 1][current_column] == "X"
                    or self.board[current_row - 1][current_column] == "1"):
                        number_pos_moves_up = 0
                        
                                    
                    if (self.board[current_row + 1][current_column] == "X"
                    or self.board[current_row + 1][current_column] == "1"):
                        number_pos_moves_down = 0
                        
                # Check for trails above final row 
                elif current_row == self.m - 1:
                    
                    if (self.board[current_row - 1][current_column] == "X"
                    or self.board[current_row - 1][current_column] == "1"):
                        number_pos_moves_up = 0
                
                
                pos_moves = ["number_pos_moves_left",
                             "number_pos_moves_right",
                             "number_pos_moves_up",
                             "number_pos_moves_down"]
                
                number_pos_moves = [number_pos_moves_left,
                                    number_pos_moves_right,
                                    number_pos_moves_up,
                                    number_pos_moves_down]
                
                max_pos_moves = max(number_pos_moves)
                
                #multiple_maxs = [m for m in number_pos_moves if m == max_moves]
                    
                # If there is only one max direction
                if number_pos_moves.count(max_pos_moves) == 1:
                    
                    max_index = number_pos_moves.index(max_pos_moves)
                
                    max_string = pos_moves[max_index]
                    
                    max_direction = max_string.split("_")[3]
                    
                    cpu_move = max_direction
                    
                    print("Max direction is " + str(max_direction))
                
                
                # If there is more than one max direction
                elif number_pos_moves.count(max_pos_moves) > 1:
                    
                    number_pos_moves_copy = number_pos_moves.copy()
                    
                    max_indexes = []
                    
                    while max_pos_moves in number_pos_moves_copy:
                        
                        max_indexes.append(
                            number_pos_moves_copy.index(max_pos_moves)
                            )
                        
                        number_pos_moves_copy[max_indexes[0]] = "D"
                        
                        if len(max_indexes) == 2:
                        
                            number_pos_moves_copy[max_indexes[1]] = "D"
                            
                        elif len(max_indexes) == 3:
                        
                            number_pos_moves_copy[max_indexes[2]] = "D"
                            
                        elif len(max_indexes) == 4:
                        
                            number_pos_moves_copy[max_indexes[3]] = "D"
                            
                            
                    max_strings = []
                    
                    max_directions = []
                    
                    for i in range(len(max_indexes)):
                        
                        max_strings.append(pos_moves[max_indexes[i]])
                        
                        max_directions.append(max_strings[i].split("_")[3])
                        
                    print("Max directions are: ")
                    print(max_directions)  
                        
                    cpu_move = random.choice((max_directions))
                    
                print("Chosen move is: " + str(cpu_move))
                    
                # new_index = np.copy(current_index)
                
                return cpu_move




    def _ask_cpu_difficulty(self, prompt):
        """Ask player what difficulty they would like to play against,
        raise exception if invalid."""
        while True:
            try:
                difficulty = input(prompt).lower() #.lower so case wont matter
                if (difficulty != "easy"
                    and difficulty != "medium"
                    and difficulty != "hard"):
                        raise InvalidCpuDifficulty
                    
            except InvalidCpuDifficulty:
                print("\n Difficulty must be easy, medium or hard! "
                      "Please enter a valid difficulty")
                
            else:
                return difficulty  
        
        
        
    def _legal_moves_info(self):
        """Return how many legal directions there are, and what these are."""
        
        current_index = np.where(self.board == "2")
        
        possible_moves = []
        
        number_legal_moves = 0

        new_index = np.copy(current_index)
        
        new_index[1] -= 1
            
        if (new_index[1] >= 0
            and self.board[tuple(new_index)] != "X"
            and self.board[tuple(new_index)] != "1"):
            
            number_legal_moves += 1
            
            possible_moves.append("left")

        new_index = np.copy(current_index)
        
        new_index[1] += 1
            
        if (new_index[1] < self.m 
            and self.board[tuple(new_index)] != "X"
            and self.board[tuple(new_index)] != "1"):
            
            number_legal_moves += 1
            
            possible_moves.append("right")

        new_index = np.copy(current_index)
        
        new_index[0] -= 1
            
        if (new_index[0] >= 0
            and self.board[tuple(new_index)] != "X" 
            and self.board[tuple(new_index)] != "1"):
            
            number_legal_moves += 1
            
            possible_moves.append("up")


        new_index = np.copy(current_index)

        new_index[0] += 1
        
        if (new_index[0] < self.m 
            and self.board[tuple(new_index)] != "X" 
            and self.board[tuple(new_index)] != "1"):
            
            number_legal_moves += 1
            
            possible_moves.append("down")


        return number_legal_moves, possible_moves

                        





class Error(Exception):
    """Base class for other exceptions"""
    
    
class InvalidDirectionError(Error):
    """Raise when input direction is invalid"""

    
class InvalidCpuDifficulty(Error):
    """Raise when input cpu difficulty is invalid"""   
        