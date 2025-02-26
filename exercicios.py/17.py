# Condições Aninhadas

v = float(input('Qual o valor da casa?: R$'))
s = float(input('Qual é o seu salário?: R$ '))
a = int(input('Qauntos anos de financiamento?: '))
p= v / (a * 12)
mini= s * 30 / 100
print(f'Para pagar uma casa de R${v:.2f} em {a} anos \n')
print(f'a prestação será de R${p:.2f}')

if p <= mini:
    print('Empretestimo concedido!')
else:
    print('Emprestimo negado.')