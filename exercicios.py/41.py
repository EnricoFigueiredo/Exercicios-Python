num = (int(input('digite um número: ')),
      int(input('digite um número: ')),
      int(input('digite um número: ')),
      int(input('digite um número: ')))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu {num.index(3)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)} posição')
else:
    print(f'O valor 3 não foi digitado ')
print(f'Os valores pares digitados foram' , end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')