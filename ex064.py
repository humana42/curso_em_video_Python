n = 0
total = 0
while n != 999:
    n = int(input('Digite um numero [Digite 999 para parar]: '))
    if n != 999:
        total += n
    else:
        print('A soma é: {}'.format(total))
        print('FIM')
