from random import shuffle
a1 = input('Digite um nome: ')
a2 = input('Digite um segundo nome: ')
a3 = input('Digite um terceiro nome: ')
a4 = input('Digite um quarto nome: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('O nome escolhido é: {}'.format(lista))
