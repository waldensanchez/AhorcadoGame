import random

class AhorcadoGame:
    def __init__(self, word, lives=5):
        self.word = word.upper()
        self.lives = lives
        self.guesses = []
        self.current_word = ['_'] * len(word)

    def display_state(self):
        print("AHORCADO:")
        print(f"WORD: {' '.join(self.current_word)}")
        print(f"LIVES: {'X ' * self.lives}")
        print(f"LETTERS USED: {' '.join(self.guesses)}")

    def check_win(self):
        return ''.join(self.current_word) == self.word

    def play(self):
        while self.lives > 0 and not self.check_win():
            self.display_state()
            guess = input("NEXT GUESS? ").strip().upper()

            if len(guess) != 1 or not 'A' <= guess <= 'Z' or guess == 'Ñ':
                print("INVALID GUESS")
                continue

            if guess in self.guesses:
                self.lives -= 1
                print("YOU DUMB!")
            elif guess in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.current_word[i] = guess
                self.guesses.append(guess)
            else:
                self.lives -= 1
                self.guesses.append(guess)
                print("NOT IN WORD!")

        self.display_state()
        if self.check_win():
            print("YOU WIN!")
        else:
            print("YOU LOST!")

def assign_word():
    word = input("Enter a word to guess: ").strip().upper()
    return word

def main():
    # Configuration part
    WORD = assign_word()  # Assign a word at the beginning
    LIVES = 5  # Change the number of lives if needed

    game = AhorcadoGame(WORD, LIVES)
    game.play()

if __name__ == "__main__":
    main()
