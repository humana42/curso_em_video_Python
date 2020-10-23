lista = []
c = 0
for n in range(0, 5):
    valor = int(input('Digite um valor:'))
    if n == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        while c <= len(lista):
            if valor <= lista[c]:
                lista.insert(c, valor)
                break
            c+=1
print(lista)

