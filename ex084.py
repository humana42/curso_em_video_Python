pessoas = []
dados = []
cad = maior = menor =0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cad += 1
    res = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if res == 'N':
        break
print(f'Foram cadastrada {cad} pessoas')
print('Maiores pessoas foram de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ')
print('Menores pesos foram de ', end='')
for p in  pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
