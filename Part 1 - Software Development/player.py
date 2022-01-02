#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:45:17 2021

@author: freddielloyd
"""


import random as random

import copy as copy


class PlayerClass:
    """A class to represent a player of the game"""
    
    def __init__(self, tron_game):
                
        self.m = tron_game.m
        
        self.board = tron_game.board
        

        
    def _ask_player_move(self, prompt):
        """Ask player for move and raise exception if move invalid."""
        while True:
            try:
                player_move = input(prompt).lower() #case doesn't matter
                if (player_move != "left" and player_move != "l"
                    and player_move != "right" and player_move != "r"
                    and player_move != "up" and player_move != "u"
                    and player_move != "down" and player_move != "d" and player_move != "s"):
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
        
        # self.difficulty = self._ask_cpu_difficulty(
        #         "Enter difficulty level of cpu player "
        #                     "(easy/medium/hard): >> "
        #         )
        
        self.difficulty = tron_game.difficulty
        
    def cpu_move(self, board):
        """Process computer move based on the difficulty chosen."""
        
        #current_index = np.where(self.board == "2")
        
        self.board = board
    
                    

        #new_index = np.copy(current_index)

        # RANDOM MOVE
        if self.difficulty == "easy" or self.difficulty == "e":
            
            cpu_move = random.choice(('left','right','up','down'))
            
            return cpu_move
        
        
        # 'RANDOM NON-SUICIDAL MOVE'
        elif self.difficulty == "medium" or self.difficulty == "m":
            
            possible_moves = self._legal_moves(self.board)
            
            if len(possible_moves) > 0:
            
                cpu_move = random.choice(possible_moves)

                return cpu_move
            
            
            elif len(possible_moves) == 0:
                
                cpu_move = random.choice(('left','right','up','down'))

                return cpu_move
            
        
        # Smart non-suicidal move - 
        # move in direction with most available spaces
        elif self.difficulty == "hard" or self.difficulty == "h":
            
            #print(self.board)
            
            possible_moves = self._legal_moves(self.board)
            
            #print(self.board)

            
            print("Number of legal moves is: " + str(len(possible_moves)))
            print(possible_moves)
            

            if len(possible_moves) == 0: # Crash in random direction
                
                cpu_move = random.choice(('left','right','up','down'))

                return cpu_move

            
            elif len(possible_moves) == 1: # Move in only available direction
                
                cpu_move = possible_moves[0]
            
                return cpu_move



            elif len(possible_moves) > 1:
            
                
                #current_index = np.where(self.board == "2")
                
                #print(current_index)
                
                for i in range(len(self.board)):
                    if "2" in self.board[i]:
                        current_index = [i, self.board[i].index("2")]
                
                current_row = int(current_index[0])
                
                current_column = int(current_index[1])
                
                
                number_pos_moves_right = 0
                number_pos_moves_left = 0
                
                number_pos_moves_up = 0
                number_pos_moves_down = 0
                
                for i in range(len(self.board)):
                    if i < current_column:
                        if self.board[current_row][i] == " ":
                            number_pos_moves_left += 1
                        else:
                            number_pos_moves_left = 0 #reset incrementer
                            
                    elif i > current_column:
                        if self.board[current_row][i] == " ":
                            number_pos_moves_right += 1
                        else:
                            break
                
                
                
                for i in range(len(self.board)):
                    if i < current_row:
                        if self.board[i][current_column] == " ":
                            number_pos_moves_up += 1
                        else:
                            number_pos_moves_up = 0 #reset incrementer
                            
                    elif i > current_row:
                        if self.board[i][current_column] == " ":
                            number_pos_moves_down += 1
                        else:
                            break
                        
            
                # number_pos_moves_left = (
                #     self.board[current_row][:current_column].count(" ")
                #     - self.board[current_row][:current_column].count("X")
                #     - self.board[current_row][:current_column].count("1")
                #     )
                
                # number_pos_moves_right = (
                #     self.board[current_row][current_column+1:].count(" ")
                #     - self.board[current_row][current_column+1:].count("X")
                #     - self.board[current_row][current_column+1:].count("1")
                #     )
                
                
                # t_board = list(zip(*self.board)) #transpose self.board
                
                # number_pos_moves_up = (
                #     t_board[current_column][:current_row].count(" ")
                #     - t_board[current_column][:current_row].count("X")
                #     - t_board[current_column][:current_row].count("1")
                #     )
                
                # number_pos_moves_down = (
                #     t_board[current_column][current_row+1:].count(" ")
                #     - t_board[current_column][current_row+1:].count("X")
                #     - t_board[current_column][current_row+1:].count("1")
                #     )
                
                
                
                # # Check for trails left and right of current position
                # if current_column > 0 and current_column < self.m - 1:
                
                #     if (self.board[current_row][current_column - 1] == "X"
                #     or self.board[current_row][current_column - 1] == "1"):
                #         number_pos_moves_left = 0
                    
                                
                #     if (self.board[current_row][current_column + 1] == "X"
                #     or self.board[current_row][current_column + 1] == "1"):
                #         number_pos_moves_right = 0
                        
                # # Check for trails left of final column
                # elif current_column == self.m - 1:
                    
                #     if (self.board[current_row][current_column - 1] == "X"
                #     or self.board[current_row][current_column - 1] == "1"):
                #         number_pos_moves_left = 0
                        
                # # Check for trails above and below current position
                # if current_row > 0 and current_row < self.m - 1:
             
                #     if (self.board[current_row - 1][current_column] == "X"
                #     or self.board[current_row - 1][current_column] == "1"):
                #         number_pos_moves_up = 0
                        
                                    
                #     if (self.board[current_row + 1][current_column] == "X"
                #     or self.board[current_row + 1][current_column] == "1"):
                #         number_pos_moves_down = 0
                        
                # # Check for trails above final row 
                # elif current_row == self.m - 1:
                    
                #     if (self.board[current_row - 1][current_column] == "X"
                #     or self.board[current_row - 1][current_column] == "1"):
                #         number_pos_moves_up = 0
                
                
                pos_moves = ["number_pos_moves_left",
                             "number_pos_moves_right",
                             "number_pos_moves_up",
                             "number_pos_moves_down"]
                
                number_pos_moves = [number_pos_moves_left,
                                    number_pos_moves_right,
                                    number_pos_moves_up,
                                    number_pos_moves_down]
                
                #print(self.board)
                
                print(number_pos_moves)
                
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
                        
                        
                        # # number_pos_moves_copy.pop(max_pos_moves)
                        
                        max_indexes.append(
                        number_pos_moves_copy.index(max_pos_moves)
                        )
                        
                        
                        # number_pos_moves_copy.pop()
                        
                        
     
                        
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
                    
                    print(cpu_move)
                    
                    pos_moves_next_turn = self._check_next_move(cpu_move)
                    
                    print("Pos moves next turn are: " + str(pos_moves_next_turn))
                    
                    if len(pos_moves_next_turn) == 0:
                    
                        max_directions.remove(cpu_move)
                    
                        cpu_move = random.choice((max_directions))
                    
                print("Chosen move is: " + str(cpu_move))
                    
                
                #print(self.board)
                    
                # new_index = np.copy(current_index)
                
                # board_copy = self.board[:]
                
                
                # # self.board = board_copy
                

                
                # #print(self.board)
                


                return cpu_move





            
    def _check_next_move(self,
                         cpu_move):
        """Check that cpu chosen move direction does not result in next
        move being suicidal."""
        
        board_copy = copy.deepcopy(self.board) # Need deep copy to copy list of lists
        
        
        for i in range(len(board_copy)):
            if "2" in board_copy[i]:
                current_index = [i, board_copy[i].index("2")]
                
        new_index = current_index[:]
                
        if cpu_move == "left":
            
            new_index[1] -= 1
            
            # Make array position before moving = "X"
            board_copy[current_index[0]][current_index[1]] = "X"
            board_copy[new_index[0]][new_index[1]] = "2" # Player 2's new position
            
        if cpu_move == "right":
            
            new_index[1] += 1
            
            # Make array position before moving = "X"
            board_copy[current_index[0]][current_index[1]] = "X"
            board_copy[new_index[0]][new_index[1]] = "2" # Player 2's new position
            
        if cpu_move == "up":
            
            new_index[0] -= 1
            
            # Make array position before moving = "X"
            board_copy[current_index[0]][current_index[1]] = "X"
            board_copy[new_index[0]][new_index[1]] = "2" # Player 2's new position
                       
        if cpu_move == "down":
            
            new_index[0] += 1
            
            # Make array position before moving = "X"
            board_copy[current_index[0]][current_index[1]] = "X"
            board_copy[new_index[0]][new_index[1]] = "2" # Player 2's new position
            
            
        pos_moves_next_turn = self._legal_moves(board_copy)  
            
        return pos_moves_next_turn
    
            
        
        
        
    def _legal_moves(self, board):
        """Return what legal directions the cpu can move in"""
        
        #current_index = np.where(self.board == "2")
        
        self.board = board
        
        for i in range(len(self.board)):          
            if "2" in self.board[i]:
                current_index = [i, self.board[i].index("2")]
                    
        
        possible_moves = []
        
        #number_legal_moves = 0

        #new_index = np.copy(current_index)
        
        new_index = current_index[:]
        
        new_index[1] -= 1 # Left
            
        if (new_index[1] >= 0
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            #number_legal_moves += 1
            
            possible_moves.append("left")

        new_index = current_index[:]
        
        new_index[1] += 1 # Right
            
        if (new_index[1] < self.m 
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            #number_legal_moves += 1
            
            possible_moves.append("right")

        new_index = current_index[:]
        
        new_index[0] -= 1 # Up
            
        if (new_index[0] >= 0
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            #number_legal_moves += 1
            
            possible_moves.append("up")


        new_index = current_index[:]

        new_index[0] += 1 # Down
        
        if (new_index[0] < self.m 
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            #number_legal_moves += 1
            
            possible_moves.append("down")


        return possible_moves

                        





class Error(Exception):
    """Base class for other exceptions"""
    
    
class InvalidDirectionError(Error):
    """Raise when input direction is invalid"""

    

        
