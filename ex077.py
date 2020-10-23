palavras = ('arroz', 'feijão', 'bife', 'ovo', 'macarrao', 'maionese', 'pao', 'leite', 'iorgut', 'cenoura')
for p in palavras:
    print(f'\nPara palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
