import random
from string import ascii_lowercase

RPS_PROMPTS = [
    "I want to play rock paper scissors",
    "let's play rock paper scissors",    
    "can we play rock paper scissors?",
    "rock paper scissors",
    "play rps",
    "play a game",
    "wanna play rock paper scissors?",
    "start rock paper scissors"
]

HANGMAN_PROMPTS = [
    "play hangman",
    "i want to play hangman",
    "start hangman",
    "let's play hangman",
    "hangman please",
    "can i play hangman",
    "run hangman game",
    "launch hangman",
    "begin hangman",
    "initiate hangman",
    "hangman game",
    "play the hangman game",
    "start the hangman game",
    "play word guessing",
    "play word game"
]

def rock_paper_scissors():
    print("Let's go! . That sounds interesting!!")

    # Different chatbots = different responses

    choices = ['rock', 'paper', 'scissors']
    GAME_ON = True

    while(GAME_ON):

        try:
            PLAYER = input('Enter your choice (Rock | Paper | Scissors"): ').lower()
            if PLAYER not in choices:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print("{e}")
        
        COMPUTER = choices[random.randint(0, len(choices) - 1)]


        if PLAYER == 'rock':
            if COMPUTER == 'rock':
                print(f'I chose: {COMPUTER.upper()}')
                print("It's a draw!")
            elif COMPUTER == 'paper':
                print(f'I chose: {COMPUTER.upper()}')
                print('I won! . Better Luck next time.')
            else:
                print(f'I chose: {COMPUTER.upper()}')
                print('You won! . Congrats!')

        if PLAYER == 'paper':
            if COMPUTER == 'rock':
                print(f'I chose: {COMPUTER.upper()}')
                print('You won! . Congrats!')
            elif COMPUTER == 'paper':
                print(f'I chose: {COMPUTER.upper()}')
                print("It's a draw!")
            else:
                print(f'I chose: {COMPUTER.upper()}')
                print('I won! . Better Luck next time.')

        if PLAYER == 'scissors':
            if COMPUTER == 'rock':
                print(f'I chose: {COMPUTER.upper()}')
                print('I won! . Better luck next time.')
            elif COMPUTER == 'paper':
                print(f'I chose: {COMPUTER.upper()}')
                print('You won! . Congrats!')
            else:
                print(f'I chose: {COMPUTER.upper()}')
                print("It's a draw!")
        
        # Check if the user wants to play another game
        PLAY_AGAIN = input('Would you like to play another game? ').lower()

        if PLAY_AGAIN in ['no', 'n']:
            GAME_ON = False
    print('OK, bye.')

def hangman_game():

    # Word categories
    fruits = [
        "apple", "banana", "cherry", "grape", "mango",
        "peach", "orange", "kiwi", "pineapple", "strawberry"
    ]

    animals = [
        "elephant", "tiger", "giraffe", "dolphin", "kangaroo",
        "zebra", "lion", "panda", "rabbit", "penguin"
    ]

    countries = [
        "jordan", "canada", "brazil", "egypt", "france",
        "germany", "japan", "india", "mexico", "australia"
    ]

    GAME_ON = True

    categories = {
        'fruits': fruits,
        'animals': animals,
        'countries': countries
    }

    print("🎮 Welcome to Hangman Game!")

    while GAME_ON:
        lives = 5
        guessed_letters = set()

        # Ask the user to choose a category
        print("\nAvailable categories: Fruits | Animals | Countries")
        choice = input("Choose a category: ").strip().lower()

        if choice not in categories:
            print("❌ Invalid category. Please try again.")
            continue

        word = list(random.choice(categories[choice]))
        blanks = ['_' for _ in word]

        print(f"\nCategory: {choice.title()}")
        print(f"{' '.join(blanks)}")

        while lives > 0:
            guess = input("\nGuess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in ascii_lowercase:
                print("❌ Please enter a single lowercase letter (a-z).")
                continue

            if guess in guessed_letters:
                print("⚠️ You've already guessed that letter. Try another one.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print("✅ Correct guess!")

                for i in range(len(word)):
                    if word[i] == guess:
                        blanks[i] = guess
            else:
                print("❌ Incorrect guess.")
                lives -= 1

            print(f"Lives remaining: {lives}")
            print(f"{' '.join(blanks)}")

            if '_' not in blanks:
                print("\n🎉 Congratulations! You guessed the word correctly!")
                break
        else:
            print(f"\n💀 Game over! The word was: {''.join(word)}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("👋 Thanks for playing! Goodbye.")
            GAME_ON = False