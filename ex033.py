p1 = int(input('Digite um numero: '))
p2 = int(input('Digite um segundo numero: '))
p3 = int(input('Digite um terceiro numero: '))
menor = p1
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p1 and p3 < p2:
    menor = p3
maior = p1
if p2 >p1 and p2 > p3:
    maior = p2
if p3 > p1 and p3> p2:
    maior = p3
print('O maior valor é: {} \nO menor valor é {}'.format(maior, menor))

