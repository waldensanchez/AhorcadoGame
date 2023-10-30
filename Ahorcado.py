WORD = 'WORDS'
LIVES = 5

class AhorcadoGame:
    def __init__(self, word, lives):
        self.word = word.upper()
        self.lives = lives
        self.guesses = []
        self.current_word = ['_'] * len(word)

    def display_state(self):
        print("\nAHORCADO:")
        print(f"WORD: {' '.join(self.current_word)}")
        print(f"LIVES: {'X ' * self.lives}")
        print(f"LETTERS USED: {' '.join(self.guesses)}")

    def is_in_word(self, guess):
        return guess in self.word

    def remove_lives(self):
        self.lives -= 1

    def did_i_win(self):
        return ''.join(self.current_word) == self.word

    def already_used(self, guess):
        return guess in self.guesses

    def valid_guess(self, guess):
        if len(guess) != 1 or not guess.isalpha() or guess == 'Ñ':
            print("INVALID GUESS")
            return False
        return True

    def get_guess(self):
        while True:
            guess = input("NEXT GUESS?").strip().upper()
            if not self.valid_guess(guess):
                continue
            if self.already_used(guess):
                print("YOU DUMB!")
                self.remove_lives()
                self.display_state()
                if self.lives == 0:
                    return None
            else:
                return guess

    def update_current_word(self, guess):
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.current_word[i] = guess

    def game_over_message(self):
        if self.did_i_win():
            print("YOU WIN!")
        else:
            print("YOU LOST!")

    def play(self):
        while self.lives > 0 and not self.did_i_win():
            self.display_state()
            guess = self.get_guess()
            if guess is None: 
                break
            self.guesses.append(guess)

            if self.is_in_word(guess):
                self.update_current_word(guess)
            else:
                self.remove_lives()
                print("NOT IN WORD!")

        self.game_over_message()

def main():
    global WORD, LIVES
    game = AhorcadoGame(WORD, LIVES)
    game.play()

if __name__ == "__main__":
    main()
