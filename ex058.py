import random
pn = int(input('Que numero estou pensando? '))
n = random.randint(0, 10)
while pn != n:
    print('Você errou!!! Tente novamente')
    pn = int(input('Que numero estou pensando? '))
print('Parabéns você acertou!!!')