#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:45:17 2021

@author: freddielloyd
"""

import numpy as np


class Parent_Player_Class:
    
    def __init__(self, tron_game):
                
        self.m = tron_game.m
        
        self.board = tron_game.board
        



class Player1Class(Parent_Player_Class): 
    """Player class contains all information related to a player such as position, colour/ID, etc."""
    
    def __init__(self, tron_game):
        
        super().__init__(tron_game)
            
  
    def p1_moves(self):
        
        index1 = np.where(self.board == "1")
        
        # Assign new index as copy of current index
        # This is to be able to change array indexes of player both before and after move
        # Create copy so doesn't change original index
        new_index1 = np.copy(index1) #assign new index as copy of current index to be able to compare old and new indexes later
        
        p1_move = input(">> Player 1: What is your move? (left,right,up,down) ")
        
        
        if p1_move == "left":
                
            new_index1[1] -= 1
            
            # Legal column index is greater than or equal to 0 as indexes start at 0
            if new_index1[1] >= 0 and self.board[tuple(new_index1)] != "X":
      
                self.board[index1] = "X" # Make array position before moving = "X"
                self.board[tuple(new_index1)] = "1" # Player 1's new position
                
            else:
                print("You Crashed!")
                return "Crash"
                             
        elif p1_move == "right":
            
            new_index1[1] += 1
            
            # Legal column index is less than than m as m-1 is final column
            if (new_index1[1] < self.m and self.board[tuple(new_index1)] != "X"):
            
                self.board[index1] = "X"
                self.board[tuple(new_index1)] = "1"
                
            else:
                print("You Crashed!")
                return "Crash"
                          
        elif p1_move == "up":
            
            new_index1[0] -= 1
            
            # Legal row index is greater than or equal to 0 as indexes start at 0
            if new_index1[0] >= 0 and self.board[tuple(new_index1)] != "X": 
            
                self.board[index1] = "X"
                self.board[tuple(new_index1)] = "1"              
            
            else:
                print("You Crashed!")
                return "Crash"
                 
        elif p1_move == "down":
            
            new_index1[0] += 1
            
            # Legal row index is less than than m as m-1 is final row
            if new_index1[0] < self.m and self.board[tuple(new_index1)] != "X":
            
                self.board[index1] = "X"
                self.board[tuple(new_index1)] = "1"
                 
            else:
                print("You Crashed!")               
                return "Crash"
                

        
        
        
class Player2Class(Parent_Player_Class): 
    """Player class contains all information related to a player such as position, colour/ID, etc."""
    
    def __init__(self, tron_game):
        
        super().__init__(tron_game)
        
           
    def p2_moves(self):
        
        index2 = np.where(self.board == "2")
        
        new_index2 = np.copy(index2)
        
        p2_move = input(">> Player 2: What is your move? (left,right,up,down) ")
        
        if p2_move == "left":
                
            new_index2[1] -= 1
            
            if new_index2[1] >= 0 and self.board[tuple(new_index2)] != "X":
      
                self.board[index2] = "X"
                self.board[tuple(new_index2)] = "2"
                    
            else:
                print("You Crashed!")
                return "Crash"
                               
        elif p2_move == "right":
            
            new_index2[1] += 1
            
            if (new_index2[1] < self.m and self.board[tuple(new_index2)] != "X"):
            
                self.board[index2] = "X"
                self.board[tuple(new_index2)] = "2"
                
            else:
                print("You Crashed!")
                return "Crash"
            
        elif p2_move == "up":
            
            new_index2[0] -= 1
            
            if new_index2[0] >= 0 and self.board[tuple(new_index2)] != "X":
            
                self.board[index2] = "X"
                self.board[tuple(new_index2)] = "2"
                
            else:
                print("You Crashed!")
                return "Crash"
                    
        elif p2_move == "down":
            
            new_index2[0] += 1
            
            if new_index2[0] < self.m and self.board[tuple(new_index2)] != "X":
            
                self.board[index2] = "X"
                self.board[tuple(new_index2)] = "2"
                
            else:
                print("You Crashed!")
                return "Crash"




