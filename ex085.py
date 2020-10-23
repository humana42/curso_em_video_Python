num = []
par = []
impar = []
for n in range(0,5):
    num.append(int(input('Digite um valor: ')))
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
num.clear()
num.append(impar)
num.append(par)
num[0].sort()
num[1].sort()
print(num)
