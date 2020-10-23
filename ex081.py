lista = []
c = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    c+=1
    res = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if res == 'N':
        break
print(f'A lista possui {c} valores')
print(f'A lista decrescente é: {lista.sort(reverse=True)}')
if 5 in lista:
   print('O numero 5 esta presente na lista ')
else:
   print('O numero 5 não esta presente na lista')