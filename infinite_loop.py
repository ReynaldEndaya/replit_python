from getpass import getpass as input

print('This is a rock paper scissor game!')

play_again = ""

while play_again != 'n':

    player1 = input('Player 1 Enter your choice (R,P,S only!)')
    print()
    player2 = input('Player 2 Enter your choice (R,P,S only!)')
    print()

    if player1 == player2:
        if player1 == 'R':
            print('You both chose Rock! It\'s a tie')
        elif player1 == 'S':
            print('You both chose Scissors! It\'s a tie')
        else:
            print('You both chose Paper! It\'s a tie!')

    elif player1 == 'R':
        if player2 == 'S':
            print('Rock beats Scissors! Player 1 wins')
        else:
            print('Paper beats Rock! Player 2 wins!')

    elif player1 == 'S':
        if player2 == 'P':
            print('Scissor beats Paper! Player 1 wins!')
        else:
            print('Rock beats Scissors! Player 2 wins')

    else:
        if player2 == 'R':
            print('Paper beats Rock! Player 1 wins!')
        else:
            print('Scissor beats Paper! Player 2 wins!')
    print()
    play_again = input('Do you want to play again? (y|n) ')
    print()
