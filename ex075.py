tupla = (int(input('Digite o valor:')), int(input('Digite o valor:')), int(input('Digite o valor:')), int(input('Digite o valor:')))
print(f'Os valores digitado foram {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)}')
if 3 in tupla:
    print(f'O valor 3 apareceu no indice {tupla.index(3)+1}')
else:
    print('Não ha valores 3 na tupla9')
for n in tupla:
    if n % 2 == 0:
        print(f'{n} é par', end='')

