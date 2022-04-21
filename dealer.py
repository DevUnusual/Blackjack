import cartas

class Dealer():
  def __init__(self):
    self.mao = []
    self.baralho = cartas.Baralho()
  
  def __str__(self):
    ret = ''
    for i in self.mao:
      ret += str(str(i) + ' \n')

    return ret

  def initdealer(self):
    self.mao.append(self.baralho.pushCarta())
    self.mao.append(self.baralho.pushCarta())

  def iniciarGame(self):
    cards = []
    cards.append(self.baralho.pushCarta())
    cards.append(self.baralho.pushCarta())
    return cards
  
  def darCarta(self):
    return self.baralho.pushCarta()

  def cartaDealer(self):
    self.mao.append(self.baralho.pushCarta())

  def getCards(self):
    return self.mao

  def getTotal(self):
    total = 0
    for i in self.mao:
      x = i.get_carta()[1]
    if x == 11 or x == 12 or x == 13:
      total += 10
    elif x == 1:
      total += 11
    else:
      total += x
    return total