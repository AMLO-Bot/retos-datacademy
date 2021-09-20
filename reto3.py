# Reto 3 - Conversor de millas a kilómetros
# Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. 
# Para no estar repitiendo este cálculo escribe un programa en que el usuario indique
# una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.
# Toma en cuenta que en cada milla hay 1.609344 Km
# Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.
import os

def miles2km():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Miles to Kilometers Conversion\n')
  miles = float(input('Enter Miles: '))
  conv_factor = 1.609344
  km = miles * conv_factor
  print(f'Miles: {miles} => Km: {km}\n')
  input('Press any key to continue')

def km2miles():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Kilometers to Miles Conversion\n')
  km = float(input('Enter Km: '))
  conv_factor = 0.62137119223
  miles = km * conv_factor
  print(f'Km: {km} => Miles: {miles}\n')
  input('Press any key to continue')
  
menu_options = {
  1: 'miles2km',
  2: 'km2miles',
  3: 'exit',
}

def print_menu():
  for key in menu_options.keys():
    print(key, '-', menu_options[key])

def convert_distance():
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome Boi to Conversion Script')
    print_menu();
    try:
      option = int(input('\nType the number of your conversion\n'))
    except:
      print('Input must be a number')

    # Trigger function according to selected menu_options
    if option == 1:
      miles2km()
    elif option == 2:
      km2miles()
    elif option == 3:
      exit()  
    else:
      print('Pick an option from the menu')  

if __name__ == '__main__':
  convert_distance()  