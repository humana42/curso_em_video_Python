from random import choice
print('='*15)
print('Jogo JokenPO')
print('='*15)
j1 = int(input('Escolha uma ação: '
      '[1] Pedra'
      '[2] Papel'
      '[3] Tesoura\n'))
lista = [1, 2, 3]
pc = choice(lista)

if j1 == 1 == pc or j1 == 2 == pc or j1 == 3 == pc:
    print('J1: {} \nPC: {} \nEMPATE'.format(j1, pc))

elif j1 == 1 and pc == 2 or pc == 1 and j1 == 2:
    print('J1: {} \nPC: {} \nPAPEL VENCEU'.format(j1, pc))

elif j1 == 1 and pc == 3 or pc == 1 and j1 == 3:
    print('J1: {} \nPC: {} \nPEDRA VENCEU'.format(j1, pc))

elif j1 == 2 and pc == 3 or pc == 2 and j1 == 3:
    print('J1: {} \nPC: {} \nTESOURA VENCEU'.format(j1, pc))

else:
    print('comando invalido! tente novamente!')



