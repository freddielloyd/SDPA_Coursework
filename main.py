#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:58:15 2021

@author: freddielloyd
Part 1: Software Developtment (45%)
This program creates a text-based version of the Tron arcade game
"""


import numpy as np


def run_game():
    """Function creating and managing Tron game"""
    
    m = int(input("Enter the board size: "))
    
    board = np.array([[" " for x in range (m)] for y in range(m)])
    
    # Default starting position of player 1 - top left corner
    board[0][0] = 1
    # Default starting position of player 2 - bottom right corner
    board[m-1][m-1] = 2
            
    #   = space not been to,
    # 1 = space of player 1
    # 2 = space of player 2
    # X = space visited by player 1 or player 2
    
    game_ongoing = True
    
    while game_ongoing == True:
        
                                        
        index1 = np.where(board == "1") #index of current position of player 1
        
        # Assign new index as copy of current index
        # This is to be able to change array indexes of player both before and after move
        # Create copy so doesn't change original index
        new_index1 = np.copy(index1)
        
        p1_move = input("Player 1: What is your move? (left,right,up,down) ")
        
        if p1_move == "left":
            
            new_index1[1] -= 1 # New index 'column' one to the left
            
            # Legal column index is greater than or equal to 0 as indexes start at 0
            if new_index1[1] >= 0 and board[tuple(new_index1)] != "X":
      
                board[index1] = "X" #make array position before moving = "X"
                board[tuple(new_index1)] = "1" # Player 1's new position
                    
            else:
                print("This moves you out of bounds on the left!")
                crash_event()
                game_ongoing = False
                           
        elif p1_move == "right":
            
            new_index1[1] += 1 # new index 'column' one to the right
            
            # Legal column index is less than than m as m-1 is final column
            if (new_index1[1] < m and board[tuple(new_index1)] != "X"):
            
                board[index1] = "X"
                board[tuple(new_index1)] = "1"
                                    
            else:
                print("This moves you out of bounds on the right!")
                crash_event()
                game_ongoing = False
            
        elif p1_move == "up":
            
            new_index1[0] -= 1 # New index 'row' one above
            
            # Legal row index is greater than or equal to 0 as indexes start at 0
            if new_index1[0] >= 0 and board[tuple(new_index1)] != "X":
            
                board[index1] = "X"
                board[tuple(new_index1)] = "1"
                
            elif new_index1[0] < 0 or board[tuple(new_index1)] == "X":
                print("This moves you out of bounds on the top!")
                crash_event()
                game_ongoing = False
                       
        elif p1_move == "down":
            
            new_index1[0] += 1 # New index 'row' one down
            
            # Legal row index is less than than m as m-1 is final row
            if new_index1[0] < m and board[tuple(new_index1)] != "X":
            
                board[index1] = "X"
                board[tuple(new_index1)] = "1"
                
            else:
                print("This moves you out of bounds on the bottom!")
                crash_event()
                game_ongoing = False
                
        print(board)
        
        # Update index of current position of player 1 after moving -
        # But before player 2's move in case they collide
        index1 = list(np.where(board == "1"))

                
        if game_ongoing == True: # If player 1 didn't crash
        
            index2 = np.where(board == "2")
            
            new_index2 = np.copy(index2)
            
            p2_move = input("Player 2: What is your move? (left,right,up,down) ")
            
            if p2_move == "left":
                    
                new_index2[1] -= 1 
                
                if (new_index2[1] >= 0 and board[tuple(new_index2)] != "X"): 
                
                    board[index2] = "X" 
                    board[tuple(new_index2)] = "2"        
                    
                else:
                    print("This moves you out of bounds on the left!")
                    crash_event()
                    game_ongoing = False
                    
            elif p2_move == "right":
                
                new_index2[1] += 1 
                
                if new_index2[1] < m and board[tuple(new_index2)] != "X": 
                
                    board[index2] = "X"
                    board[tuple(new_index2)] = "2"
                    
                else:
                    print("This moves you out of bounds on the right!")
                    crash_event()
                    game_ongoing = False
                
            elif p2_move == "up":
                
                new_index2[0] -= 1 
                
                if new_index2[0] >= 0 and board[tuple(new_index2)] != "X": 
                
                    board[index2] = "X"
                    board[tuple(new_index2)] = "2"
                    
                else:
                    print("This moves you out of bounds on the top!")
                    crash_event()
                    game_ongoing = False                
                
            elif p2_move == "down":
                
                new_index2[0] += 1 
                
                if new_index2[0] < m and board[tuple(new_index2)] != "X": 
                
                    board[index2] = "X"
                    board[tuple(new_index2)] = "2"
                    
                else:
                    print("This moves you out of bounds on the bottom!")
                    crash_event()
                    game_ongoing = False

            print(board)      
                    
            # Update index of current position of player 2 after moving in case of collision
            index2 = list(np.where(board == "2"))
                                                      
                    
            if index1 == index2: # Check that indexes after moves do not match
                print("Players Collide! It's a Draw! GAME OVER!!!")
                game_ongoing = False
                        


 
def crash_event():
    """Player crashes into wall or previously visited cell of either player"""
    
    print("You crashed! Better luck next time!")

 
 
 
 
run_game()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
