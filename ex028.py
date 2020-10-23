import random
pn = int(input('Que numero estou pensando? '))
#lista = [1, 2, 3, 4, 5]
#n = random.choice(lista)
n = random.randint(0, 5)
if pn==n:
    print('Parabéns você acertou!!!')
else:
    print('Você Perdeu! \n O numero sortiado foi {}'.format(n))
