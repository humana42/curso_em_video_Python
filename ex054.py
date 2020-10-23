from datetime import date
menor = 0
maior = 0
ano = date.today().year
for c in range(0, 7):
    d = int(input('Digite o ano de nascimento: '))
    v = ano - d
    if v < 18:
       menor += 1
    else:
        maior += 1
print('Tem {} pessoas maior de idade e {} menor de idade'.format(maior, menor))
