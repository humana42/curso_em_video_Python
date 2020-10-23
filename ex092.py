from datetime import date
dados = {}
dados['nome'] = input('Nome: ')
dados['idade'] = date.today().year - (int(input('Ano nascimento: ')))
ctps = int(input('Numero da carteira de trabalho: [caso não tenha 0] '))
if ctps != 0:
    dados['ctps'] = ctps
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Remuneração: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao']+35) - date.today().year)
print('-+'*30)
for k, v in dados.items():
    print(f'{k} tem valor {v}')

