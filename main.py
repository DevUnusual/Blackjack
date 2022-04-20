from dealer import Dealer

print('Bem vindo ao blackjack')
player = []
dealermesa = Dealer()

dealermesa.initdealer()
player = dealermesa.iniciarGame()

print('cartas da mesa:')
print(dealermesa)

print('Suas cartas:')
for i in player:
  print(i)

print('DECISAO:')
decision = int(input('1 - MAIS UMA CARTA \n2 - FINALIZAR JOGO'))

if decision == 1:
  player.append(dealermesa.darCarta())
elif decision == 2:
  dealermesa.getCards().somarMao


