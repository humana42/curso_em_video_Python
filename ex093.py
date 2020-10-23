jogador = {}
total=0
jogador['nome'] = input('Nome do jogado: ')
partida= int(input('Numero de Partidas jogada: '))
npartida = []
for p in range(1, partida+1):
    npartida.append(int(input(f'    Quantos gols na partida {p}? ')))
jogador['gols'] = npartida[:]
jogador['total'] = sum(npartida)
print('=+'*30)
print(jogador)
print('=+'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('=+'*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["total"]} partidas.')
for p,i in enumerate(npartida):
    print(f'    => Na partida {p+1}, fez {i} gols')
print(f'Foi um total de {jogador["total"]} gols')
