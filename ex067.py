cont = 0
while True:
    n = (int(input('Quer ver a tabuada de qual numero? ')))
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} X {cont} = {n*cont}')
        cont += 1