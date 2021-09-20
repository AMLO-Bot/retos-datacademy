# Reto 2 - Piedra, papel o tijera
# Este es un juego en el que nunca fui bueno, pero eso no significa que hacer un programa sea difícil.
# Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el jugador 1 o el jugador 2.
# def ppt(player1, player2):
#   options = {
#     'tijeras': 'papel',
#     'papel': 'piedra',
#     'piedra': 'tijera',
#   }

#   if player1 == player2:
#     winner = 'Es empate padre santo'
#   elif options[player1] == player2:
#     winner = 'El ganador es player 1'
#   else :
#     winner = 'El ganador es player 2'
      
#   return winner 

# print(ppt('papel', 'tijeras'))

# Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.
# ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2
import os

def ppt():
  match_counter = 1
  wins_p1 = 0
  wins_p2 = 0
  winner_prompt = ''
  options = {
    'tijeras': 'papel',
    'papel': 'piedra',
    'piedra': 'tijeras',
  }
  print('Piedra, papel o tijeras\n2 de 3')

  while wins_p1 < 3 or wins_p2 < 3:
    print(f'\nMATCH: {match_counter}')
    print('Escribe un movimiento \n tijeras \n papel \n piedra')
    move_p1 = input('\nPick a movement Player 1 \n').strip().lower()
    move_p2 = input('\nPick a movement Player 2 \n').strip().lower()

    if move_p1 == move_p2:
      input('\nFue empate\nPresiona cualquier tecla para continuar')
    elif options[move_p1] == move_p2:
      wins_p1 += 1;
      input('\nPlayer 1 se lleva el match\nPresiona cualquier tecla para continuar')
    else :
      wins_p2 += 1;
      input('\nPlayer 2 se lleva el match\nPresiona cualquier tecla para continuar')

    match_counter += 1
    os.system('cls' if os.name == 'nt' else 'clear')

  if wins_p1 == 2:
    winner_prompt = 'Player 1, ganaste 3 sets padre'
  if wins_p2 == 2:
    winner_prompt = 'Player 2, ganaste 3 sets padre'

  return winner_prompt
  
print(ppt())

