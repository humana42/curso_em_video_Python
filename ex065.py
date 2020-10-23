resp = 'S'
soma = qtd = media = maior = menor = 0
while resp in 'S':
    n = int(input('Digite o valor: '))
    soma += n
    qtd += 1
    if qtd == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
media = soma/qtd
print('A media é {:.1f}'.format(media))
print('O maior valor é {} e o menor valor {}'.format(maior, menor))