from time import sleep
from random import randint
print('='*10,'SORTEIO MEGASENA', '='*10)
qtd = int(input('Quantos jogos você quer fazer? '))
print('=-'*15)
print('         SORTEANDO ...     ')
print('-='*15)
n=1
sorteio = []
jogos = list()
while n <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont >= 6:
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    n +=1
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
    sleep(1)
print('=-'*5, 'BOA SORTE!', '=-'*5)