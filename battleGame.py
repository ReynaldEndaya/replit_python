import random, time, os


def characterGenerator():
  name = input('Name your legend: ')
  type = input('Character Type: ')
  print()
  return name

def diceRand(sides):
  dice = random.randint(1, sides)
  return dice


def healthStats():
  health = ((diceRand(6) * diceRand(12)) / 2 + 10)
  return health


def strengthStats():
  strength = ((diceRand(6) * diceRand(12)) / 2 + 12)
  return strength

os.system("clear")
print('⚔️ BATTLE TIME ⚔️')

firstPlayerName = characterGenerator()
print(firstPlayerName)
time.sleep(1)
firstPlayerHealth = healthStats()
print('HEALTH:', firstPlayerHealth)
time.sleep(1)
firstPlayerStrength = strengthStats()
print('STRENGTH:', firstPlayerStrength)

print()
print('Who are they battling?')
print()

secondPlayerName = characterGenerator()
print(secondPlayerName)
time.sleep(1)
secondPlayerHealth = healthStats()
print('HEALTH:', secondPlayerHealth)
time.sleep(1)
secondPlayerStrength = strengthStats()
print('STRENGTH:', secondPlayerStrength)
os.system('clear')
print('The battle begins!')

while True:
  
    print()
    firstPlayerRollDice = diceRand(6)
    secondPlayerRollDice = diceRand(6)
    strengthDifference = (firstPlayerStrength - secondPlayerStrength) + 1
    
    print(firstPlayerName,'rolled',firstPlayerRollDice)
    time.sleep(1)
    print(secondPlayerName,'rolled',secondPlayerRollDice)
    time.sleep(1)
    print()

    if firstPlayerRollDice > secondPlayerRollDice:
        secondPlayerHealth -= abs(strengthDifference)
    elif secondPlayerRollDice > firstPlayerRollDice:
        firstPlayerHealth -= abs(strengthDifference)
    else:
        print('Roll Dice Draw!')
        print('Re-rolling...')
        time.sleep(1)
        continue
    
    print(firstPlayerName)
    print('HEALTH:', firstPlayerHealth)
    print()
    time.sleep(1)
    print(secondPlayerName)
    print('HEALTH:', secondPlayerHealth)
    time.sleep(2)

    if firstPlayerHealth < 0 or secondPlayerHealth < 0:
        os.system('clear')
        print('Game Over!')
        print()
        if firstPlayerHealth < 0:
            print(secondPlayerName, 'wins!')
            print()
            print(secondPlayerName, 'has', secondPlayerHealth, 'hp remaining',
                    firstPlayerName, 'has', firstPlayerHealth, 'hp remaining')
            break
        else:
            print(firstPlayerName, 'wins!')
            print()
            print(firstPlayerName, 'has', firstPlayerHealth, 'hp remaining',secondPlayerName, 'has', secondPlayerHealth, 'hp remaining')
            break
    else:
        print()
        print('And they\'re both standing for the next round!')
        time.sleep(1)
        os.system('clear')  
        print('The battle continues!')
        time.sleep(2)
        continue
        
