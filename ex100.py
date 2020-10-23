from random import randint
from time import sleep
def sorteio(lista):
    print('Sorteando 5 valores...')
    for i in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.2)

def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma+=i
    print(f'\nA soma dos numeros pares é de {soma}')

#programa
numeros = []
sorteio(numeros)
somapar(numeros)
