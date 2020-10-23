from datetime import date
def verif(ano):
    idade = date.today().year - ano
    if  60 > idade >= 18:
        print('Voto Obrigatorio!')
    elif idade < 16:
        print('Não vota')
    else:
        print('Voto facultativo ')

#programa
ano = int(input('Digite seu ano de nascimento: '))
verif(ano)