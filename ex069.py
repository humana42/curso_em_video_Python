qtd = qtdIdade = qtdMulher = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    sexo = input('DIGITE UM SEXO: [F/M] ').strip().upper()[0]
    idade = int(input('DIGITE A IDADE: '))
    if 'M' != sexo != 'F':
        print('Opção incorreta! TENTE NOVAMENTE')
    else:
        qtd += 1
        if idade >= 18:
            qtdIdade += 1
        if sexo == 'M' and idade > 20:
            qtdMulher +=1
        resp = input('DESEJA CONTINUAR? [S/N]').strip().upper()
        if resp == 'N':
            break
print(f'O Cadastro possui {qtd} pessoas')
print(f'A quantidade de pessoas maior de idade é de {qtdIdade}')
print(f'A quantidade de Mulheres maior de 20 anos é de {qtdMulher}')
