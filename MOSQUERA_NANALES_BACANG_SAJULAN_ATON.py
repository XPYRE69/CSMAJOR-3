import os
import random
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \/|\
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \/|\
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     \/|\
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |     \/|
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def hangman():
    words = [
        ("python", "A popular programming language"),
        ("elephant", "A large mammal with a trunk"),
        ("guitar", "A musical instrument with strings"),
        ("ocean", "A vast body of saltwater"),
        ("mountain", "A tall landform that rises above its surroundings")
    ]
    
    score = 0
    start_time = time.time()
    time_limit = 60
    
    for word, hint in random.sample(words, len(words)):
        guessed_letters = set()
        tries = 6
        correct_guesses = set(word)
        
        clear_screen()
        print("Welcome to Hangman!")
        print("The game begins! Here's your hint:")
        print(f"Hint: {hint}")
        
        while tries > 0 and correct_guesses:
            elapsed_time = time.time() - start_time
            if elapsed_time >= time_limit:
                print("Time's up! Game over!")
                print(f"Your final score: {score}")
                return
            
            display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
            print(display_hangman(tries))
            print(f"Word: {display_word}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
            print(f"Time left: {int(time_limit - elapsed_time)} seconds")
            print(f"Score: {score}")
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            
            guessed_letters.add(guess)
            
            if guess in word:
                correct_guesses.discard(guess)
                print("Correct guess!")
            else:
                tries -= 1
                print("Incorrect guess!")
            
            if not correct_guesses:
                score += 1
                print(f"Congratulations! You guessed the word: {word}")
                break
            
        if tries == 0:
            print(display_hangman(tries))
            print(f"Game over! The word was: {word}")
            print(f"Your final score: {score}")
            return
    
    print(f"Time's up! Your final score: {score}")

if __name__ == "__main__":
    hangman()
