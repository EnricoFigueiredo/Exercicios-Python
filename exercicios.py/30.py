n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
     [1] somar 
     [2] multipicar
     [3] maior
     [4] novos números
     [5] sair do programa     ''')
    opcao = int(input('Qual é a sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'a soma de {n1} + {n2} = {soma}')

    elif opcao == 2:
        mult = n1 * n2
        print(f'a multipicação de {n1} X {n2} = {mult}')

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior= n2

    elif opcao == 4:
        print('Informe os Numeros novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('FINALIZANDO....')

    else:
        print('Opção Inválida, Tente Novamente')
    print('=-=' * 10) 
    
print('Fim do programa! Volte sempre!!')