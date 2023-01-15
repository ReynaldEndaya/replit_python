# from getpass import getpass as input

print('This is a rock paper scissor game! Best of three!')
print()

play_again = ""
score_player_1 = 0
score_player_2 = 0

while True:

    player1 = input('Player 1 Enter your choice (R,P,S only!)')
    print()
    player2 = input('Player 2 Enter your choice (R,P,S only!)')
    print()


    if player1 == player2: #code to run when players chose the same
        if player1 == 'R' or player1 == 'r':
            print('You both chose Rock! It\'s a tie!')
        elif player1 == 'S' or player1 == 's':
            print('You both chose Scissors! It\'s a tie')
        elif player1 == 'P' or player1 == 'p':
            print('You both chose Paper! It\'s a tie!')
        else:
            print('Invalid choice!')

    elif player1 == 'R' or player1 == 'r':
        if player2 == 'S' or player2 == 's':
            print('Rock beats Scissors! Player 1 wins')
            score_player_1 += 1
        elif player2 == 'P' or player2 == 'p':
            print('Paper beats Rock! Player 2 wins!')
            score_player_2 += 1
        else:
            print('Invalid choice!')

    elif player1 == 'S' or player1 =='s':
        if player2 == 'P' or player2 == 'p':
            print('Scissor beats Paper! Player 1 wins!')
            score_player_1 += 1
        elif player2 == 'R' or player2 == 'r':
            print('Rock beats Scissor! Player 2 wins!')
            score_player_2 += 1
        else:
            print('Invalid choice!')

    elif player1 == 'P' or player1 == 'p':
        if player2 == 'R' or player2 == 'r':
            print('Paper beats Rock! Player 1 wins!')
            score_player_1 += 1 
        elif player2 == 'S' or player2 == 's':
            print('Scissor beats Paper! Player 2 wins!')
            score_player_2 += 1
        else:
            print('Invalid choice!')
    else:
        print('Invalid choice!')
    print()
    
    print('Player 1 score: ',score_player_1)
    print('Player 2 score: ',score_player_2)
    print()

    if score_player_1 >= 3 or score_player_2 >= 3:
        print('Game Over!!!')
        if score_player_1 > score_player_2:
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
        print()
        exit()
    else:
        continue

                        