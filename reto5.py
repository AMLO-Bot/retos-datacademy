# Reto 5 - Rangos cambiantes
# Para este reto final juguemos con números. En tu programa pide al usuario ingresar 3 números: un límite inferior, un límite superior y uno de comparación.
# Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.
# En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y
# pide ingresar otro número para repetir el proceso.
import os
def range(lower_limit, upper_limit, compare):
  in_range = False

  while in_range == False:
    if lower_limit <= compare <= upper_limit:
      print(compare)
      in_range = True
    elif compare < lower_limit or compare > upper_limit:
      print(f'\nNumber {compare} is out of range')
      try:
        print(f'Range {lower_limit} - {upper_limit}')
        compare = int(input('Input a number inside the range\n'))
      except:
        print('Input must be a number')  
    os.system('cls' if os.name == 'nt' else 'clear')

range(12,56,5)