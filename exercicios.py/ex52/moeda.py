#modulos para usar
def aument(preco=0, taxa=0, format=False):
    resp= preco + (preco * taxa /100)
    return resp if not format else moeda(resp)


def diminuir (preco=0, taxa=0, format=False):
    resp = preco - (preco * taxa / 100)
    return resp if not format  else moeda(resp)


def dobra(preco=0, format=False):
    resp = preco * 2
    return resp if not  format else moeda(resp)


def met(preco=0, format=False):
    resp= preco / 2
    return resp if not format else moeda(resp)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, taxaa=100, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobra(preco,True)}')
    print(f'A metade do ppreço: \t{met(preco,True)}')
    print(f'{taxaa}% de aumento: \t{aument(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')

