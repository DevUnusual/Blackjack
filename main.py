dic = {1 : 'Ás de', 11 : 'Valete de', 12 : 'Dama de', 13 : 'Rei de'}
frase = ''
for i in [1, 12 , 13]:
  if i == 1 or i == 11 or i == 12 or i == 13:
    # card = i.get_carta()
    frase += str(dic.get(i) + str(i))

print(frase)