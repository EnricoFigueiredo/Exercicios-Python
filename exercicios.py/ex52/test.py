import moeda

p = float(input('digite o preço: R$'))
print(f'Ao aumentar 10% de {moeda.moeda(p)} tivemos {moeda.aument(p,10,True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.met(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobra(p,True)}')