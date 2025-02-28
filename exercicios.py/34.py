
while True:
    tab = int(input('Digite um número para tabuada: '))
    if tab < 0:
        break
    print('-' * 20)
    for n in range(1, 11):
        print(f' {tab} X {n} = {tab * n}')
    print('-' * 20)
