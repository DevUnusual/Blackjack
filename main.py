from dealer import Dealer

def somarTotal(mao):
  total = 0
  for i in mao:
    x = i.get_carta()[1]
    if x == 11 or x == 12 or x == 13:
      total += 10
    elif x == 1:
      total += 11
    else:
      total += x
  return total


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

print(f'\nPlacar \nMesa:{somarTotal(dealermesa.getCards())} | player:{somarTotal(player)}\n')

while(True):
  print('DECISAO:')
  decision = int(input('1 - MAIS UMA CARTA? \n2 - FINALIZAR JOGO\n->'))

  if decision == 1:
    player.append(dealermesa.darCarta())
    print('Suas cartas:')
    for i in player:
      print(i)

  elif decision == 2:
    dealermesa.cartaDealer()

    print('mesa puxa uma carta ficando com:')
    print(dealermesa)
    print('Suas cartas:')
    for i in player:
      print(i)

    dealerPoint = somarTotal(dealermesa.getCards())
    playerPoint = somarTotal(player)

    print(f'dealer: {dealerPoint} | player: {playerPoint}')
    if dealerPoint >= playerPoint and dealerPoint <=21:
      print('A mesa ganhou.')
    elif dealerPoint <= playerPoint and playerPoint <= 21:
      print('Parabens voce ganhou.')
    elif dealerPoint > 21 and playerPoint > 21 :
      print('A mesa ganhou.')
    break


