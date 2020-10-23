from time import sleep
def contagem(a,b, c):
    print(f'Contagem de inicio {a} atém fim {b} de {c} em {c}')
    cont = a
    sleep(1)
    if c < 0:
        c*= -1
    if c == 0:
        c = 1
    if a < b:
        while cont <= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont+=c
        print('\n FIM!')
    else:
        while cont >= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -=c
        print('\nFIM!')


#programa
contagem(1,10,2)
print('-'*20)
contagem(10, 0, 22)
print('Agora é seu vez de personalizar!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
cont = int(input('Contador: '))
contagem(i,f,cont)