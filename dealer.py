import cartas

class Dealer():
  def __init__(self):
    self.mao = []
    self.baralho = cartas.Baralho()

  def darCarta(self):
    return self.baralho.pushCarta()

  def cartaDealer(self):
    self.mao.append(self.baralho.pushCarta())