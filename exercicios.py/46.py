def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade and idade < 18 or idade < 65:
        return f'Com {idade} anos: NÃO É OBRIGADO A VOTAR'
    else:
        return f'Com {idade} anos: Obrigado a votar'

nasc = int(input('Qual ano voce nasceu?: '))
print(voto(nasc))