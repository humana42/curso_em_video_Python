somaIdade = 0
idadeVelho = 0
qtdMulher = 0
for g in range(1,5):
    print('---- {} PESSOA ----'.format(g))
    nome = input('Digite o nome: ').upper().strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ').upper().strip()
    somaIdade = somaIdade + idade
    if sexo == 'MASCULINO':
        if g == 1:
            idadeVelho = idade
            nomeVelho = nome
        if idade > idadeVelho:
            nomeVelho = nome
    if sexo == 'FEMININO':
        if idade < 20:
            qtdMulher += 1
print('A media de idade do grupo é de {:.2f}'.format(somaIdade/4))
print('O homem mais velho é o {}'.format(nomeVelho))
print('Existe {} mulheres menores de 20 anos'.format(qtdMulher))
