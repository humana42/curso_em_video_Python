from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Valores sorteados')
for i in n:
    print(i, end=' ')
print(f'\nMaior valor: {max(n)}')
print(f'Menor valor: {min(n)}')
