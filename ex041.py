from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('Idade: {} \ncategoria: MIRIM'.format(idade))

elif idade > 9 and idade <= 14:
    print('Idade: {} \ncategoria: INFANTIL'.format(idade))

elif idade > 14 and idade <= 19:
    print('Idade: {} \ncategoria: JUNIOR'.format(idade))

elif idade > 19 and idade <= 25:
    print('Idade: {} \ncategoria: SENIOR'.format(idade))

elif idade > 25:
    print('Idade: {} \ncategoria: MASTER'.format(idade))

