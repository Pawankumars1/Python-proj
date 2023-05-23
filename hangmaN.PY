import random

def hangman():
    words = ["apple", "banana", "cherry", "durian", "elderberry"]  # List of words to choose from
    word = random.choice(words)  # Select a random word from the list
    guessed_letters = []
    tries = 6  # Number of tries or guesses allowed

    print("Welcome to Hangman!")
    print("_ " * len(word))  # Display the word as underscores

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            print_word(word, guessed_letters)
            
            if "_" not in print_word(word, guessed_letters):
                print("Congratulations! You guessed the word correctly!")
                break
        else:
            tries -= 1
            print("Wrong guess!")
            print_hangman(tries)

            if tries == 0:
                print("Game over! You ran out of tries.")
                print(f"The word was '{word}'.")
                break

def print_word(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)
    return display_word

def print_hangman(tries):
    stages = [  
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
        '''
    ]
    print(stages[tries])

hangman()
