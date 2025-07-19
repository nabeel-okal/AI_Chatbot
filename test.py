import random
from string import ascii_lowercase

fruits = [
    "apple",
    "banana",
    "cherry",
    "grape",
    "mango",
    "peach",
    "orange",
    "kiwi",
    "pineapple",
    "strawberry"
]

animals = [
    "elephant",
    "tiger",
    "giraffe",
    "dolphin",
    "kangaroo",
    "zebra",
    "lion",
    "panda",
    "rabbit",
    "penguin"
]

countries = [
    "jordan",
    "canada",
    "brazil",
    "egypt",
    "france",
    "germany",
    "japan",
    "india",
    "mexico",
    "australia"
]

def hangman_game():
    GAME_ON = True

    # Make the user choose between these 3 categories (initially)
    categories = {'fruits': fruits, 'animals': animals, 'countries': countries}

    while GAME_ON:
        lives = 5
        
        choice = input('Choose which category (Animals | Fruits | Countries): ').lower()

        # Get category and choosing random word from this category
        if choice not in categories:
            print('Invalid input. Please try again.\n')
            continue
        else:
            word = list(random.choice(categories[choice]))
        
        # Create blank spaces for the word        
        blanks = list('_' for blank in range(len(word)))
        # print(f'the word is {word} and its category is {choice}')

        print(f"\t{' '.join(blanks)}")

        while lives != 0:
            guess = input('\nGuess the letter: ')
            print(f'Lives: {lives}\n')

            if guess not in ascii_lowercase or len(guess) != 1:
                print('Invalid input. Please enter a single lowercase letter.')
                continue
            else:
                if guess in word:
                    print('Correct! . Keep going!')
                    
                    for i in range(len(blanks)):
                        if word[i] == guess:
                            blanks[i] = guess
                    print(f"\t{' '.join(blanks)}")

                else:
                    print('Incorrect, try again.')
                    lives -= 1
                    print(f"\t{' '.join(blanks)}")
                if '_' not in blanks:
                    print("🎉 Congratulations! You guessed the word correctly.")
                    break


        play_again = input('Would you like to play again? ').lower()

        if play_again in ['no', 'n']:
            print('Ok, bye!')
            GAME_ON = False

hangman_game()