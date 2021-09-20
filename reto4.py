# Reto 4 - Calculadora de volúmenes
# Sigamos con matemáticas elementales para no perder la costumbre y retar nuestras habilidades. 
# Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen de un cilindro.
# Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. Aplica las fórmulas en tu programa 
# recibiendo datos como altura y radio.
# import math
# def get_volume(radius, height):
#   a_base = math.pi * (radius ** 2)
#   volume = a_base * height
#   return volume 
# print(get_volume(1, math.pi))
# Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.
import os
import math

menu_options = {
    1: 'Cone',
    2: 'Square',
    3: 'Cylinder',
    4: 'Sphere',
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def handle_cone():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Volumen del Cono\n')
  print('Ingrese radio y altura\n')
  try:
    radio = float(input('Radio: '))
    height = float(input('Altura: '))
  except:
    print('Input must be a number')
  volume = round(math.pi * (radio ** 2) * height / 3, 2)
  print(f'Volumen: {volume}\n')  

def handle_square():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Volumen del Cubo\n')
  print('Ingrese lado\n')
  try:
    side = float(input('Lado: '))
  except:
    print('Input must be a number')
  volume = round(side ** 3, 2)
  print(f'Volumen: {volume}\n')  

def handle_cylinder():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Volumen del Clindro\n')
  print('Ingrese radio y altura\n')
  try:
    radio = float(input('Radio: '))
    height = float(input('Altura: '))
  except:
    print('Input must be a number')
  volume = round(math.pi * (radio ** 2) * height, 2)
  print(f'Volumen: {volume}\n')  

def handle_sphere():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Volumen de la Esfera\n')
  print('Ingrese radio\n')
  try:
    radio = float(input('Radio: '))
  except:
    print('Input must be a number')
  volume = round(math.pi * (radio ** 3) * 4/3, 2)
  print(f'Volumen: {volume}\n')  

def calc_volumes():
  while(True):
    print_menu()
    # option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    #Check what choice was entered and act accordingly
    if option == 1:
        handle_cone()
    elif option == 2:
      handle_square()
    elif option == 3:
      handle_cylinder()        
    elif option == 4:
        handle_cone()
    elif option == 5:
      exit('Come back soon \\UwU/')          
    else:
        print('Invalid option. Please enter a number between 1 and 4.')
        

if __name__=='__main__':
    calc_volumes()