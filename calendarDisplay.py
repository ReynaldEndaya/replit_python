print('This is a calendar!\n')

monthNumber = int(input('Enter Month Number: '))

if monthNumber == 2:
    i = 28
elif monthNumber <=7 and (monthNumber % 2) != 0:
    i = 31
elif monthNumber >= 8 and (monthNumber % 2) != 0:
    i = 30
else:
    i = 31

for days in range(1,i+11):
    print(days, sep=" ", end=" ")