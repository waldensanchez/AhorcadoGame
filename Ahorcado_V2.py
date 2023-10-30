import random

class AhorcadoGame:
    def __init__(self, word, lives=5):
        self.word = word.upper()
        self.lives = lives
        self.guesses = []
        self.current_word = ['_'] * len(word)
        self.hangman_stage = 6  # Initialize to the full hangman

    def display_state(self):
        hangman_images = [
            "  ____\n |    |\n |\n |\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |    |\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |   /|\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |   /|\\\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |   /|\\\n |   / \n |\n=========",
            "  ____\n |    |\n |    O\n |   /|\\\n |   / \\ \n |\n========="  # Extended for longer words
        ]

        print("AHORCADO:")
        print(f"WORD: {' '.join(self.current_word)}")
        print(f"LIVES: {'X ' * self.lives}")
        print(f"LETTERS USED: {' '.join(self.guesses)}")

        if self.hangman_stage >= 0 and self.hangman_stage < len(hangman_images):
            print(hangman_images[self.hangman_stage])
        else:
            print("Hangman stage not available")

    def check_win(self):
        return ''.join(self.current_word) == self.word

    def make_guess(self, guess):
        guess = guess.strip().upper()

        if len(guess) != 1 or not 'A' <= guess <= 'Z' or guess == 'Ñ':
            return "INVALID GUESS"

        if guess in self.guesses:
            return "YOU DUMB! You already guessed this letter."

        if guess in self.word:
            self.add_to_word(guess)
            self.guesses.append(guess)
        else:
            self.remove_life()
            self.guesses.append(guess)
            return "NOT IN WORD"

    def add_to_word(self, guess):
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.current_word[i] = guess

    def remove_life(self):
        self.lives -= 1
        self.hangman_stage -= 1  # Remove a limb

    def play(self):
        while self.lives > 0 and not self.check_win():
            self.display_state()
            guess = input("NEXT GUESS? ")
            result = self.make_guess(guess)
            if result:
                print(result)

        self.display_state()
        if self.check_win():
            self.display_win()
        else:
            print("YOU LOST! The word was:", self.word)

    def display_win(self):
        print("YOU WIN!")
        freed_hangman = (
            "  ____\n |    |\n |   \\O/\n |    |\n |   / \\\n |\n========="
        )
        print(freed_hangman)

def assign_word():
    word = input("Enter a word to guess: ").strip().upper()
    return word

def main():
    # Configuration part
    WORD = assign_word()  # Assign a word at the beginning
    LIVES = 6  # Change the number of lives if needed

    game = AhorcadoGame(WORD, LIVES)
    game.play()

if __name__ == "__main__":
    main()
