matriz = [0,0,0], [0,0,0], [0,0,0]
somapar = somacol = maiorlin = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-'*40)
for l in range(0,3):
        somacol += matriz[l][2]
for c in range(0, 3):
        if matriz[1][c] == 0:
            maiorlin = matriz[2][c]
        elif matriz[1][c] > maiorlin:
            maiorlin = matriz[1][c]
print(f'A soma dos valres par é de: {somapar}')
print(f'A soma dos numeros da terceira coluna é de: {somacol}')
print(f'O maior numero da segunda linha é o: {maiorlin}')
