def analise(*seq):
    print('-='*40)
    print('Analisando os valores...')
    for i in seq:
        print(f'{i} ', end='')
    print()
    print(f'Foram passados {len(seq)} valores')
    print(f'O maior valor foi de {max(seq)}')
    print('-='*40)

#programa
analise(1,2,20,4,5)