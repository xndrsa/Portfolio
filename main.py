import random
import time

while True:
#pregunta al usuario
 user_name = input('Ingresa tu nombre ')
 print("Hola ",user_name)
 time.sleep(1)
 print("vamos a jugar")
 time.sleep(1)
 user_option = input('piedra, papel o tijera? => ')

#Seleccion random del sistema
 list1 = (1, 2, 3)
 computer_option = int(random.choice(list1))
 if computer_option == 1:
  computer_option = 'Tijera'
 elif computer_option == 2:
  computer_option = 'Piedra'
 else:
  computer_option = 'Papel'
 print("Yo seleccione ", computer_option)

#Respuestas segun opciones
 if user_option == computer_option:
  print('Tuvimos un Empate!')
 elif user_option.lower() == 'piedra':
  if computer_option == 'Tijera':
     print('Piedra gana a Tijera')
     print(user_name, " gana!")
  else:
     print('Papel gana a Piedra')
     print('Yo Gano!')
 elif user_option.lower() == 'papel':
  if computer_option == 'Piedra':
     print('Papel gana a Piedra')
     print(user_name, " gana!")
  else:
     print('Tijera gana a papel')
     print('Yo Gano!')
 elif user_option.lower() == 'tijera':
  if computer_option == 'Papel':
     print('Tijera gana a Papel')
     print(user_name, " gana!")
  else:
     print('Piedra gana a Tijera')
     Print('Yo Gano!')
 #reinicia el juego   
 play_again = input("Intentamos de nuevo? (s/n): ")
 if play_again.lower() == "n":
   print("Nos vemos pronto")
   time.sleep(1)
   break
