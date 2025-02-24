dia = int(input('Quantos dias alugados?: '))
km = float(input('Quantos KM foram rodados?: '))
preco_dia = 60
preco_km = 0.15

soma = (dia * preco_dia) + (preco_km * km)

print(f'O valor do carro pelos {dia} dias e {km}km percorridos foram no total de R${soma:.2f}')