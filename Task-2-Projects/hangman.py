import random

# Predefined dictionary of words with corresponding hints
WORD_DICT = {
    "PYTHON": "A popular high-level programming language.",
    "VARIABLE": "A reserved memory location to store values.",
    "FUNCTIONS": "A block of code which only runs when it is called.",
    "DICTIONARY": "An unordered collection of key-value pairs in Python.",
    "ALGORITHM": "A step-by-step procedure or set of rules for solving a problem.",
    "DEVELOPER": "A person who creates computer software or applications."
}

# ASCII Visual Stages for Hangman progress
HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    ========="""
]


def play_hangman():
    # 1. Word Selection & Setup
    word, hint = random.choice(list(WORD_DICT.items()))
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("\n========================================")
    print("      WELCOME TO HANGMAN GAME!          ")
    print("========================================")
    print(f"HINT: {hint}")

    # 2. Main Game Loop
    while incorrect_guesses < max_attempts:
        # Display Visual Progress
        print(HANGMAN_PICS[incorrect_guesses])

        # Partially Revealed Word
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("\nWord: " + " ".join(display_word))
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining Attempts: {max_attempts - incorrect_guesses}")

        # Check Win Condition
        if set(word).issubset(guessed_letters):
            print("\n🎉 Congratulations! You guessed the hidden word:", word)
            break

        # 3. User Input & Validation
        guess = input("\nGuess a letter (or type 'hint' to view hint): ").strip().upper()

        if guess == "HINT":
            print(f"\nHINT: {hint}")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        # 4. Check Guess
        if guess in word:
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            print(f"❌ Incorrect! '{guess}' is not in the word.")
            incorrect_guesses += 1

    # 5. Loss Condition
    if incorrect_guesses == max_attempts:
        print(HANGMAN_PICS[incorrect_guesses])
        print("\n💀 Game Over! You ran out of attempts.")
        print(f"The correct word was: {word}")


def main():
    # 6. Play Again Loop
    while True:
        play_hangman()
        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("Thank you for playing Hangman! Goodbye.")
            break


if __name__ == "__main__":
    main()