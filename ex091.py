from random import randint
from time import sleep
from operator import itemgetter
sorteados = { 'Jogador 1': randint(1,6),
              'Jogador 2': randint(1,6),
              'Jogador 3': randint(1,6),
              'Jogador 4': randint(1,6)}
print('Valores Sorteados:')
rank = []
for k, v in sorteados.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
rank = sorted(sorteados.items(), key=itemgetter(1), reverse=True)
print('+'*30)
for i, l in enumerate(rank):
    print(f'{i+1} lugar: {l[0]} com {l[1]}')
    sleep(1)