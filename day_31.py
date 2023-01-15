import os,time

def colorizer(color):
  if color == 'red':
    return "\033[0;31m"
  elif color == 'white':
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

heading = f'{red}={white}={blue}={yellow} Music App {red}={white}={blue}='
radio_gaga = 'Radio Gaga'
queen_text = 'Queen'



# print()
print(f'{heading: ^100}')
print(f'🔥▶️',end='')
print(f'{white}{radio_gaga: ^15}')
print(f'{yellow}{queen_text: ^15}')