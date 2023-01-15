import os,time

def colorizer(color):
  if color == 'red':
    return "\033[0;31m"
  elif color == '5':
    return "\033[1;37m"
  elif color == 'blue':
    return "\033[0;34m"
  elif color == 'yellow':
    return "\033[1;33m"
  else:
    return "\033[0m"

red = colorizer('red')
white = colorizer('white')
blue = colorizer('blue')
yellow = colorizer('yellow')

heading_1 = f'{white}WELCOME TO'
heading_2 = f'{blue}-- ARMBOOK --'
text_1 = f'Definitely not a rip off of'
text_2 = f'a certain other social'
text_3 = f'networking site'
text_4 = f'Honest.'
text_5 = f'Username:'
text_6 = f'Password:'

# print()
print(f'{heading_1: ^50}')
print(f'{heading_2: ^50}')
print()
print(f'{yellow}{text_1: ^50}')
print(f'{yellow}{text_2: >38}')
print(f'{yellow}{text_3: >38}')
print()
print(f'{red}{text_4: ^45}')
print()
print(f'{white}{text_5: ^45}')
print(f'{white}{text_6: ^45}')
