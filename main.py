from dealer import Dealer
import cartas

print('Bem vindo ao blackjack')
participantes = int(input('Quantos jogadores vao participar? \n'))
players = []
dealermesa = Dealer()

dealermesa.initdealer()
for i in range(participantes):
  players.append(dealermesa.iniciarGame())

for i in players:
  for j in i:
    print(j)