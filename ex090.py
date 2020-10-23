dicionario = dict()
dicionario['nome'] = input('NOME: ')
dicionario['media'] = float(input('MEDIA: '))
if dicionario['media'] >= 7.5:
    dicionario['situacao'] = 'Aprovado'
elif 5 < dicionario['media'] <7.5:
    dicionario['situacao'] = 'Recuperação'
elif dicionario['media'] <= 5:
    dicionario['situacao'] = 'Reprovado'
print('='*30)
for k, v in dicionario.items():
    print(f'{k} é igual a {v}')