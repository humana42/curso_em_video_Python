qtd = total = menor = 0
while True:
    print('-'*20)
    print('LOJA BARATÃO')
    print('-'*20)
    prod = input('Produto: ').strip()
    preco = float(input('Preço: R$'))
    continuar = ' '
    total += preco
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
    else:
        menor = preco
        if preco > 1000:
            qtd += 1
        if preco <= menor:
            menor += preco
            menorProd = prod
print(f'O Valor total: R${total:.2f}')
print(f'A quantidade de produtor maior de R$1000.00 foi de {qtd}')
print(f'O produto mais barato foi {menorProd}')
