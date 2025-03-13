import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31m SITE PUDIM NÃO ESTÁ ACESSIVEL NO MOMENTO\031')
else:
    print('CONSEGUI ACESSAR!!!')