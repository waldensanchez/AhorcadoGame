import requests
import re
import random

class AhorcadoGame:
    def __init__(self, word, lives):
        self.word = word.upper()
        self.lives = lives
        self.guesses = []
        self.current_word = ['_'] * len(word)
        self.hangman_stage = 6

    def display_state(self):
        hangman_images = [
            "  ____\n |    |\n |\n |\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |    |\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |   /|\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |   /|\\\n |\n |\n=========",
            "  ____\n |    |\n |    O\n |   /|\\\n |   / \n |\n=========",
            "  ____\n |    |\n |    O\n |   /|\\\n |   / \\ \n |\n========="
        ]
        print("\nAHORCADO:")
        print(f"WORD: {' '.join(self.current_word)}")
        print(f"LIVES: {'X ' * self.lives}")
        print(f"LETTERS USED: {' '.join(self.guesses)}")
        print(hangman_images[self.hangman_stage])

    def check_win(self):
        return ''.join(self.current_word) == self.word

    def get_guess(self):
        while True:
            guess = input("NEXT GUESS? ").strip().upper()
            if len(guess) != 1 or not guess.isalpha() or guess == 'Ñ':
                print("INVALID GUESS")
            elif guess in self.guesses:
                print("YOU DUMB!")
                self.lives -= 1
                self.hangman_stage -= 1 
                self.display_state()
                if self.lives == 0:
                    return None
            else:
                return guess

    def update_guesses_and_lives(self, guess):
        if guess is None:
            return
        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.current_word[i] = guess
        else:
            self.lives -= 1
            print("NOT IN WORD!")
            self.hangman_stage -= 1
        self.guesses.append(guess)

    def game_over_message(self):
        if self.check_win():
            print("YOU WIN!")
            freed_hangman = (
                "  ____\n |    |\n |   \\O/\n |    |\n |   / \\\n |\n========="
            )
            print(freed_hangman)
        else:
            print(f"YOU LOST! The word was: {self.word}")
            lost_hangman = (
                "  ____\n |    |\n |    O\n |   /|\\\n |   / \\ \n |\n========="
            )
            print(lost_hangman)

    def play(self):
        while self.lives > 0 and not self.check_win():
            self.display_state()
            guess = self.get_guess()
            if guess is None:
                break
            self.update_guesses_and_lives(guess)
        self.display_state()
        self.game_over_message()

def fetch_wikipedia_article(topic):
    topic = topic.replace(' ', '_')
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={topic}&prop=extracts&format=json&explaintext"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        page_id = next(iter(data['query']['pages']))
        extract = data['query']['pages'][page_id].get('extract', '')
        return extract
    else:
        print("Failed to retrieve Wikipedia content")
        return None

def extract_words_from_text(text):
    words = re.findall(r'\b[A-Za-z]{5,}\b', text)
    return words

def get_random_word(words):
    long_words = [word for word in words if len(word) >= 5]
    return random.choice(long_words).upper() if long_words else None

def assign_word_from_wikipedia():
    topic = input("Enter a topic for the hangman game: ")
    article_content = fetch_wikipedia_article(topic)
    if article_content:
        words = extract_words_from_text(article_content)
        word = get_random_word(words)
        if word:
            return word
        else:
            print("No suitable words were found in the article.")
            return None
    else:
        print(f"Could not fetch a Wikipedia article on {topic}.")
        return None

def assign_lives():
    lives = input("Enter the number of lives: ").strip()
    if lives.isdigit():
        return int(lives)
    else:
        print("Invalid input for lives. Using default of 5.")
        return 5

def main():
    WORD = assign_word_from_wikipedia()
    if WORD:
        LIVES = assign_lives()
        game = AhorcadoGame(WORD, LIVES)
        game.play()
    else:
        print("Game could not start without a word.")

if __name__ == "__main__":
    main()
