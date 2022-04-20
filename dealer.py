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