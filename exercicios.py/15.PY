"""
Faça um programa que tenha uma função chamada escreve(), quee receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
"""
def escreva(msg):
   tam = len(msg) + 3
   print('~' * tam)
   print(f'{msg}')
   print('~' * tam)



escreva('Enrico Figueiredo')
escreva('Python 3')
escreva('Oi')