jogador = {}
lista = list()
total=0
indice =1
while True:
    jogador['nome'] = input('Nome do jogado: ')
    partida= int(input('Numero de Partidas jogada: '))
    npartida = []
    for p in range(1, partida+1):
        npartida.append(int(input(f'    Quantos gols na partida {p}? ')))
    jogador['gols'] = npartida[:]
    jogador['total'] = sum(jogador['gols'])
    lista.append(jogador.copy())
    resp = input('Deseja realizar um novo cadastro? [S/N]').strip().upper()
    if resp in 'N':
        break
print('=-'*30)
print('-'*30)
print(f'{"Cod"} {"NOME":<9}{"GOLS":<8}{"TOTAL"}')
for i, v in enumerate(lista):
    print(f' {i}', end='    ')
    for d in v.values():
        print(f'{str(d):<10}', end='')
print()
print('-'*30)
while True:
    escolha = int(input('consultar qual jogador? [para sair: 999] '))
    if escolha == 999:
        print('ENCERRANDO...')
        break
    if escolha >= len(lista):
        print('ERRO! Não existe jogador nesta busca. Tente novamente')
    else:
        print(f'Levantamento do jogador {lista[escolha]["nome"]}')
        for i, g in enumerate(lista[escolha]['gols']):
                print(f'No jogo {i+1} fez {g}')