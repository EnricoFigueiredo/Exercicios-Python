times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia'
         'São Paulo', 'Fluminense', 'Sport Recife', 
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')

print('=' * 15)
print(f'Lista e Times do Brasileirão {times}')
print('=' * 15)
print(f'os 5 primeiros times são {times[0:5]}')
print('=' * 15)
print(f'Os 4 últimos são{times[-4:]}')
print('=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 20)
print(f'O chapecoense está na {times.index("Chapecoense") + 1} posição')