from random import randint
v =0
while True:
    jogador = int(input('Diga um Valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tp =' '
    while tp not in 'PI':
        tp = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o PC jogou {pc} total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tp == 'P':
        if total % 2 == 0:
         print('Voce Venceu!!')
         v+= 1
        else:
         print('Voce Perdeu :(')
        break
    elif tp == 'I':
       if total % 2 == 1:
          print('Voce Venceu!!')
          v += 1
       else:
          print('voce perdeu')
          break
    print('Vamos jogar novamente...')
print(f'GAME OVER! VOCE VENCEU {v} vezes')