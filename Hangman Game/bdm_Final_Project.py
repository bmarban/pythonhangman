"""
Barbara Marban
Class: CS 521 - Spring 1
13/02/2021
Final Project - Hangman Game

Description of Project: This is a Hangman Game.
The game has three levels to chose from and
will output a file with the summary of the game.
"""

# import class
from player_class import PlayersGame

# Start of game
def start_game():
    start_bool = False
    while not start_bool:
        user_start = input("\nWould you like to play Hangman (Y or N): ")
        if user_start.upper() == "Y" or user_start.upper() == "YES":
            start_bool = True
        elif user_start.upper() == "N" or user_start.upper() == "NO":
            print("Ok, goodbye. Hope to see you again soon!")
            exit()
        else:
            print("Sorry, invalid input! Please try again.")
            continue


# Chose difficulty level
def diff_game():

    # based on input from user pass into word list function the difficulty
    loop_bool = False
    while not loop_bool:
        diff_str = input("Great! What difficulty do you "
                         "chose (Easy, Medium, Hard)? ")
        if diff_str.upper() == "E" or diff_str.upper() == "EASY":
            loop_bool = True
            return "easy"
        elif diff_str.upper() == "M" or diff_str.upper() == "MEDIUM":
            loop_bool = True
            return "medium"
        elif diff_str.upper() == "H" or diff_str.upper() == "HARD":
            loop_bool = True
            return "hard"
        else:
            print("Sorry, invalid input! Please try again.")
            continue


# Get list of words from external files
def word_list_choice(difficulty_str):

    file_name = difficulty_str + ".txt"

    # try to open file with a given name,
    # if file doesnt exist create error and exit
    try:
        # Open file and read words
        file_open = open(file_name, "r")

        # Create three lists of words
        word_lists = file_open.read().split()

        # Close Files
        file_open.close()

        # Return lists
        return word_lists

    except FileNotFoundError:
        print("\nSorry, the file with the required words does not exist."
              "\nPlease create word file with correct name "
              "(easy, medium or hard) and try again.")
        exit()


# Pick random word and return word and list of letters
def letter_choice(word_list):
    import random
    word = random.choice(word_list)

    # list of letters
    letter_list = []
    for letter in word:
        letter_list.append(letter)

    return word, letter_list


# get number of guesses available
def guess_amt(letters):
    return len(letters) + 10


# check guessed letter
def guess_check(guess_list):

    # make sure letter is in the alphabet
    import string
    alphabet_list = list(string.ascii_lowercase)

    guess_bool = False
    while not guess_bool:
        guess = input("What is your letter? ").lower()
        if guess in alphabet_list:
            if guess in guess_list:
                print("You already tried that letter. Please try again!")
                continue
            guess_bool = True
            return guess
        else:
            print("That is not a valid letter. Please try again.")
            continue


# Guess loop until complete
def guess_loop(letter_list, guess_int, guess_space_list):

    guess_list = []
    import copy
    del_letter_list = copy.deepcopy(letter_list)
    while guess_int >= 1 and "_" in guess_space_list:
        guess = guess_check(guess_list)  # get a valid guess
        guess_int -= 1  # deduct one guess for the person
        del_ind = []  # index to delete
        change_ind = []  # index to change line to letter
        if guess in letter_list:  # correct guess
            # checking if letter is in word more times
            for i, e in enumerate(del_letter_list):
                if e == guess:
                    del_ind.append(i)
            # remove the letter as many times as it appears
            for _ in del_ind:
                del_letter_list.remove(guess)
            for i, e in enumerate(letter_list):
                if e == guess:
                    change_ind.append(i)
            # change line to the letter as many times as it appears
            for i in change_ind:
                guess_space_list[i] = guess
            print("\nWow! You guessed {} correctly!".format(guess))
            print("You have {} more tries.".format(guess_int))
            print(guess_space_list)
            guess_list.append(guess)
            print("You have tried the following letters:"
                  " \n{}\n".format(guess_list))

        else:
            print("\nSorry {} is not in the word. "
                  "\nYou have {} more tries.".format(guess, guess_int))
            print(guess_space_list)
            guess_list.append(guess)
            print("You have tried the following letters:"
                  "\n{}".format(guess_list))

    return guess_space_list, guess_int


# main game
def main_game(word, letter_list, guess_int):
    # create guess visual
    guess_space_list = []
    for s in range(len(word)):
        guess_space_list.append("_")

    # Intro to game with word length and guesses
    print("\nThe word has {} letters. You have "
          "{} tries.".format(len(word), guess_int))
    print(guess_space_list)

    # play game
    guess_space_list, guess_int = guess_loop(letter_list,\
                                             guess_int, guess_space_list)

    # End game
    if "_" in guess_space_list:
        print("Sorry, you lost. The word was '{}'.".format(word))
        result = "lost"
    else:
        print("Congratulations! You guessed the word '{}' "
              "correctly!".format(word))
        result = "won"

    return guess_int, result


if __name__ == "__main__":
    # Find Username or create a new one
    check = False
    while not check:
        new_user = input("Have you played before and "
                         "do you have a username (Y or N): ").upper()
        if new_user == "Y":
            user_name = input("What is your username? ").lower()
            try:
                user_file = open("players_game.txt", "r")
                user_stats = [line for line in user_file.readlines()\
                              if user_name == (line.split(","))[0]]
            except FileNotFoundError:  # if file does not exist
                print("Sorry it looks like we don't have any history of "
                      "users. Lets start again and create a new username.")
                continue
            user_file.close()

            if not user_stats:  # if user not found
                print("Sorry could not find username. Lets try again:")
                continue
            else:
                check = True
        elif new_user == "N":  # create new user
            dupl_check = False
            while not dupl_check:
                try:
                    user_name = input("Chose a username (please only letters and numbers): ").lower()
                    user_file = open("players_game.txt", "r")
                    user_found = [line for line in user_file.readlines() \
                                  if user_name in line]
                    user_file.close()
                except FileNotFoundError:
                    user_found = []
                if not user_found:
                    user_file = open("players_game.txt", "a")
                    user_file.write(user_name + ", 0, 0")
                    user_file.close()
                    user_stats = ["{}, 0, 0".format(user_name)]
                    dupl_check = True
                    check = True
                else:
                    print("That user already exists "
                          "chose a different username. ")
                    continue
        else:
            print("Sorry invalid input please try again: ")
            continue

    # User stats
    name, wins, losses = user_stats[0].strip().split(", ")

    # Create player instance and welcome
    current_player = PlayersGame(name, wins, losses)
    print(current_player.score())
    print(current_player.total())

    # Begin game
    start_game()

    # Main data for game and output
    difficulty = diff_game()
    word_list = word_list_choice(difficulty)
    word, letter_list = letter_choice(word_list)
    guess_int = guess_amt(letter_list)

    # start guessing
    guess_int, result = main_game(word, letter_list, guess_int)

    # Create new player instance with updated stats
    if result == "won":
        updated_player = PlayersGame(name, int(wins)+1, losses)
    else:
        updated_player = PlayersGame(name, wins, int(losses)+1)

    new_user_stats = updated_player.user_stats()

    # Update score in file
    user_file = open("players_game.txt", "r")
    updated_file = ""
    for line in user_file.readlines():
        if line == user_stats[0]:
            updated_file += new_user_stats + "\n"
        else:
            updated_file += line
    user_file.close()

    write_user_file = open("players_game.txt", "w")
    write_user_file.write(updated_file)
    write_user_file.close()

    # output file
    text_output = """
    Thank you for playing Hangman {}!
    
    Your word was: {}
    You had {} tries left!
    You {} the game. 
    
    Your old stats were:
        Wins: {}
        Losses: {}
    
    Your new stats are: 
        Wins: {}
        Losses: {}
    
    Hope to see you next time!
    """.format(name, word, guess_int, result, \
               current_player.wins, current_player.loss, \
               updated_player.wins, updated_player.loss)

    output_file = open("summary_game.txt", "w")

    output_file.write(text_output)

    output_file.close()

    print("\nWe printed a summary file for your records. Hope you enjoyed."
          "\nCome again soon!")


