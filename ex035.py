r1 = float(input('Digite o primeiro comprimento de reta: '))
r2 = float(input('Digite o segundo comprimento de reta: '))
r3 = float(input('Digite o terceiro comprimento de reta: '))
if r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 + r2:
    print('O seguimento de reta podem formar um triangulo!')
else:
    print('O seguimento de reta não podem formar um triangulo!')
