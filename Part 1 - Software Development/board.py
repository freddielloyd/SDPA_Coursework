#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:44:59 2021

@author: Freddie Lloyd

Part 1: Software Development

Contains the board class which possessess methods to manage the board of the 
Tron game, including the initial creation and processing of moves.
"""

import copy as copy

class BoardClass:
    """
    A class to represent the board on which the game is played.
    
        
    Attributes:
        current_game - The current game of Tron being played   
    """

    def __init__(self, current_game):
        
        self.m = current_game.m

    def create_board(self):
        """
        Creates the initial board and returns it.
        
        " "   = space not been to,
        "1" = position of player 1
        "2" = position of player 2
        "X" = space visited by player 1 or player 2
        
        Returns:
            self.board - the initial board created
        """
                
        self.board = [[" " for x in range (self.m)] for y in range(self.m)]

        # Default starting position of player 1 - top left corner
        self.board[0][0] = "1"
        # Default starting position of player 2 - bottom right corner
        self.board[self.m-1][self.m-1] = "2"
        
        print("\nBoard of size (" + str(self.m) + "x" + str(self.m) + 
              ") created with default locations.")
              
        print("\nThe initial board is: ")
        
        return self.board
    

    def output_board(self):
        """Prints the board to the console."""
 
        # Row of hashes of length m to 'frame' top and bottom of output board
        hash_array_row = ["#"] * self.m
        
        print("#|" + "|".join(str(wall) for wall in hash_array_row) + "|#")
      
        for row in range(self.m):
            print("#|" + "|".join(str(num) for num in self.board[row]) + "|#")

        print("#|" + "|".join(str(wall) for wall in hash_array_row) + "|#\n")
        
        
        
    def process_move(self, 
                     players_turn, 
                     move_direction):
        """
        Process chosen player move and return its legality.
        
        Parameters: 
            players_turn - Which players turn it is to move
            move_direction - The chosen direction of the player
            
        Returns:
            move_result - The outcome of the move
        """
        
        if players_turn == "p1":
            
            for i in range(len(self.board)):
                if "1" in self.board[i]:
                    current_index = [i, self.board[i].index("1")]
    
        elif (players_turn == "p2"
              or players_turn == "cpu"):
            
            for i in range(len(self.board)):
                if "2" in self.board[i]:
                    current_index = [i, self.board[i].index("2")]
                    

        # Assign new index as copy of current index to be able to update
        # board with both new and old positions 
    
        new_index = current_index[:]

        if move_direction == "left" or move_direction == "l":
                
            new_index[1] -= 1
            
            # Legal column index >= 0 as indexes start at 0
            if new_index[1] >= 0:
                
                if self.board[new_index[0]][new_index[1]] == "1":
                    move_result = "potential_draw"

                elif (self.board[new_index[0]][new_index[1]] != "X"
                    and self.board[new_index[0]][new_index[1]] != "2"):
            
                    self._update_board(players_turn, 
                                       current_index, 
                                       new_index)
                    
                    move_result = "legal"
                
                elif (self.board[new_index[0]][new_index[1]] == "X"
                      or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"
                
            elif new_index[1] < 0:
                move_result = "crash"
                             
        elif move_direction == "right" or move_direction == "r":
            
            new_index[1] += 1
            
            # Legal column index is < m as m-1 is final column
            if new_index[1] < self.m:
                
                if self.board[new_index[0]][new_index[1]] == "1":
                    move_result = "potential_draw"

                elif (self.board[new_index[0]][new_index[1]] != "X"
                    and self.board[new_index[0]][new_index[1]] != "2"):
            
                    self._update_board(players_turn, 
                                       current_index, 
                                       new_index)
                                        
                    move_result = "legal"  
                                
                elif (self.board[new_index[0]][new_index[1]] == "X"
                      or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"
                                
            elif new_index[1] >= self.m:
                move_result = "crash"
                          
        elif move_direction == "up" or move_direction == "u":
            
            new_index[0] -= 1
            
            # Legal row index is >= 0 as indexes start at 0
            if new_index[0] >= 0:
                
                if self.board[new_index[0]][new_index[1]] == "1":
                    move_result = "potential_draw"

                elif (self.board[new_index[0]][new_index[1]] != "X"
                    and self.board[new_index[0]][new_index[1]] != "2"):
            
                    self._update_board(players_turn, 
                                       current_index, 
                                       new_index)
            
                    move_result = "legal"
                                
                elif (self.board[new_index[0]][new_index[1]] == "X"
                      or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"

            elif new_index[0] < 0:
                move_result = "crash"
                 
        elif move_direction == "down" or move_direction == "d":
            
            new_index[0] += 1
            
            # Legal row index is less than than m as m-1 is final row
            if new_index[0] < self.m:
                
                if self.board[new_index[0]][new_index[1]] == "1":
                    move_result = "potential_draw"
                
                elif (self.board[new_index[0]][new_index[1]] != "X"
                    and self.board[new_index[0]][new_index[1]] != "2"):
            
                    self._update_board(players_turn, 
                                       current_index, 
                                       new_index)
                        
                    move_result = "legal"           
                                
                elif (self.board[new_index[0]][new_index[1]] == "X"
                      or self.board[new_index[0]][new_index[1]] == "2"):                    
                    
                    move_result = "crash"
                                 
            elif new_index[0] >= self.m:
                move_result = "crash"
                
        return move_result


    
    def _update_board(self,
                     players_turn,
                     current_index,
                     new_index):
        """
        Update board with new position of player after move,
        as well as marking the position just moved from.
        
        Parameters: 
            players_turn - Which players turn it is to move
            current_index - The current board position of the player
            new_index - The new board position of the player

        """
    
        # Mark board position moved from
        self.board[current_index[0]][current_index[1]] = "X"
        
        # Update board with new position
        if players_turn == "p1":
            self.board[new_index[0]][new_index[1]] = "1" 
        elif (players_turn == "p2"
              or players_turn == "cpu"):
            self.board[new_index[0]][new_index[1]] = "2"

        
    
        
    def _crash_event(self, 
                     players_turn,
                     game_type):
        """
        Display output message if a player has crashed out of bounds,
        into other player, or into the trail of either player.
        
        Parameters: 
            players_turn - Which players turn it is to move
            game_type - Game against player or computer
        
        """
                
        if players_turn == "p1":
            
            if game_type == "player":
                print("\nPlayer 1 crashed! Player 2 wins!"
                      "\nTaking you back to game menu!")

            elif game_type == "computer":
                print("\nPlayer 1 crashed! Computer wins!"
                      "\nTaking you back to game menu!")
            
        elif players_turn == "p2":
            print("\nPlayer 2 crashed! Player 1 wins!"
                  "\nTaking you back to game menu!")

        elif players_turn == "cpu":
            print("\nComputer crashed! Player 1 wins!"
                  "\nTaking you back to game menu!")
            
            
    def _draw_outcome(self):  
        """Display draw message if player 2 or computer collides into
        player 1 during simultaenous game."""
    
        print("\nPlayers crashed into each other! Its a draw!"
              "\nTaking you back to game menu!")
        
        
        
        
        
        
        
    def create_hex_board(self):
        """
        Creates the initial hex board and returns it.
        
        " "   = space not been to,
        "1" = position of player 1
        "2" = position of player 2
        "X" = space visited by player 1 or player 2
        
        Returns:
            self.board - the initial hex board created
        """
                
        
        # BOARD SIZE MUST BE AN ODD NUMBER SO PUT EXCEPTION FOR THIS
        # and at least 5 or greater
    
        
        self.board = [[" " for x in range (self.m)] for y in range(self.m)]
        self.board[0][0] = "N" #top left corner
        self.board[self.m-1][self.m-1] = "N" #bottom right corner
              
        
        self.board[0][(self.m//2)] = "1" # Top left corner of hex
        self.board[self.m-1][(self.m//2)] = "2" # Bottom right corner of hex
        #self.board[self.m-1][self.m-1] = "2" # Bottom right corner of hex

        final_row = self.m-1
        
        row = self.m-1
        
        l = self.m
        
        while (l//2) > 1:
            self.board[0][(l//2)-1] = "N" #final top row needed
            self.board[(l//2)-1][0] = "N" #final bottom row needed

            self.board[1][(l//2)-2] = "N"
            
            if l >= 9:
                self.board[2][(l//2)-3] = "N"
                
            if l >= 11:
                self.board[3][(l//2)-4] = "N"
            
            self.board[final_row][(l//2)+2] = "N" #final bottom row needed
            self.board[row-1][self.m-1] = "N" 
            
            #self.board[row-1][(l//2)-2] = "O"
            self.board[self.m-2][self.m-2] = "N"

            # if l >= 9:
            #     self.board[row-1][(l//2)-3] = "O"
                
            # if l >= 11:
            #     self.board[row-1][(l//2)-4] = "O"

            # self.board[final_row][(l//2)-1] = "O"
            # self.board[row-1][0] = "O"
            
            l = l - 2
            
            row = row - 1
        
        
        # board = [[" " for x in range (m)] for y in range(m)]
        # board[0][0] = "N" #top left corner
        # board[m-1][m-1] = "N" #bottom right corner     
        
        # board[0][(m//2)] = "1" # Top left corner of hex
        # board[m-1][(m//2)] = "2" # Bottom right corner of hex

        # final_row = m-1
        
        # row = m-1
        
        # l = m
        
        # while (l//2) > 1:
        #     board[0][(l//2)-1] = "N" #final top col needed
        #     board[(l//2)-1][0] = "N" #final bottom row needed

        #     board[1][(l//2)-2] = "N"
            
        #     if l >= 9:
        #         board[2][(l//2)-3] = "N"
                
        #     if l >= 11:
        #         board[3][(l//2)-4] = "N"
            
        #     board[final_row][(l//2)+2] = "N" #final bottom row needed
        #     board[row-1][m-1] = "N" #last col
            
        #     #board[row-1][(l//2)+2] = "N"
        #     board[m-2][m-2] = "N"

        #     # if l >= 9:
        #     #     self.board[row-1][(l//2)-3] = "O"
                
        #     # if l >= 11:
        #     #     self.board[row-1][(l//2)-4] = "O"

        #     #board[row-1][] = "O"          
        #     l = l - 2
        #     row = row - 1
            
        # board
            

        print("\nBoard of size (" + str(self.m) + "x" + str(self.m) + 
              ") created with default locations.")
              
        print("\nThe initial board is: ")
        
        return self.board



    
    def output_hex_board(self):
        """Prints the hex board to the console."""
 
        fboard = copy.deepcopy(self.board)
        
        # a.append(a.pop(0))
        
        # for x in range(m):
        #     fboard[m-1][x+3] = fboard[m-1][x]
        
        new_final_row = fboard[self.m-1][:(self.m//2)+1] #shift four three across
        fboard[self.m-1][self.m//2:] = new_final_row
        
        new_2ndfinal_row = fboard[self.m-2][:(self.m//2)+2] #shift five two across
        fboard[self.m-2][(self.m//2)-1:] = new_2ndfinal_row
        
        new_3rdfinal_row = fboard[self.m-3][:(self.m//2)+3] #shift six one across
        fboard[self.m-3][(self.m//2)-2:] = new_3rdfinal_row
        

        #print(fboard)
        
        fboard[0][0] = "O" #top left corner
        fboard[self.m-1][0] = "O" #bottom left corner
        
        final_row = self.m-1
        
        row = self.m-1
        
        l = self.m
        
        while (l//2) > 1:
            fboard[0][(l//2)-1] = "O" #final top row needed
            fboard[(l//2)-1][0] = "O" #final bottom row needed
            fboard[1][(l//2)-2] = "O"          
            if l >= 9:
                fboard[2][(l//2)-3] = "O"              
            if l >= 11:
                fboard[3][(l//2)-4] = "O"          
            fboard[final_row][(l//2)-1] = "O" #final bottom row needed
            fboard[row-1][0] = "O" #first col         
            fboard[row-1][(l//2)-2] = "O"
            if l >= 9:
                fboard[row-1][(l//2)-3] = "O"                
            if l >= 11:
                fboard[row-1][(l//2)-4] = "O"
            fboard[final_row][(l//2)-1] = "O"
            fboard[row-1][0] = "O"   
            
            #fboard[final_row][(l//2)+2] = " " #final bottom row needed
            #fboard[row-1][self.m-1] = " " 
            
            #fboard[m-2][m-2] = " "
            
            #fboard[m-1][m-1] = " "

            l = l - 2         
            row = row - 1
            
        #print(fboard)

        for y in range(self.m):
            
            # Display the top half of the hexagon:
            for x in range(self.m):
    
                if fboard[y][x] == "O":
                    print('   ', end='')
                    #print('\__/  ', end='')
                    
                elif fboard[y][x] != "O":
                    
                    if y == 0:
        
                        if x != self.m-1:
                            print("/ " +"  ".join(fboard[y][x]) + "\  ", end='')
                            
                        elif x == self.m-1:
                            print("/ " +"  ".join(fboard[y][x]) + "\\", end='')
                        
                    elif y > 0:
                        print("/ " +"  ".join(fboard[y][x]) + "\  ", end='')      
            print()
        
            # Display the bottoself.m half of the hexagon:
            for x in range(self.m):
                
                if fboard[y][x] == "O":
                    print('   ', end='')
                    
                elif fboard[y][x] != "O":
                    
                    if y != self.m-1:
                        
                        if x != self.m-1:
                            print('\__/__', end='')
                            
                        elif x == self.m-1:
                            print('\__/', end='')
                            
                    if y == self.m-1:
                            print('\__/  ', end='')       
        
            print()
            
            
            
    def process_hex_move(self, 
                         players_turn, 
                         move_direction):
        """
        Process chosen player hex move and return its legality.
        
        Parameters: 
            players_turn - Which players turn it is to move
            move_direction - The chosen direction of the player
            
        Returns:
            move_result - The outcome of the move
        """
        
        if players_turn == "p1":
            
            for i in range(len(self.board)):
                if "1" in self.board[i]:
                    current_index = [i, self.board[i].index("1")]
            
            # for i in range(len(board)):
            #     if "1" in board[i]:
            #         current_index = [i, board[i].index("1")]
    
        elif (players_turn == "p2"
              or players_turn == "cpu"):
            
            for i in range(len(self.board)):
                if "2" in self.board[i]:
                    current_index = [i, self.board[i].index("2")]
                    

        # Assign new index as copy of current index to be able to update
        # board with both new and old positions 
    
        new_index = current_index[:]

        if move_direction == "left" or move_direction == "l":
            
                
            new_index[1] -= 1
            
            if new_index[1] >= 0:
            
                if (self.board[new_index[0]][new_index[1]] == "X"
                    or self.board[new_index[0]][new_index[1]] == "N"
                    or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"
                
                elif self.board[new_index[0]][new_index[1]] == "1":
                        move_result = "potential_draw"
                
                elif self.board[new_index[0]][new_index[1]] == " ":
                        self._update_board(players_turn, 
                                           current_index, 
                                           new_index)
                        
                        move_result = "legal"
                        
            elif new_index[1] < 0:
                move_result = "crash"
                    
                             
        elif move_direction == "right" or move_direction == "r":
            
            new_index[1] += 1
            
            # Legal column index is < m as m-1 is final column
            if new_index[1] < self.m:
                
                if (self.board[new_index[0]][new_index[1]] == "X"
                    or self.board[new_index[0]][new_index[1]] == "N"
                    or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"
                
                elif self.board[new_index[0]][new_index[1]] == "1":
                        move_result = "potential_draw"
                
                elif self.board[new_index[0]][new_index[1]] == " ":
                        self._update_board(players_turn, 
                                           current_index, 
                                           new_index)
                        
                        move_result = "legal"
                                
            elif new_index[1] >= self.m:
                move_result = "crash"
                
                
        elif (move_direction == "up left" or move_direction == "left up"
              or move_direction == "ul" or move_direction == "lu"):
            
            new_index[0] -= 1 # One up
            #new_index[1] -= 1 # One left
                        
            if new_index[0] >= 0:
                
                if (self.board[new_index[0]][new_index[1]] == "X"
                    or self.board[new_index[0]][new_index[1]] == "N"
                    or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"
                
                elif self.board[new_index[0]][new_index[1]] == "1":
                        move_result = "potential_draw"
                
                elif self.board[new_index[0]][new_index[1]] == " ":
                        self._update_board(players_turn, 
                                           current_index, 
                                           new_index)
                        
                        move_result = "legal"            

            elif new_index[0] < 0:
                move_result = "crash"
                
                                                     
        elif (move_direction == "up right" or move_direction == "right up"
              or move_direction == "ur" or move_direction == "ru"):
            
            new_index[0] -= 1 # One up
            new_index[1] += 1 # One right
                        
            if new_index[0] >= 0 and new_index[1] < self.m:
                
                if (self.board[new_index[0]][new_index[1]] == "X"
                    or self.board[new_index[0]][new_index[1]] == "N"
                    or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"
                
                elif self.board[new_index[0]][new_index[1]] == "1":
                        move_result = "potential_draw"
                
                elif self.board[new_index[0]][new_index[1]] == " ":
                        self._update_board(players_turn, 
                                           current_index, 
                                           new_index)
                        
                        move_result = "legal"            

            elif new_index[0] < 0 or new_index[1] >= self.m: 
                move_result = "crash"
                 
                
        elif (move_direction == "down left" or move_direction == "left down"
              or move_direction == "dl" or move_direction == "ld"):
            
            new_index[0] += 1 # One down
            new_index[1] -= 1 # One left
                        
            if new_index[0] < self.m and new_index[1] >= 0:
                
                if (self.board[new_index[0]][new_index[1]] == "X"
                    or self.board[new_index[0]][new_index[1]] == "N"
                    or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"
                
                elif self.board[new_index[0]][new_index[1]] == "1":
                        move_result = "potential_draw"
                
                elif self.board[new_index[0]][new_index[1]] == " ":
                        self._update_board(players_turn, 
                                           current_index, 
                                           new_index)
                        
                        move_result = "legal"            

            elif new_index[0] >= self.m or new_index[1] < 0:
                move_result = "crash"
                
                
    
                move_result = "crash"
                 
                
        elif (move_direction == "down right" or move_direction == "right down"
              or move_direction == "dr" or move_direction == "rd"):
            
            new_index[0] += 1 # One down
            #new_index[1] += 1 # One right
                        
            if new_index[0] < self.m:
                
                if (self.board[new_index[0]][new_index[1]] == "X"
                    or self.board[new_index[0]][new_index[1]] == "N"
                    or self.board[new_index[0]][new_index[1]] == "2"):
                    
                    move_result = "crash"
                
                elif self.board[new_index[0]][new_index[1]] == "1":
                        move_result = "potential_draw"
                
                elif self.board[new_index[0]][new_index[1]] == " ":
                        self._update_board(players_turn, 
                                           current_index, 
                                           new_index)
                        
                        move_result = "legal"            

            elif new_index[0] >= self.m:
                move_result = "crash"
                

        return move_result
                
         
