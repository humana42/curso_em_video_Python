def fatorial(n, show=False):
    """
    Calcula o fatorial de um numero n
    show=para mostra detalhes da conta
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c >1 :
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f

#programa
print(fatorial(3, show=False))
