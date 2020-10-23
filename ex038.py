n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo numero: '))
if n1 == n2:
    print('Operação invalida!')
elif n1 > n2:
    print('O numero {} é maior e {} é menor'.format(n1, n2))
elif n2 > n1:
    print('O numero {} é maior e o {} é menor'.format(n2, n1))
