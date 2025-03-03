lista = []
mai = 0
men = 0 

for c in range(0,5):
    lista.append(int(input(f'Digite uma valor para a Posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print(f' Voce digitou os valores {lista}')
print(f' O maior Valor digitado foi {mai} nas posições',   end = '')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}   ', end='')
print()
print(f'O menor valor foi {men} nas posições',   end = '')
for i, v in enumerate(lista):
     if v == men:
             print(f'{i}   ', end='')
print()

    