valor = []
valor.append(int(input('Digite um valor: ')))
while True:
    res = input('Deseja continuar: [S/N]').upper().strip()[0]
    if res == 'N':
        break
    else:
        dig = int(input('Digite um valor: '))
        if dig in valor:
            print('Valor já existe na lista!')
        else:
            valor.append(dig)
            print('Valor adicionado...')
print(valor)

