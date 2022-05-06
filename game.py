from phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("Have a great day"),
            Phrase("May the fourth be with you"),
            Phrase("I am iron man"),
            Phrase("I can do this all day"),
            Phrase("Live and let live")
        ]
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            self.active_phrase.display(self.guesses)
            print("\n")
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.check_letter(user_guess)
            if not self.active_phrase.check_letter(user_guess):
                print(f"Incorrect guesses: {self.missed}\n")
        self.game_over()
        print("The phrase was:", self.active_phrase.phrase.upper())
        self.continue_playing()

    def welcome(self):
        return "-" * 30 + "\n" + "WELCOME TO PHRASE-HUNTING GAME" + "\n" + "-" * 30 + "\n"

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        user_guess = input("Guess a letter: ").lower()
        while True:
            if user_guess.isalpha():
                if len(user_guess) == 1:
                    break
                else:
                    print("Game only accepts one letter per chance. Please try again.")
                    user_guess = input("Guess a letter: ").lower()
                    continue
            else:
                print("Game only accepts alphabets. Please try again.")
                user_guess = input("Guess a letter: ").lower()
                continue

        if user_guess in self.guesses:
            print(f"You've already guessed {user_guess} once. Try another one. ")
        else:
            self.guesses.append(user_guess)
            if self.active_phrase.check_letter(user_guess):
                print("")
            else:
                print("You've guessed an incorrect letter. Please try again. ")
                self.missed += 1
                print(f"You're left with {5-self.missed} out of 5 chances to win.")
        return user_guess

    def game_over(self):
        self.active_phrase.display(self.guesses)
        if self.missed == 5:
            print("\nAll the chances are over. Game over, Sorry.")
        else:
            print("\nCongrats, you guessed it right. ")

    def continue_playing(self):
        user_playing = input("\nWould you like to play again? Y/N ")
        if user_playing.upper() == "Y":
            print("")
            self.active_phrase = None
            new_game = Game()
            new_game.start()
        else:
            print("\nOkay! Thanks for playing. ")
