# Tron 2D

Should include your project title and a description of your project design, classes, methods and other important details.

Your Part1.md file should be at least several paragraphs in length and should explain what your project is, what each of the files you wrote for the porject contains and does, and if you debated certain design choices, explaining why you made them.

### Project Summary

This project aimed at creating a text-based version of the Tron board game using an object-oriented approach.


To do so, three Python files were created: 
- main.py: Main script to play the game in the console
- board.py: Board class to manage the gameplay and print the board
- player.py: Contains player classes to differentiate between human and computer players

The classes in the board and player files are imported into the main script to allow for use of their methods.



### Project Design

The most important feature of the project is the main script, which contains the Tron class that initialises the startup menu and allows for the player(s) to select what type of game they want to play. The options are a 2-player game or a game against a 'computer' player, or the player can exit the menu to quit the game.

Once a selection has been made, the Tron run_game method is called, which initiates the start of a game. At this point the user will be asked for what size of board they want to play on and whether they would like the game to be simultaneous, allowing for the possibility of a draw. If a computer game was chosen, the user will also be asked what difficulty they would like to play on, with three options of easy, medium, and hard.

Having chosen the desired configuration of settings, the initial board is displayed in the console. The players start in opposite corners of the board. Each player takes it in turn to move one square in any direction. If a player moves to a square that is out of bounds, or into a square already traversed by a player, they are considered to have crashed and the game will end, returning the player(s) to the menu. The aim of the game is to survive for longer than the other player.

### Files

##### main.py

The main.py script contains the Tron class, which represents the actual game. As mentioned, this contains the script that allows the player to interact with the game via the console, as well as the startup menu allowing for the desired choice of game.

Additionally, the file contains helper methods for the three questions that a player must answer to begin a game. Each method has exceptions so that the user must input a valid answer for the question being asked. The board size must be greater than 3x3, the difficulty must be easy, medium or hard, and the player must answer yes or no to a simultaneous game. Failure to provide these will not allow the game to continue.

A choice was made to also not allow the game board to be a size greater than 20, as beyond this it becomes difficult to fit in the console.

##### player.py

This file contains the parent player class, and the two 'children' classes which inherit from it: the human player class and computer player class.

The parent class contains a method to ask the player what move they would like to make out of the 4 possible directions. Players are able to input only the first letter of each direction to allow for quicker interaction with the game. Exceptions are again written so that the player must correctly choose one direction before the game can continue.

The computer player class represents a non-human player in the game, and contains methods to make its move depending on the difficulty level the player has chosen to play against. The differences in moves is as follows:

- Easy: A random move from the 4 directions
- Medium: A random move in any non-suicidal direction
- Hard: A smart move in the direction with the most available spaces, whilst avoiding moves that would result in definite suicide the turn after

To choose its move on medium or hard difficulty, a helper method returns the legal moves that are available for the computer to make.

On hard difficulty, if there are multiple moves available, a random choice is made between them.


##### board.py

The board file contains the class which manages the board. This is achieved by methods which create the board, process moves, output the board to the console, and display end of game messages.
