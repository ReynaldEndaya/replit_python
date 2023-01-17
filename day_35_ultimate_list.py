import os,time

toDoList = []

def clearDisplay(timeout):
  time.sleep(timeout)
  os.system("clear")

def printList():
  print()
  counter = 1
  for item in toDoList:
    print(f'{counter}: {item}')
    counter += 1
  print()

def editList():
  print()
  printList()
  taskToRemove = input('Enter name of task that you want to edit: ')
  newTask = input('\nEnter name of new task: ')
  index = toDoList.index(taskToRemove)
  toDoList[int(index)] = newTask 
  print()
  print('Here\'s your new task list\n')
  printList()    

def addList():
  print()
  toDo = input('Input your to do: ')
  if toDo not in toDoList:
    toDoList.append(toDo)
  else:
    print()
    print('Cannot add item as it is already in list!')
  print()

def removeItem():
  print()
  print('Here\'s your current to do list')
  printList()
  toDo = input('Input item to remove: ')
  if toDo in toDoList:
    confirm = input('Do you really want to remove this item? (y|n): ')
    if confirm == 'y':
      toDoList.remove(toDo)
    else:
      print('Item not removed!')
    print()
  else:
    print('Item is not in list')
    printList()

def deleteList():
  print()
  confirm = input('Are you sure you want to delete the entire list? (y|n): ')
  if confirm == 'y':
    toDoList.clear()
  else:
    print('List is not deleted!')
      

while True:
  
  header = f'ToDo List Manager'
  print(f'{header: >100}')
  print()
  action = input('''Do you want to view, add, or edit your to do list? 
  
1. View List
2. Add List
3. Edit List
4. Remove Item
5. Delete List

Enter number of your option: ''')
  
  if action == '1':
    print()
    print('Here\'s your to do!')
    printList()
    clearDisplay(2)
  
  elif action == '2':
    addList()
    clearDisplay(1.5)
  
  elif action == '3':
    editList()
    clearDisplay(1)
  
  elif action == '4':
    removeItem()
    clearDisplay(1)
    
  elif action == '5':
    deleteList()
    clearDisplay(1)
    
  else:
    print('Invalid Option! Please select again')
    continue