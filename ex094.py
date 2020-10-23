soma = media = 0
pessoa = dict()
cadastro = list()
while True:
    pessoa['nome'] = input('Nome:')
    while True:
        pessoa['sexo'] = input('Sexo: [F/M] ').strip().upper()
        if pessoa['sexo'] in 'FM':
            break
        else:
            print('    Valor errado!!! Tente novamente')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    escolha = input('Deseja continuar? [S/N] ').strip().upper()
    if escolha == 'N':
        cadastro.append(pessoa.copy())
        print('    FINALIZANDO CADASTRO...')
        print('-='*30)
        break
    if escolha != 'N' and escolha != 'S':
        print('    valor errado!!! Tente novamente')
    cadastro.append(pessoa.copy())
print(f'Ao todo tem {len(cadastro)} pessoas cadastradas')
media = soma/len(cadastro)
print(f'A media da soma das idades foi de {media:5.2f} anos')
print(f'As mulheres cadastradas foram:', end='')
for p in cadastro:
    if p['sexo'] in 'F':
        print(f'{p["nome"]};', end='')
print()
print('Lista de Pessoas que estão acima da media: ', end='')
for p in cadastro:
    if p['idade'] >= media:
        print(f'{p["nome"]};')

