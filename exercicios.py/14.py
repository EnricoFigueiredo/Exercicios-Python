# Faça um programa que tenha uma função chamada ÁREA()
# que receba as dimensões de um terreno retangular (larg e comp)
# mostre a área do terreno

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é de {a}m2. ')



print('Controle de Terrenos')
print('-'*20)
larg = float(input('largura (m): '))
comp = float(input('comprimento (m): '))
area(larg, comp)  