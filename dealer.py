import cartas

class Dealer():
  def __init__(self):
    self.mao = []
    self.baralho = cartas.Baralho()

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

  def terminarGame(self, game : list):
    winner = [0,'']
    for i in game:
      if i.somarMao() > winner[0]:
        winner[0] = i.somarMao()
        winner[1] = i
    
    return winner[1]