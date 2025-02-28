tg = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Qual o nome do Produto?: '))
    preco = float(input('Qual o Preço? R$: '))
    cont += 1
    tg += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA '))
print(f'O total da compra foi {tg:.2f} ')
print(f'Tem {totmil} custando mais de R$ 1.000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f} ')