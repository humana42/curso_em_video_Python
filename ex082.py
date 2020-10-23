lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    res = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if res == 'N':
        break
for i, n in enumerate(lista):
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Lista digitada {lista}')
print(f'Os numero pares da lista são {par}')
print(f'Os numero impares da lista são {impar}')


