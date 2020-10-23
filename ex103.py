def jogador(nome="<desconhecido>", gols=0 ):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols')

jogador(input('Nome: '), input('Quantidade de Gols: '))