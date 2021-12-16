#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:44:59 2021

@author: freddielloyd
"""


#import numpy as np



 
class BoardClass:
    """A class to represent the board on which the game is played."""


    def __init__(self, tron_game):
        
        #self.m = self._ask_board_size("Enter the board size: >> ")
        
        self.m = tron_game.m

    
    def create_board(self):
        """Creates the initial board and returns it."""
                
        # self.board = (
        #     np.array([[" " for x in range (self.m)] for y in range(self.m)])
        #     )
        
        #board = [[" " for x in range (m)] for y in range(m)]
        self.board = [[" " for x in range (self.m)] for y in range(self.m)]
                
        #   = space not been to,
        # 1 = space of player 1
        # 2 = space of player 2
        # X = space visited by player 1 or player 2

        # Default starting position of player 1 - top left corner
        self.board[0][0] = "1"
        # Default starting position of player 2 - bottom right corner
        self.board[self.m-1][self.m-1] = "2"
        
        print("\nBoard of size (" + str(self.m) + "x" + str(self.m) + 
              ") created with default locations.")
              
        print("\nThe initial board is: ")
        
        return self.board
        
        
    def output_board(self):
        """Prints the board to be displayed to the player(s)."""
        
        #hash_array = np.array("#")
        
       # hash_array = ["#"]
        
        # Row of hashes of length m to 'frame' top and bottom of output board
        #hash_array_row = hash_array.repeat(self.m)
        
        hash_array_row = ["#"] * self.m
        
        print("#|" + "|".join(str(wall) for wall in hash_array_row) + "|#")
      
        for row in range(self.m):
            print("#|" + "|".join(str(num) for num in self.board[row]) + "|#")

        print("#|" + "|".join(str(wall) for wall in hash_array_row) + "|#\n")
        
        
        
    def process_move(self, 
                     tron_game, 
                     players_turn, 
                     move_direction,
                     opponent):
        """Process chosen move and update board"""
        
        if players_turn == "p1":
            #current_index = np.where(self.board == "1")
            
            for i in range(len(self.board)):
                if "1" in self.board[i]:
                    current_index = [i, self.board[i].index("1")]
    
        elif (players_turn == "p2"
              or players_turn == "cpu"):
            #current_index = np.where(self.board == "2")
            
            for i in range(len(self.board)):
                if "2" in self.board[i]:
                    current_index = [i, self.board[i].index("2")]
                    

        # Assign new index as copy of current index
        # This is to be able to change array elements of player position -
        # both before and after the move
        #new_index = np.copy(current_index)
    
        new_index = current_index[:]

        if move_direction == "left" or move_direction == "l":
                
            new_index[1] -= 1
            
            # Legal column index >= 0 as indexes start at 0
            if (new_index[1] >= 0
                and self.board[new_index[0]][new_index[1]] != "X"
                and self.board[new_index[0]][new_index[1]] != "1"
                and self.board[new_index[0]][new_index[1]] != "2"):
                
                self._update_board(players_turn, 
                                   current_index, 
                                   new_index)
                    
                return "Legal"
                
            #elif new_index[1] < 0:
                #self._crash_event_oob(players_turn, 
                #                      opponent)
            else:
                return "Crash"
                             
        elif move_direction == "right" or move_direction == "r":
            
            new_index[1] += 1
            
            # Legal column index is < m as m-1 is final column
            if (new_index[1] < self.m
                and self.board[new_index[0]][new_index[1]] != "X"
                and self.board[new_index[0]][new_index[1]] != "1"
                and self.board[new_index[0]][new_index[1]] != "2"):
            
                self._update_board(players_turn, 
                                   current_index, 
                                   new_index)
                    
                return "Legal"
                
            else:
                return "Crash"
                          
        elif move_direction == "up" or move_direction == "u":
            
            new_index[0] -= 1
            
            # Legal row index is >= 0 as indexes start at 0
            if (new_index[0] >= 0
                and self.board[new_index[0]][new_index[1]] != "X"
                and self.board[new_index[0]][new_index[1]] != "1"
                and self.board[new_index[0]][new_index[1]] != "2"):
            
                self._update_board(players_turn, 
                                   current_index, 
                                   new_index)
            
                return "Legal"

            else:
                return "Crash"
                 
        elif move_direction == "down" or move_direction == "d":
            
            new_index[0] += 1
            
            # Legal row index is less than than m as m-1 is final row
            if (new_index[0] < self.m 
                and self.board[new_index[0]][new_index[1]] != "X"
                and self.board[new_index[0]][new_index[1]] != "1"
                and self.board[new_index[0]][new_index[1]] != "2"):
            
                self._update_board(players_turn, 
                                   current_index, 
                                   new_index)
                    
                return "Legal"
                 
            else:
                return "Crash"
            
        elif move_direction == "s":
            return "Legal"

        
        
        # if p1_move == "Crash":
        #         self._crash_event(players_turn,
        #                           self.opponent)
         
        # elif p1_move == "Legal":
        #         self.board_class.output_board()
        
        
    # def _move_legal(self,
    #                 current_index,
    #                 new_index):
        
    
    def _update_board(self,
                     players_turn,
                     current_index,
                     new_index):
        
    
        # Make array position before moving = "X"
        self.board[current_index[0]][current_index[1]] = "X"
        
        if players_turn == "p1":
            self.board[new_index[0]][new_index[1]] = "1" # Player 1's new position
        elif (players_turn == "p2"
              or players_turn == "cpu"):
            self.board[new_index[0]][new_index[1]] = "2" # Player 2's new position

        
    
        
    def _crash_event(self, 
                     players_turn,
                     opponent):
        """Display output message if a player has crashed out of bounds,
        into other player, or into the trail of either player."""
                
        if players_turn == "p1":
            
            if opponent == "player":
                print("\nPlayer 1 crashed! Player 2 wins!"
                      "\nTaking you back to game menu!")

            elif opponent == "cpu":
                print("\nPlayer 1 crashed! Computer wins!"
                      "\nTaking you back to game menu!")
            
        elif players_turn == "p2":
            print("\nPlayer 2 crashed! Player 1 wins!"
                  "\nTaking you back to game menu!")

        elif players_turn == "cpu":
            print("\nComputer crashed! Player 1 wins!"
                  "\nTaking you back to game menu!")
        
        
    # def _crash_players_collision(self, 
    #                              players_turn, 
    #                              opponent):
    #     """Check equality of current player indices after each move
    #     and end game if equal"""
 
    #     if players_turn == "p1":
            
    #         if opponent == "player":
    #             print ("\nPlayer 1 crashed into Player 2! Player 2 wins!" 
    #                    "\nTaking you back to game menu!")
            
    #         elif opponent == "cpu":
    #             print ("\nPlayer 1 crashed into the computer! Computer wins!"
    #                    "\nTaking you back to game menu!")
            
    #     elif players_turn == "p2":
    #         print ("\nPlayer 2 crashed into Player 1! Player 1 wins!" 
    #                "\nTaking you back to game menu!")
            
    #     elif players_turn == "cpu":
    #         print ("\nComputer crashed into Player 1! Player 1 wins!" 
    #                "\nTaking you back to game menu!")
                

        
        

            


    
