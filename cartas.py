from random import randint

class Carta():
  def __init__(self, naipe, valor):
    self.naipe = naipe
    self.valor = valor

  def __str__(self):
    dic = {1 : 'Ás de ', 11 : 'Valete de ', 12 : 'Dama de ', 13 : 'Rei de '}
    frase = ''
    if self.valor == 1 or self.valor == 11 or self.valor == 12 or self.valor == 13:
      frase += str(dic.get(self.valor) + self.naipe)
    else:
      frase += str(str(self.valor) +' de '+ self.naipe)
    return frase
  
  def get_carta(self):
    return (self.naipe, self.valor)

class Baralho():
  def __init__(self):
    self.baralho = []
    for i in ['Copas', 'Espada', 'Paus', 'Ouro']:
      for j in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
        self.baralho.append(Carta(i, j))

  def pushCarta(self):
    choseOne = self.baralho.pop(randint(0, (len(self.baralho)-1)))
    return choseOne 
  
  def devolverCarta(self, carta):
    self.baralho.append(carta)

class Mao():
  def __init__(self):
    self.mao = [Carta]

  def __str__(self):
    dic = {1 : 'Ás de ', 11 : 'Valete de ', 12 : 'Dama de ', 13 : 'Rei de '}
    frase = ''
    for i in self.mao:
      if i == 1 or i == 11 or i == 12 or i == 13:
        card = i.get_carta()
        frase += str(dic.get(card[1]) + card[0])
      else:
        card = i.get_carta()
        frase += str(str(card[1]) + card[0])
    return frase
  
  def pegarCarta(self, card : Carta):
    self.mao.append(card)
  
  