
namesList = []

def duplicateCheck(fullName):
    if fullName in namesList:
        print('Name is already in list!')
        print()
    else:
        namesList.append(fullName)

def showList():
    counter = 1
    for name in namesList:
        print(f'{counter}. {name}')
        counter = 1
    print()

def addName():
    firstName = input('First Name: ').strip().capitalize()
    lastName = input('Last Name: ').strip().capitalize()
    print()
    return f'{firstName} {lastName}'

fullName = addName()
duplicateCheck(fullName)
print()
showList()

while True:
    
    response = input('Do you want to enter another name? (y|n) ')
    
    if response.lower() == 'y':
        print()
        fullName = addName()
        duplicateCheck(fullName)
        showList()
        print()
        continue
    elif response.lower() == 'n':
        break
    else:
        print(f'Invalid Response! Enter y or n only!')
        continue
        
    