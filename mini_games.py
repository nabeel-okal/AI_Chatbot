import random

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
        
        COMPUTER = random.randint(0, len(choices) - 1)


        if PLAYER == 'rock':
            if COMPUTER == 'rock':
                print("It's a draw!")
            elif COMPUTER == 'paper':
                print('I won! . Better Luck next time.')
            else:
                print('You won! . Congrats!')

        if PLAYER == 'paper':
            if COMPUTER == 'rock':
                print('You won! . Congrats!')
            elif COMPUTER == 'paper':
                print("It's a draw!")
            else:
                print('I won! . Better Luck next time.')

        if PLAYER == 'scissors':
            if COMPUTER == 'rock':
                print('I won! . Better luck next time.')
            elif COMPUTER == 'paper':
                print('You won! . Congrats!')
            else:
                print("It's a draw!")
        
        # Check if the user wants to play another game
        PLAY_AGAIN = input('Would you like to play another game?').lower()

        if PLAY_AGAIN in ['no', 'n']:
            GAME_ON == False

# ADD: Guess the word game