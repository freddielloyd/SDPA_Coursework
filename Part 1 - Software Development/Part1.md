# Tron 2D

This project aimed at creating a text-based version of the Tron board game using an object-oriented approach. The game works by players taking it in turns to choose a move whilst trying to avoid crashing. In a regular game, the player who survives for the longest wins.


To do so, three Python files were created: 
- main.py: Main script containing methods to interact with and play the game in the console
- board.py: Board class to manage the gameplay, process moves and print the board
- player.py: Contains human and computer player classes to differentiate between players and how they move

The classes in the board and player files are imported into the main script to allow for use of their methods. The main script imports the sys module from the Python standard library, the player file imports copy and random, and board imports copy.

### Project Design

On running the main script, the Tron class is called which initialises the game's startup menu and allows for the player to select what type of game they want to play. The options are a 2-player game or a game against a 'computer' player, or the player can exit the menu to quit the game.

Once a selection has been made, the Tron run_game method is called, which initiates the start of a game. At this point the user will be asked if they would like to play on a hexagon board, what size of board they want to play on and whether they would like the game to be simultaneous, allowing for the possibility of a draw. If a computer game was chosen, the user will also be asked what difficulty they would like to play on, with three options of easy, medium, and hard.

Having chosen the desired configuration of settings, the initial board is displayed in the console. The players start in opposite corners of the board. Each player takes it in turn to move one square in any direction. If a player moves to a square that is out of bounds, or into a square already traversed by a player, they are considered to have crashed and the game will end, returning the player(s) to the menu. The aim of the game is to survive for longer than the other player. In a simultaneous game, the game can end in a draw if the players collide or crash on the same turn.

### Files

##### main.py

The main.py script contains the Tron class, which represents the actual game. As mentioned, this contains the script that allows the player to interact with the game via the console, as well as the startup menu allowing for the desired choice of game.

Additionally, the file contains helper methods for the four questions that a player must answer to begin a game. Each method has exceptions so that the user must input a valid answer for the question being asked, failure to provide these will not allow the game to continue. They are as follows:
- The player must answer yes or no to a hexagon game
- The board size must be greater than 3x3 for a reasonable game experience, and less than 20x20 is this is difficult to fit in the console
- The difficulty must be easy, medium or hard
- The player must answer yes or no to a simultaneous game. Failure to provide these will not allow the game to continue.

##### player.py

This file contains the parent player class, and the two 'children' classes which inherit from it: the human player class and computer player class.

The parent class contains methods to ask the player what move they would like to make out of the 4 possible directions if playing on a square grid, or the 6 possible diretions on a hexagonal grid . Players are able to input only the first letter of each direction to allow for quicker interaction with the game. Exceptions are again written so that the player must correctly choose one direction before the game can continue.

The computer player class represents a non-human player in the game, and contains methods to make its move depending on the difficulty level the player has chosen to play against. The differences in moves is as follows:

- Easy: A random move from the 4 directions
- Medium: A random move in any non-suicidal direction
- Hard: A smart move in the direction with the most available spaces, whilst avoiding moves that would result in definite suicide the turn after

To choose its move on medium or hard difficulty, a helper method returns the legal moves that are available for the computer to make. 

On hard difficulty, if there are multiple maximum direction moves available, a random choice is made between them.


##### board.py

The board file contains the class which manages the board. This is achieved by methods which create the board, process moves, output the board to the console, and display end of game messages.
