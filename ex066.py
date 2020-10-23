cont = soma = 0
while True:
    n = int(input('Digite um numero: [use 999 para parar]'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A quantidade de numero digitado foi {cont} e a soma dos valores é de {soma}')

