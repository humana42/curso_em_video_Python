n = int(input('Digite um numero: '))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print('o numero possui {} unidades'.format(u))
print('o numero possui {} dezena'.format(d))
print('o numero possui {} centena'.format(c))
print('o numero possui {} milhar'.format(m))
