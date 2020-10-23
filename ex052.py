n = int(input('Digite um número: '))
c = 0
for i in range(1, n+1):
    if n % i == 0:
        print(f'\033[0;33m{i}\033[m', end=' ')
        c += 1
    else:
        print(f'\033[0;31m{i}\033[m', end=' ')
if n % 2 == 0:
    print(f'\nO número {n} foi divisível {c} vezes')
    print('Então ele não é um numero primo.')
else:
    print(f'\nO número {n} foi divisível apenas {c} vezes')
    print(f'Então ele é um numero primo.')