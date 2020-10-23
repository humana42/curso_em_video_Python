n = int(input('Digite um numero: '))
v = int(input('Escolha uma converção: \n1-Binário \n2-Octal \n3-Hexadecimal: '))
if v==1:
    print('O valor escolhido foi Binário \n{}'.format(bin(n)[2:]))
elif v==2:
    print('O valor escolhido foi Octal \n{}'.format(oct(n)[2:]))
else:
    print('O valor escolhido foi Hexadecimal \n{}'.format(hex(n)[2:]))

