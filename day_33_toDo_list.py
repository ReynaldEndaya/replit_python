import os,time

toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

header = f'ToDo List Manager'

while True:
  
  print(f'{header: >100}')
  print()
  action = input('''Do you want to view, add, or edit your to do list? 
  
1. View List
2. Add List
3. Edit List

Enter number of your option: ''')
  
  if action == '1':
    print()
    print('Here\'s your to do!')
    printList()
    time.sleep(2)
    os.system("clear")
  
  elif action == '2':
    print()
    toDo = input('Input your to do: ')
    toDoList.append(toDo)
    print()
    time.sleep(1)
    os.system("clear")
  
  elif action == '3':
    print()
    print('Here\'s your current to do list')
    printList()
    toDo = input('Input item to remove: ')
    if toDo in toDoList:
      toDoList.remove(toDo)
      print()
    else:
      print('Item is not in list')
      printList()
      time.sleep(1)
      os.system("clear")
  
  else:
    print('Invalid Option! Please select again')
    continue
    