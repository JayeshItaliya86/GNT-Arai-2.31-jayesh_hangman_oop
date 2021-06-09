from random import randint
import re
class Hangman:
    def __init__(self):
        self.user_input = " "
        self.lst = self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.lst = self.word_to_find = self.possible_words[randint(0, 3)]
        self.int = self.lives = len(self.word_to_find)
        self.lst = self.correctly_guessed_letter = ["_" for item in self.word_to_find]
        self.lst = self.wrongly_guessed_letters = []
        self.lst = self.well_guessed_letter = []
        self.int = self.turn_count = 0
        self.int = self.error_count = 0

    def play(self):
        print("start game")
        while self.lives > 0:
            self.user_input = input("Please enter only one letter at a time in lowercase : ")[0]
            pattern = '[a-z]'  # check for lower case alphabet character
            if re.findall(pattern, self.user_input):
                word_split = [element for element in self.word_to_find]
                if self.user_input in word_split:
                    for index, guessed_word in enumerate(word_split):
                        if guessed_word == self.user_input:
                            self.correctly_guessed_letter[index] = self.user_input
                        else:
                            continue
                    self.well_guessed_letter.append(self.user_input)
                    self.turn_count += 1
                    self.lives -= 1
                    if self.correctly_guessed_letter == self.word_to_find:
                        break
                    else:
                        continue
                else:
                    self.wrongly_guessed_letters.append(self.user_input)
                    self.error_count += 1
                    self.lives -= 1
    def start_game(self):
        self.play()
        if self.lives == 0:
            self.game_over()
        if self.well_played() == self.well_guessed_letter:
            self.well_played()
        print(f"Well guessed letter : {self.well_guessed_letter}, wrongly guessed letter : {self.wrongly_guessed_letters}, lives : {self.lives}, error count : {self.error_count} and turn count : {self.turn_count}")

    def well_played(self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")

    def game_over(self):
        print("game over...")