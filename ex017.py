import math
cad = float(input('Digite o cateto adjacente: '))
cop = float(input('Digite o cateto oposto: '))
print('A hipotenusa do triangulo retangulo é: {:.2f}'.format(math.hypot(cad, cop)))
