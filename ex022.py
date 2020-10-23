nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiusculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome tem um total de letras de: {}'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome tem {} letras'.format(len(separa[0])))
print('O seu primeiro nome tem um total de {} letras'.format(nome.find(' ')))

