"""
Barbara Marban
Class: CS 521 - Spring 1
13/02/2021
Final Project - Hangman Game

Description of Project: Player Class
"""


# Class with player information
class PlayersGame:
    def __init__(self, name, wins, losses):
        # Includes 1 private and 2 public self attributes
        self.__name = name
        self.wins = wins
        self.loss = losses

    def __repr__(self):
        return "The current user playing Hangman is " + str(self.__name)

    def score(self):
        return "Welcome {}, your score is {} wins and {} " \
               "losses.".format(self.__name, self.wins, self.loss)

    def total(self):
        # Public method
        return self.__totalscore()

    def __totalscore(self):
        # private method
        score = (int(self.wins) - int(self.loss))
        if score <= 0:
            return "Your overall score is {}. Lets play a game to " \
                   "try to improve it!".format(score)
        else:
            return "Your overall score is {}. Lets play a " \
                   "game and try to beat it!".format(score)

    def user_stats(self):
        return "{}, {}, {}".format(self.__name, self.wins, self.loss)

if __name__ == "__main__":

 # Unit tests for class
 player_1 = PlayersGame("Alex783", 2, 1)

 assert player_1.score() == "Welcome Alex783, your score is 2 wins and 1 " \
               "losses.", "Player scoring method not working correctly."

 assert player_1.total() == "Your overall score is 1. Lets play a game and " \
                        "try to beat it!", "Total score method not working."

 assert player_1.user_stats() =="Alex783, 2, 1", \
                        "User stats method not working."
