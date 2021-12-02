#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:45:17 2021

@author: freddielloyd
"""

import numpy as np


class PlayerClass:
    
    def __init__(self, tron_game):
                
        self.m = tron_game.m
        
        self.board = tron_game.board
        
        
    def player_move(self, players_turn):
        
        
        if players_turn == "p1":
            current_index = np.where(self.board == "1")
            player_move = input(">> Player 1: What is your move? (left,right,up,down) ")

        else:
            current_index = np.where(self.board == "2")
            player_move = input(">> Player 2: What is your move? (left,right,up,down) ")

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
                else:
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
                    self.board[tuple(new_index)] = "1" # Player 1's new position
                else:
                    self.board[tuple(new_index)] = "2" # Player 2's new position
                    
                return "Legal"
                
            else:
                return "Crash"
                          
        elif player_move == "up":
            
            new_index[0] -= 1
            
            # Legal row index is greater than or equal to 0 as indexes start at 0
            if new_index[0] >= 0 and self.board[tuple(new_index)] != "X": 
            
                self.board[current_index] = "X"
                
                if players_turn == "p1":
                    self.board[tuple(new_index)] = "1" # Player 1's new position
                else:
                    self.board[tuple(new_index)] = "2" # Player 2's new position
            
                return "Legal"

            else:
                return "Crash"
                 
        elif player_move == "down":
            
            new_index[0] += 1
            
            # Legal row index is less than than m as m-1 is final row
            if new_index[0] < self.m and self.board[tuple(new_index)] != "X":
            
                self.board[current_index] = "X"
                
                if players_turn == "p1":
                    self.board[tuple(new_index)] = "1" # Player 1's new position
                else:
                    self.board[tuple(new_index)] = "2" # Player 2's new position
                    
                return "Legal"
                 
            else:
                return "Crash"
                
        
