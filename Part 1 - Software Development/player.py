#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:45:17 2021

@author: Freddie Lloyd

Part 1: Software Development

Contains the player class and its children classes human and computer,
each possessing methods for the respective player to make a move in 
the Tron game.

"""


import random as random

import copy as copy


class PlayerClass:
    """
    A class to represent a player in the Tron game.
    
    Attributes:
        current_game - The current game of Tron being played   
    """
    
    def __init__(self, current_game):
                
        self.m = current_game.m
        
        self.board = current_game.board   

    def _ask_player_move(self, prompt):
        """
        Asks player for move, raises exception if invalid.
        
        Parameters: 
            prompt - The question to be asked to the player
            
        Returns:
            player_move - The player's chosen move
        """
        while True:
            try:
                player_move = input(prompt).lower() # Case of input doesn't matter
                if (player_move != "left" and player_move != "l"
                    and player_move != "right" and player_move != "r"
                    and player_move != "up" and player_move != "u"
                    and player_move != "down" and player_move != "d"):
                        raise InvalidDirectionError
                    
            except InvalidDirectionError:
                print("\nDirection must be left (l), right (r), up (u) or down (d)! "
                      "Please enter a valid direction!")
            else:
                return player_move
            
            
    def _ask_player_hex_move(self, prompt):
        """
        Asks player for move in a hexagon game, raises exception 
        if invalid.
        
        Parameters: 
            prompt - The question to be asked to the player
            
        Returns:
            player_move - The player's chosen move
        """
        while True:
            try:
                player_move = input(prompt).lower() # Case of input doesn't matter
                if (player_move != "left" and player_move != "l"
                    and player_move != "right" and player_move != "r"
                    and player_move != "up left" and player_move != "left up"
                    and player_move != "ul" and player_move != "lu"
                    and player_move != "up right" and player_move != "right up"
                    and player_move != "ur" and player_move != "ru"
                    and player_move != "down left" and player_move != "left down"
                    and player_move != "dl" and player_move != "ld"
                    and player_move != "down right" and player_move != "right down"
                    and player_move != "dr" and player_move != "rd"):
                        raise InvalidDirectionError
                    
            except InvalidDirectionError:
                print("\nDirection must be left (l), right (r), up left (ul/lu), "
                      "up right (ur/ru), down left (dl/ld) or down right (dr/rd)! ")
                      
                print("\nPlease enter a valid direction!")
            else:
                return player_move
            

    
class HumanPlayer(PlayerClass):
    """
    A class to represent a human player in the Tron game,
    inherits from the player class.
    
    Attributes:
        current_game - The current game of Tron being played  
    """
    
    def __init__(self, current_game):
        
        super().__init__(current_game)
    
    def player_move(self, players_turn):
        """
        Asks human player for their move.
        
        Parameters: 
            players_turn - Which player's turn it is to make a move
            
        Returns:
            player_move - The player's chosen move
        """
        
        if players_turn == "p1":
            
            player_move = self._ask_player_move(
                "Player 1: What is your move? >> "
                )

        elif players_turn == "p2":
            
            player_move = self._ask_player_move(
                "Player 2: What is your move? >> "
                )
            
        return player_move
    
    def player_hex_move(self, players_turn):
        """
        Asks human player for their move in a hex game.
        
        Parameters: 
            players_turn - Which player's turn it is to make a move
            
        Returns:
            player_move - The player's chosen move
        """
        
        if players_turn == "p1":
            
            player_move = self._ask_player_hex_move(
                "Player 1: What is your move? >> "
                )

        elif players_turn == "p2":
            
            player_move = self._ask_player_hex_move(
                "Player 2: What is your move? >> "
                )
            
        return player_move
    
    
    
            


class ComputerPlayer(PlayerClass):
    """
    A class to represent a computer player in the Tron game,
    inherits from the player class.
    
    Attributes:
        current_game - The current game of Tron being played 
    """
        
    def __init__(self, 
                 current_game):
        
        super().__init__(current_game)
        
        #self.difficulty = current_game.difficulty
        
    def cpu_move(self, 
                 board,
                 difficulty):
        """
        Determines computer player's move based on chosen difficulty level.
        
        Parameters: 
            board - The current board state before the cpu's move
            difficulty - The selected difficulty level of the computer player
            
        Returns:
            cpu_move - The direction selected for the computer player to move in
        """

        self.board = board

        # Easy difficulty is a random move in any direction
        if difficulty == "easy" or difficulty == "e":
            
            cpu_move = random.choice(('left','right','up','down'))
            
        
        # Medium diffiulty is a random non-suicidal move
        elif difficulty == "medium" or difficulty == "m":
            
            # Retrieve non-suicidal directions
            possible_moves = self._legal_moves(self.board)
            
            if len(possible_moves) > 0:

                cpu_move = random.choice(possible_moves)
            
            elif len(possible_moves) == 0:
                
                cpu_move = random.choice(('left','right','up','down'))
            
        
        # Hard difficulty is a smart move in the direction with most available 
        # spaces, whilst avoiding moves that in result in suicide next turn.
        elif difficulty == "hard" or difficulty == "h":
            
            possible_moves = self._legal_moves(self.board)

            # print("Number of legal moves is: " + str(len(possible_moves)))
            # print(possible_moves)

            if len(possible_moves) == 0:
                
                # Crash in random direction
                cpu_move = random.choice(('left','right','up','down'))

            
            elif len(possible_moves) == 1:
                
                # Move in only available direction
                cpu_move = possible_moves[0]


            elif len(possible_moves) > 1:
                
                cpu_move = self._choose_between_moves()

        # Return chosen move of any difficulty level
        return cpu_move
    
    
    
    def cpu_hex_move(self, 
                     board,
                     difficulty):
        """
        Determines computer player's move in a hexagon game based on chosen 
        difficulty level.
        
        Parameters: 
            board - The current board state before the cpu's move
            difficulty - The selected difficulty level of the computer player
            
        Returns:
            cpu_move - The direction selected for the computer player to move in
        """

        self.board = board

        # Easy difficulty is a random move in any direction
        if difficulty == "easy" or difficulty == "e":
            
            cpu_move = random.choice(('left',
                                      'right',
                                      'up left',
                                      'up right',
                                      'down left',
                                      'down right'))
            
        
        # Medium diffiulty is a random non-suicidal move
        elif difficulty == "medium" or difficulty == "m":
            
            # Retrieve non-suicidal directions
            possible_moves = self._legal_hex_moves(self.board)
            
            print(self.board)
            
            if len(possible_moves) > 0:

                cpu_move = random.choice(possible_moves)
            
            elif len(possible_moves) == 0:
                
                cpu_move = random.choice(('left',
                                          'right',
                                          'up left',
                                          'up right',
                                          'down left',
                                          'down right'))            
            
        # Hard difficulty is a smart move in the direction with most available 
        # spaces, whilst avoiding moves that in result in suicide next turn.
        elif difficulty == "hard" or difficulty == "h":
            
            possible_moves = self._legal_hex_moves(self.board)

            # print("Number of legal moves is: " + str(len(possible_moves)))
            # print(possible_moves)

            if len(possible_moves) == 0:
                
                # Crash in random direction
                cpu_move = random.choice(('left',
                                          'right',
                                          'up left',
                                          'up right',
                                          'down left',
                                          'down right'))  

            
            elif len(possible_moves) == 1:
                
                # Move in only available direction
                cpu_move = possible_moves[0]


            elif len(possible_moves) > 1:
                
                cpu_move = self._choose_between_hex_moves()

        # Return chosen move of any difficulty level
        return cpu_move
    
    
            
        
    def _legal_moves(self, board):
        """Given the state of a board, returns what legal directions the cpu
        player can move in on a regular square board.
        
        Parameters: 
            board - The board to check the possible legal moves for
            
        Returns:
            possible_moves - The legal directions that can be moved in
        """
        
        # Receives a board argument to be able to check legal moves
        # for either the actual board or a copy board
        self.board = board
        
        for i in range(len(self.board)):          
            if "2" in self.board[i]:
                current_index = [i, self.board[i].index("2")]
                    
        # Create empty list to append legal moves to
        possible_moves = []
        
        # Create a copy of current index of player 2 to be able to check
        # each direction indiviually
        new_index = current_index[:]
        
        # Check left move
        new_index[1] -= 1
            
        if (new_index[1] >= 0
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("left")

        new_index = current_index[:]
        
        # Check right move
        new_index[1] += 1
            
        if (new_index[1] < self.m 
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("right")

        new_index = current_index[:]
        
        # Check up move
        new_index[0] -= 1
            
        if (new_index[0] >= 0
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("up")

        new_index = current_index[:]

        # Check down move
        new_index[0] += 1
        
        if (new_index[0] < self.m 
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("down")

        return possible_moves
    
          
    def _legal_hex_moves(self, board):
        """Given the state of a board, returns what legal directions the cpu
        player can move in on a hexagon board.
        
        Parameters: 
            board - The board to check the possible legal moves for
            
        Returns:
            possible_moves - The legal directions that can be moved in
        """
        
        # Receives a board argument to be able to check legal moves
        # for either the actual board or a copy board
        self.board = board
        
        for i in range(len(self.board)):          
            if "2" in self.board[i]:
                current_index = [i, self.board[i].index("2")]
                    
        # Create empty list to append legal moves to
        possible_moves = []
        
        # Create a copy of current index of player 2 to be able to check
        # each direction indiviually
        new_index = current_index[:]
        
        # Check left move
        new_index[1] -= 1
            
        if (new_index[1] >= 0
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "N"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("left")

        new_index = current_index[:]
        
        # Check right move
        new_index[1] += 1
            
        if (new_index[1] < self.m 
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "N"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("right")

        new_index = current_index[:]
        
        # Check up left move
        new_index[0] -= 1
            
        if (new_index[0] >= 0
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "N"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("up left")

        new_index = current_index[:]

        # Check up right move
        new_index[0] -= 1 
        new_index[1] += 1 
        
        if (new_index[0] >= 0
            and new_index[1] < self.m
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "N"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("up right")
    
        new_index = current_index[:]
        
        # Check down left move
        new_index[0] += 1
        new_index[1] -= 1
            
        if (new_index[0] < self.m
            and new_index[1] >= 0
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "N"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("down left")

        new_index = current_index[:]

        # Check down right move
        new_index[0] += 1
        
        if (new_index[0] < self.m
            and self.board[new_index[0]][new_index[1]] != "X"
            and self.board[new_index[0]][new_index[1]] != "N"
            and self.board[new_index[0]][new_index[1]] != "1"):
            
            possible_moves.append("down right")


        return possible_moves
    
    
    
    def _choose_between_moves(self):
        """
        Assesses which move the computer should make and returns it.
        
        Returns:
            cpu_move - the selected 'best' move for the computer
        """
        
        # Retrieve current position of player 2
        for i in range(len(self.board)):
            if "2" in self.board[i]:
                 current_index = [i, self.board[i].index("2")]
         
        current_row = int(current_index[0])
        current_column = int(current_index[1])
         
         # Check for number of possible moves directly left and right
        number_pos_moves_right = 0
        number_pos_moves_left = 0
        
        for i in range(len(self.board)):
            
            if i < current_column:
                if self.board[current_row][i] == " ":
                    number_pos_moves_left += 1
                else:
                    number_pos_moves_left = 0
                    
            elif i > current_column:
                if self.board[current_row][i] == " ":
                    number_pos_moves_right += 1
                else:
                    break
        
        # Check for number of legal moves directly up and down
        number_pos_moves_up = 0
        number_pos_moves_down = 0
        
        for i in range(len(self.board)):
            
            if i < current_row:
                if self.board[i][current_column] == " ":
                    number_pos_moves_up += 1
                else:
                    number_pos_moves_up = 0
                    
            elif i > current_row:
                if self.board[i][current_column] == " ":
                    number_pos_moves_down += 1
                else:
                    break
                

        pos_moves = ["left", "right", "up", "down"]
        
        # Purposely same order as pos_moves so can retrieve later
        number_pos_moves = [number_pos_moves_left,
                            number_pos_moves_right,
                            number_pos_moves_up,
                            number_pos_moves_down]
               
        max_pos_moves = max(number_pos_moves)


        # If there is only one max direction
        if number_pos_moves.count(max_pos_moves) == 1:
            
            # Retrieve 'LRUD'
            max_index = number_pos_moves.index(max_pos_moves)
        
            cpu_move = pos_moves[max_index]
        
        
        # If there is more than one max direction
        elif number_pos_moves.count(max_pos_moves) > 1:
            
            # Make a copy so original list unaffected
            number_pos_moves_copy = number_pos_moves.copy()
            
            # Retrieve indexes within pos_moves of maximum directions
            max_indexes = []
            
            while max_pos_moves in number_pos_moves_copy:
                
                max_indexes.append(
                number_pos_moves_copy.index(max_pos_moves)
                )
                
                # Mark position of max move already appended with N/A
                number_pos_moves_copy[max_indexes[0]] = "N/A"
                
                if len(max_indexes) == 2:
                
                    number_pos_moves_copy[max_indexes[1]] = "N/A"
                    
                elif len(max_indexes) == 3:
                
                    number_pos_moves_copy[max_indexes[2]] = "N/A"
                    
                elif len(max_indexes) == 4:
                
                    number_pos_moves_copy[max_indexes[3]] = "N/A"
                    
            
            # Retrieve the multiple max directions from their indexes
            max_directions = []
            
            for i in range(len(max_indexes)):
                
                max_directions.append(pos_moves[max_indexes[i]])
    
                
            cpu_move = random.choice(max_directions)
            
            # Check to see that there will be a possible legal move
            # on next turn after chosen move is processed
            pos_moves_next_turn = self._check_next_move(cpu_move)
            
            #print("Pos moves next turn are: " + str(pos_moves_next_turn))
            
            if len(pos_moves_next_turn) == 0:
            
                # Remove suicidal move from choices
                max_directions.remove(cpu_move)
                
                # Choose move from remaining max directions
                cpu_move = random.choice(max_directions)
                
        return cpu_move
    
    
    def _choose_between_hex_moves(self):
        """
        Assesses which move the computer should make in a hexagon game 
        and returns it.
        
        Returns:
            cpu_move - the selected 'best' move for the computer
        """
        
        print(self.board)
        
        # Retrieve current position of player 2
        for i in range(len(self.board)):
            if "2" in self.board[i]:
                 current_index = [i, self.board[i].index("2")]
         
        current_row = int(current_index[0])
        current_column = int(current_index[1])
         
         # Check for number of possible moves directly left and right
        number_pos_moves_right = 0
        number_pos_moves_left = 0
        
        for i in range(len(self.board)):
            
            if i < current_column:
                if self.board[current_row][i] == " ":
                    number_pos_moves_left += 1
                else:
                    number_pos_moves_left = 0
                    
            elif i > current_column:
                if self.board[current_row][i] == " ":
                    number_pos_moves_right += 1
                else:
                    break
        
        # Check for number of legal moves up left and down right
        number_pos_moves_up_left = 0
        number_pos_moves_down_right = 0
        
        for i in range(len(self.board)):
            
            if i < current_row:
                if self.board[i][current_column] == " ":
                    number_pos_moves_up_left += 1
                else:
                    number_pos_moves_up_left = 0
                    
            elif i > current_row:
                if self.board[i][current_column] == " ":
                    number_pos_moves_down_right += 1
                else:
                    break
                
                
        copy_index = current_index[:]
                
        # Check for number of legal moves up right and down left
        number_pos_moves_up_right = 0
        
        copy_index[0] -= 1 
        copy_index[1] += 1 
   
        while(copy_index[0] >= 0
            and copy_index[1] < self.m
            and self.board[copy_index[0]][copy_index[1]] != "X"
            and self.board[copy_index[0]][copy_index[1]] != "N"
            and self.board[copy_index[0]][copy_index[1]] != "1"):                   
            
                number_pos_moves_up_right += 1
                
                copy_index[0] -= 1 
                copy_index[1] += 1 
                
                
        copy_index = current_index[:]

        number_pos_moves_down_left = 0
        
        copy_index[0] += 1 
        copy_index[1] -= 1 
        
        while(copy_index[0] < self.m
            and copy_index[1] >= 0
            and self.board[copy_index[0]][copy_index[1]] != "X"
            and self.board[copy_index[0]][copy_index[1]] != "N"
            and self.board[copy_index[0]][copy_index[1]] != "1"):     
            
                number_pos_moves_down_left += 1
                
                copy_index[0] += 1 
                copy_index[1] -= 1 
    

        pos_moves = ['left',
                    'right',
                    'up left',
                    'up right',
                    'down left',
                    'down right']
        
        # Purposely same order as pos_moves so can retrieve later
        number_pos_moves = [number_pos_moves_left,
                            number_pos_moves_right,
                            number_pos_moves_up_left,
                            number_pos_moves_up_right,
                            number_pos_moves_down_left,
                            number_pos_moves_down_right]
               
        max_pos_moves = max(number_pos_moves)


        # If there is only one max direction
        if number_pos_moves.count(max_pos_moves) == 1:
            
            # Retrieve 'LRUD'
            max_index = number_pos_moves.index(max_pos_moves)
        
            cpu_move = pos_moves[max_index]
        
        
        # If there is more than one max direction
        elif number_pos_moves.count(max_pos_moves) > 1:
            
            # Make a copy so original list unaffected
            number_pos_moves_copy = number_pos_moves.copy()
            
            max_indexes = []
            
            # Retrieve indexes within pos_moves of maximum directions
            while max_pos_moves in number_pos_moves_copy:
                
                max_indexes.append(
                number_pos_moves_copy.index(max_pos_moves)
                )
                
                # Mark position of max move already appended with N/A
                number_pos_moves_copy[max_indexes[0]] = "N/A"
                
                if len(max_indexes) == 2:
                
                    number_pos_moves_copy[max_indexes[1]] = "N/A"
                    
                elif len(max_indexes) == 3:
                
                    number_pos_moves_copy[max_indexes[2]] = "N/A"
                    
                elif len(max_indexes) == 4:
                
                    number_pos_moves_copy[max_indexes[3]] = "N/A"
                    
                elif len(max_indexes) == 5:
                
                    number_pos_moves_copy[max_indexes[4]] = "N/A"
                    
                elif len(max_indexes) == 6:
                
                    number_pos_moves_copy[max_indexes[5]] = "N/A"
                    
            
            # Retrieve the multiple max directions from their indexes
            max_directions = []
            
            for i in range(len(max_indexes)):
                
                max_directions.append(pos_moves[max_indexes[i]])
                
                
            cpu_move = random.choice(max_directions)
            
            # Check to see that there will be a possible legal move
            # on next turn after chosen move is processed
            pos_moves_next_turn = self._check_next_hex_move(cpu_move)
        
            
            if len(pos_moves_next_turn) == 0:
            
                # Remove suicidal move from choices
                max_directions.remove(cpu_move)
                
                # Choose move from remaining max directions
                cpu_move = random.choice(max_directions)
                
        return cpu_move
    
        
     
        
    def _check_next_move(self,
                         cpu_move): 
       """
       Checks how many legal moves can be made on the next turn given
       the selected computer move, returns which moves these are.
       
       Parameters: 
           cpu_move - The selected computer move
           
       Returns:
           pos_moves_next_turn - What legal moves are available on the next turn
       """
       
       # Create a copy of the board to not affect the actual board
       # Needs to be a deep copy for a list of lists
       board_copy = copy.deepcopy(self.board)
       
       
       for i in range(len(board_copy)):
           if "2" in board_copy[i]:
               current_index = [i, board_copy[i].index("2")]
               
       new_index = current_index[:]
               
       if cpu_move == "left":
           
           new_index[1] -= 1
           
           # Make array position before moving = "X"
           board_copy[current_index[0]][current_index[1]] = "X"
           # Update board copy with player 2's position if they move left
           board_copy[new_index[0]][new_index[1]] = "2" 
           
       elif cpu_move == "right":
           
           new_index[1] += 1
           
           board_copy[current_index[0]][current_index[1]] = "X"
           board_copy[new_index[0]][new_index[1]] = "2"
           
       elif cpu_move == "up":
           
           new_index[0] -= 1
           
           board_copy[current_index[0]][current_index[1]] = "X"
           board_copy[new_index[0]][new_index[1]] = "2" 
                      
       elif cpu_move == "down":
           
           new_index[0] += 1
           
           board_copy[current_index[0]][current_index[1]] = "X"
           board_copy[new_index[0]][new_index[1]] = "2"
           
       
       # Check what moves will be available on the next turn given
       # the chosen direction
       pos_moves_next_turn = self._legal_moves(board_copy)  
           
       return pos_moves_next_turn
   
    
   
    def _check_next_hex_move(self,
                             cpu_move):
       """
       Checks how many legal moves can be made on the next turn given
       the selected computer move in a hexagon gae, returns which moves 
       these are.
       
       Parameters: 
           cpu_move - The selected computer move
           
       Returns:
           pos_moves_next_turn - What legal moves are available on the next turn
       """
       
       # Create a copy of the board to not affect the actual board
       # Needs to be a deep copy for a list of lists
       board_copy = copy.deepcopy(self.board)
       
       
       for i in range(len(board_copy)):
           if "2" in board_copy[i]:
               current_index = [i, board_copy[i].index("2")]
               
       new_index = current_index[:]
               
       if cpu_move == "left":
           
           new_index[1] -= 1
           
           # Make array position before moving = "X"
           board_copy[current_index[0]][current_index[1]] = "X"
           # Update board copy with player 2's position if they move left
           board_copy[new_index[0]][new_index[1]] = "2" 
           
       elif cpu_move == "right":
           
           new_index[1] += 1
           
           board_copy[current_index[0]][current_index[1]] = "X"
           board_copy[new_index[0]][new_index[1]] = "2"
           
       elif cpu_move == "up left":
           
           new_index[0] -= 1
           
           board_copy[current_index[0]][current_index[1]] = "X"
           board_copy[new_index[0]][new_index[1]] = "2" 
           
                      
       elif cpu_move == "up right":
           
            
           new_index[0] -= 1
           new_index[1] += 1
           
           board_copy[current_index[0]][current_index[1]] = "X"
           board_copy[new_index[0]][new_index[1]] = "2" 
           
           
       elif cpu_move == "down left":  
            
           new_index[0] += 1
           new_index[1] -= 1
           
           board_copy[current_index[0]][current_index[1]] = "X"
           board_copy[new_index[0]][new_index[1]] = "2" 
                      
       elif cpu_move == "down right":
           
           new_index[0] += 1
           
           board_copy[current_index[0]][current_index[1]] = "X"
           board_copy[new_index[0]][new_index[1]] = "2"
           
       
       # Check what moves will be available on the next turn given
       # the chosen direction
       pos_moves_next_turn = self._legal_moves(board_copy)  
           
       return pos_moves_next_turn
   
   
   

                        

class Error(Exception):
    """Base class for other exceptions"""
    
    
class InvalidDirectionError(Error):
    """Raise when input direction is invalid"""

    

        
