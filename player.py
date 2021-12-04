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
        
        
    def player_move(self, players_turn):
        
        if players_turn == "p1":
            current_index = np.where(self.board == "1")
            player_move = (
                input(">> Player 1: What is your move? (left/right/up/down) ")
                )

        elif players_turn == "p2":
            current_index = np.where(self.board == "2")
            player_move = (
                input(">> Player 2: What is your move? (left/right/up/down) ")
                )

        # Assign new index as copy of current index
        # This is to be able to change array elements of player position -
        # both before and after the move
        new_index = np.copy(current_index)
        
        
        if player_move == "left":
                
            new_index[1] -= 1
            
            # Legal column index >= 0 as indexes start at 0
            if new_index[1] >= 0 and self.board[tuple(new_index)] != "X":
                      
                # Make array position before moving = "X"
                self.board[current_index] = "X"
                
                if players_turn == "p1":
                    self.board[tuple(new_index)] = "1" # Player 1's new position
                elif players_turn == "p2":
                    self.board[tuple(new_index)] = "2" # Player 2's new position
                    
                return "Legal"
                
            else:
                return "Crash"
                             
        elif player_move == "right":
            
            new_index[1] += 1
            
            # Legal column index is < m as m-1 is final column
            if new_index[1] < self.m and self.board[tuple(new_index)] != "X":
            
                self.board[current_index] = "X"
                
                if players_turn == "p1":
                    self.board[tuple(new_index)] = "1"
                elif players_turn == "p2":
                    self.board[tuple(new_index)] = "2"
                    
                return "Legal"
                
            else:
                return "Crash"
                          
        elif player_move == "up":
            
            new_index[0] -= 1
            
            # Legal row index is >= 0 as indexes start at 0
            if new_index[0] >= 0 and self.board[tuple(new_index)] != "X": 
            
                self.board[current_index] = "X"
                
                if players_turn == "p1":
                    self.board[tuple(new_index)] = "1"
                elif players_turn == "p2":
                    self.board[tuple(new_index)] = "2"
            
                return "Legal"

            else:
                return "Crash"
                 
        elif player_move == "down":
            
            new_index[0] += 1
            
            # Legal row index is less than than m as m-1 is final row
            if new_index[0] < self.m and self.board[tuple(new_index)] != "X":
            
                self.board[current_index] = "X"
                
                if players_turn == "p1":
                    self.board[tuple(new_index)] = "1"
                elif players_turn == "p2":
                    self.board[tuple(new_index)] = "2"
                    
                return "Legal"
                 
            else:
                return "Crash"
                
    
    
class HumanPlayer(PlayerClass):
    """A class representing a human player in the game"""
    
    def __init__(self, tron_game):
        super().__init__(tron_game)
        
        
    def human_move(self, players_turn = "p1"):
        """Utiliases player move function from parent class with player = "p1"."""
        
        return(self.player_move(players_turn))

        

class ComputerPlayer(PlayerClass):
    """A class representing a non-human player in the game"""
        
    def __init__(self, tron_game):
        super().__init__(tron_game)
        
        self.difficulty = tron_game.difficulty
        
        
    def cpu_move(self):
        """Process computer move based on the difficulty chosen."""
        
        current_index = np.where(self.board == "2")

        new_index = np.copy(current_index)

        # RANDOM MOVE
        if self.difficulty == "easy":
            
            cpu_move = random.choice(('left','right','up','down'))
            
            move_outcome = self.cpu_move_outcome(current_index, 
                                                 new_index, 
                                                 cpu_move)
            
            return self.board, move_outcome
        
        
        # 'RANDOM NON-SUICIDAL MOVE'
        if self.difficulty == "medium":
            
            number_legal_moves, possible_moves = self._legal_moves_info()
            
            if number_legal_moves > 0:
            
                cpu_move = random.choice(possible_moves)
                
                move_outcome = self.cpu_move_outcome(current_index, 
                                                     new_index, 
                                                     cpu_move)

                return self.board, move_outcome
            
            
            elif number_legal_moves == 0:
                
                cpu_move = random.choice(('left','right','up','down'))
                
                move_outcome = self.cpu_move_outcome(current_index, 
                                                     new_index, 
                                                     cpu_move)
            
                return self.board, move_outcome
            
        
        # Smart non-suicidal move - 
        # move in direction with most available spaces
        if self.difficulty == "hard":
            
            number_legal_moves, possible_moves = self._legal_moves_info()

            if number_legal_moves > 0:
                
                current_index = np.where(self.board == "2")
                
                current_row = int(current_index[0])
                
                current_column = int(current_index[1])
                
                
                number_pos_moves_left = (
                np.count_nonzero(self.board[current_row, :current_column] == " ")
                )
                
                number_pos_moves_right = (
                np.count_nonzero(self.board[current_row, current_column+1:] == " ")
                )
                
                number_pos_moves_up = (
                np.count_nonzero(self.board[:current_row, current_column] == " ")
                )
                
                number_pos_moves_down = (
                np.count_nonzero(self.board[current_row+1:, current_column] == " ")
                )
                
                
                # Check for trails left and right of current position
                if current_column > 0 and current_column < self.m - 1:
                
                    if self.board[current_row][current_column - 1] == "X":
                        number_pos_moves_left = 0
                    
                                
                    if self.board[current_row][current_column + 1] == "X":
                        number_pos_moves_right = 0
                        
                # Check for trails left of final column
                elif current_column == self.m - 1:
                    
                    if self.board[current_row][current_column - 1] == "X":
                        number_pos_moves_left = 0
                        
                # Check for trails above and below current position
                if current_row > 0 and current_row < self.m - 1:
             
                    if self.board[current_row - 1][current_column] == "X":
                        number_pos_moves_up = 0
                        
                                    
                    if self.board[current_row + 1][current_column] == "X":
                        number_pos_moves_down = 0
                        
                # Check for trails above final row 
                elif current_row == self.m - 1:
                    
                    if self.board[current_row - 1][current_column] == "X":
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
                            
                        if len(max_indexes) == 3:
                        
                            number_pos_moves_copy[max_indexes[2]] = "D"
                            
                        if len(max_indexes) == 4:
                        
                            number_pos_moves_copy[max_indexes[3]] = "D"
                            
                            
                    max_strings = []
                    
                    max_directions = []
                    
                    for i in range(len(max_indexes)):
                        
                        max_strings.append(pos_moves[max_indexes[i]])
                        
                        max_directions.append(max_strings[i].split("_")[3])
                        
                        
                    cpu_move = random.choice((max_directions))
                    
                    
                new_index = np.copy(current_index)
                
                move_outcome = self.cpu_move_outcome(current_index, 
                                                     new_index, 
                                                     cpu_move)
                
                return self.board, move_outcome


            elif number_legal_moves == 0:
                
                cpu_move = random.choice(('left','right','up','down'))
                
                move_outcome = self.cpu_move_outcome(current_index, 
                                                     new_index, 
                                                     cpu_move)
            
                return self.board, move_outcome
        
        
        
    def _legal_moves_info(self):
        """Returns how many legal directions there are, and what they are."""
        
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

                        
            

    def cpu_move_outcome(self, current_index, new_index, cpu_move):
        """Returns the legality of the computer's move"""
        
        if cpu_move == "left":
                
            new_index[1] -= 1
            
            if new_index[1] >= 0 and self.board[tuple(new_index)] != "X":
                      
                self.board[current_index] = "X"
                
                #if players_turn == "p1":
                #    self.board[tuple(new_index)] = "1"
                #elif players_turn == "p2":
                self.board[tuple(new_index)] = "2"
                    
                return "Legal"
                
            else:
                return "Crash"
                             
        elif cpu_move == "right":
            
            new_index[1] += 1
            
            if (new_index[1] < self.m and self.board[tuple(new_index)] != "X"):
            
                self.board[current_index] = "X"
                
                #if players_turn == "p1":
                #    self.board[tuple(new_index)] = "1"
                #elif players_turn == "p2":
                self.board[tuple(new_index)] = "2"
                    
                return "Legal"
                
            else:
                return "Crash"
                          
        elif cpu_move == "up":
            
            new_index[0] -= 1
            
            if new_index[0] >= 0 and self.board[tuple(new_index)] != "X": 
            
                self.board[current_index] = "X"
                
                # if players_turn == "p1":
                #     self.board[tuple(new_index)] = "1"
                # elif players_turn == "p2":
                self.board[tuple(new_index)] = "2"
            
                return "Legal"

            else:
                return "Crash"
                 
        elif cpu_move == "down":
            
            new_index[0] += 1
            
            if new_index[0] < self.m and self.board[tuple(new_index)] != "X":
            
                self.board[current_index] = "X"
                
                # if players_turn == "p1":
                #     self.board[tuple(new_index)] = "1"
                # elif players_turn == "p2":
                self.board[tuple(new_index)] = "2"
                    
                return "Legal"
                 
            else:
                return "Crash"

        
        
        