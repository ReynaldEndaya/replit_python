print('Guess the number!')
print()

number = 500000
guess_counter = 0

while True:
    guess = int(input('Guess a number between 1 and 1,000,000: '))
    if guess == number:
        guess_counter += 1
        print('You guessed correctly ☺️! The number is',number)
        print('It took you',guess_counter,'tries to correctly guess the number')
        break
    elif guess > number:
        guess_counter += 1
        print('Too high!')
        continue
    elif guess < number and guess > 0:
        guess_counter += 1
        print('Too low!')
        continue
    else:
        print('Your guess is out of bounds!')
        exit()