import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Indisponivel')
else:
    print('conexão ok')