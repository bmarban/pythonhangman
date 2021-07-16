# Hangman Game

# Why Was This Program Created?

This program was created as a final project for CS521 class. The main requirements were to show a good use of python and that it contained the following elements: 

* container type (list, tuple, set, or dictionary)
* iteration type (for, while)
* conditional (if)
* try blocks
* user-defined functions
* input and/or output file (submit input data)
* user-defined class. The class must be imported by your main program and have
the following required structures.
    *  at least 1 private and 2 public self attributes
    *  at least 1 private and 1 public method that take arguments, return values and
    are used by your program
    *  an init() method that takes at least 1 argument
    *  a repr() method


# How To Play

Welcome to my Hangman game. This game was done completely in python without the need to install any third-party modules to play. It meets all the criteria required for the Boston University class CS 521, Information Structures with Python. This game was completed on February 27, 2021 by Barbara Marban. 

First, if it is the first time a player is playing the game they will have to enter a username of their choice. This username will be entered into a file called “players_game” that has the summary of all players and their scores with a score of 0. If the player has played before and they remember their username, then he can use that as the username input and retrieve his previous score to continue working on it. Once the score is retrieved the game begins. 

The program works exactly like a classical Hangman game. A difficulty level is chosen by the player between easy, medium and hard. There is a preset list of words for each level saved in the same folder as the game. The program will randomly choose a word from the selected level file and the player will have 10 more tries than the length of the word to guess the word. The guessing now begins. 

As the player guesses letters the program will make sure that the letter has not been guessed before and that the player input is a valid letter. The program will display the amount of guesses left for the player and the letters guessed by the player. Additionally, the player will visually be able to see the length of the word they are guessing as well as what letters they have guessed correctly and in what position they are. The game ends either with the total amount of allowed guesses ending or the word being guessed. 

Once the game ends the player’s score is updated and they will receive a summary file with what word they had to guess, how many guesses they had left, if they won or lost, their previous score, and their current score. This file is saved as “summary_game”.

This program is useful to entertain anyone as it has different difficulty levels. The game can also be expanded by adding more words into the easy, medium and hard files so that if a player plays many times there is a smaller likelihood of the same word being chosen once. 

Hope you enjoy the game!
