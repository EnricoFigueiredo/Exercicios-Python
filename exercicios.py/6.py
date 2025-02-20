nome= (input('Digite seu nome: '))
print(f'Bem vindo(a) {nome},\n Vamos cacular sua média!')

n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda  nota: '))
n3= float(input('Digite a terceira  nota: '))

media= (n1 + n2 + n3) / 3
if media >= 9:
    print(f' EXCELENTE!! Aprovado {media:.2f}')
elif 7 <=media < 9:
    print(f'Aprovado! {media:.2f} ')
else:
  print(f'VOCÊ REPROVOU {media:.2f} ')
