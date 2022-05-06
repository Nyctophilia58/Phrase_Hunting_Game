class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.unique_letters = set(self.phrase)
        self.unique_letters.discard(" ")

    def display(self, guesses):
        for letter in self.phrase:
            if letter == " ":
                print(" ", end="")
            elif letter in guesses:
                print(f"{letter}", end="")
            else:
                print("_", end="")

    def check_letter(self, guess):
        return guess in self.phrase

    def check_complete(self, guesses):
        if len(self.unique_letters - set(guesses)) == 0:
            return True
