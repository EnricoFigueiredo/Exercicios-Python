velocidade = float(input('Qual a velocidade atual do carro?: '))
if velocidade > 80:
    print(f'MULTADO! Voce excedeu o limite permitido de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'Voce deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia!')