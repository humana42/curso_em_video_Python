c = ('\033[m',           #0 sem cores
     '\033[0;30;41m',    #1 vermelho
     '\033[0;30;42m',    #2 verde
     '\033[0;30;43m',    #3 amarelo
     '\033[0;30;44m',    #4 azul
     '\033[0;30;45m',    #5 roxo
     '\033[7;30m'       #6 branco
     )
def ajuda(comand):
    titulo(f'Acessando a bibliote do comando {comand}', 4)
    print(c[6], end='')
    help(comand)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')

#programa
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando = input('Função da Biblioteca >', )
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)