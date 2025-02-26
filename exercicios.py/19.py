idade= int(input('Digite sua idade: '))

alistamento = 18 - idade


if idade == 18:
    print('Voce precisa se alistar')
elif idade <= 17:
    print(f'novo pra se alistar faltam {alistamento} ano(s) para se alistar')
elif idade >= 19:
    print(f'Muito velho passou anos do prazo')

