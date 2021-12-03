#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:45:17 2021

@author: freddielloyd
"""

import numpy as np

import random as random


class PlayerClass:
    
    def __init__(self, tron_game):
                
        self.m = tron_game.m
        
        self.board = tron_game.board
        
        
    def player_move(self, players_turn):
        
        
        if players_turn == "p1":
            current_index = np.where(self.board == "1")
            player_move = input(">> Player 1: What is your move? (left/right/up/down) ")

        elif players_turn == "p2":
            current_index = np.where(self.board == "2")
            player_move = input(">> Player 2: What is your move? (left/right/up/down) ")

        # Assign new index as copy of current index
        # This is to be able to change array indexes of player both before and after move
        # Create copy so doesn't change original index
        new_index = np.copy(current_index)
        
        
        
        if player_move == "left":
                
            new_index[1] -= 1
            
            # Legal column index is greater than or equal to 0 as indexes start at 0
            if new_index[1] >= 0 and self.board[tuple(new_index)] != "X":
                      
                self.board[current_index] = "X" # Make array position before moving = "X"
                
                if players_turn == "p1":
                    self.board[tuple(new_index)] = "1" # Player 1's new position
                elif players_turn == "p2":
                    self.board[tuple(new_index)] = "2" # Player 2's new position
                    
                return "Legal"
                
            else:
                return "Crash"
                             
        elif player_move == "right":
            
            new_index[1] += 1
            
            # Legal column index is less than than m as m-1 is final column
            if (new_index[1] < self.m and self.board[tuple(new_index)] != "X"):
            
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
            
            # Legal row index is greater than or equal to 0 as indexes start at 0
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
    
    def __init__(self, tron_game):
        super().__init__(tron_game)
        
        
    def human_move(self):
        players_turn = "p1"
        
        return(self.player_move(players_turn))

        
        
        
        
class ComputerPlayer(PlayerClass):
        
    def __init__(self, tron_game):
        super().__init__(tron_game)
        
        self.difficulty = tron_game.difficulty
        
        
    def cpu_move(self):
        
        #players_turn == "cpu"
        current_index = np.where(self.board == "2")

        # Assign new index as copy of current index
        # This is to be able to change array indexes of player both before and after move
        # Create copy so doesn't change original index
        new_index = np.copy(current_index)

        
        if self.difficulty == "easy":
            
            cpu_move = random.choice(('left','right','up','down'))
            
            move_outcome = self.cpu_move_outcome(current_index, 
                                                 new_index, 
                                                 cpu_move)
            
            return self.board, move_outcome
        
        
        #CPU WILL NOT CRASH OTHER THAN INTO PLAYER - 'RANDOM NON-SUICIDAL MOVE'
        if self.difficulty == "medium":
            
            number_legal_moves, possible_moves = self._legal_moves_info()
            
            if number_legal_moves > 0:
            
                cpu_move = random.choice(possible_moves) #selects from non-suicidal moves other than into player 1
                #print(cpu_move)
            
                move_outcome = self.cpu_move_outcome(current_index, 
                                                     new_index, 
                                                     cpu_move)
                #print(move_outcome)

            
            # cpu move will go on forever if no legal moves so add if statement
            # if number_legal_moves > 0:
            
                # while move_outcome == "Crash":
                #     # Reset new index if crashed to output correct board
                #     new_index = np.copy(current_index)
                #     cpu_move = random.choice(('left','right','up','down'))
                #     print(cpu_move)
                #     move_outcome = self.cpu_move_outcome(current_index, 
                #                                          new_index, 
                #                                          cpu_move)
                #     print(move_outcome)

                return self.board, move_outcome
            
            elif number_legal_moves == 0:
                
                cpu_move = random.choice(('left','right','up','down'))
                
                move_outcome = self.cpu_move_outcome(current_index, 
                                                     new_index, 
                                                     cpu_move)
            
                return self.board, move_outcome
        
        
    def _legal_moves_info(self):
        
        current_index = np.where(self.board == "2")

        # Assign new index as copy of current index
        # This is to be able to change array indexes of player both before and after move
        # Create copy so doesn't change original index
        new_index = np.copy(current_index)
        
        possible_moves = []
        
        number_legal_moves = 0
        
        new_index[1] -= 1
            
        # Legal column index is greater than or equal to 0 as indexes start at 0
        if new_index[1] >= 0 and self.board[tuple(new_index)] != "X" and self.board[tuple(new_index)] != "1":
            
            number_legal_moves += 1
            
            possible_moves.append("left")

        new_index = np.copy(current_index)
        
        new_index[1] += 1
            
        # Legal column index is less than than m as m-1 is final column
        if (new_index[1] < self.m and self.board[tuple(new_index)] != "X") and self.board[tuple(new_index)] != "1":
            
            number_legal_moves += 1
            
            possible_moves.append("right")

        new_index = np.copy(current_index)
        
        new_index[0] -= 1
            
        # Legal row index is greater than or equal to 0 as indexes start at 0
        if new_index[0] >= 0 and self.board[tuple(new_index)] != "X" and self.board[tuple(new_index)] != "1":
            
            number_legal_moves += 1
            
            possible_moves.append("up")


        new_index = np.copy(current_index)

        new_index[0] += 1
        
        # Legal row index is less than than m as m-1 is final row
        if new_index[0] < self.m and self.board[tuple(new_index)] != "X" and self.board[tuple(new_index)] != "1":
            
            number_legal_moves += 1
            
            possible_moves.append("down")


        return number_legal_moves, possible_moves

                        
            

    def cpu_move_outcome(self, current_index, new_index, cpu_move):
        
        if cpu_move == "left":
                
            new_index[1] -= 1
            
            # Legal column index is greater than or equal to 0 as indexes start at 0
            if new_index[1] >= 0 and self.board[tuple(new_index)] != "X":
                      
                self.board[current_index] = "X" # Make array position before moving = "X"
                
                #if players_turn == "p1":
                #    self.board[tuple(new_index)] = "1"
                #elif players_turn == "p2":
                self.board[tuple(new_index)] = "2"
                    
                return "Legal"
                
            else:
                return "Crash"
                             
        elif cpu_move == "right":
            
            new_index[1] += 1
            
            # Legal column index is less than than m as m-1 is final column
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
            
            # Legal row index is greater than or equal to 0 as indexes start at 0
            if new_index[0] >= 0 and self.board[tuple(new_index)] != "X": 
            
                self.board[current_index] = "X"
                
                # if players_turn == "p1":
                #     self.board[tuple(new_index)] = "1" # Player 1's new position
                # elif players_turn == "p2":
                self.board[tuple(new_index)] = "2"
            
                return "Legal"

            else:
                return "Crash"
                 
        elif cpu_move == "down":
            
            new_index[0] += 1
            
            # Legal row index is less than than m as m-1 is final row
            if new_index[0] < self.m and self.board[tuple(new_index)] != "X":
            
                self.board[current_index] = "X"
                
                # if players_turn == "p1":
                #     self.board[tuple(new_index)] = "1"
                # elif players_turn == "p2":
                self.board[tuple(new_index)] = "2"
                    
                return "Legal"
                 
            else:
                return "Crash"

        
        
        