n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
opcao=0
while opcao != 5:
    print('-----CALCULADORA-----')
    opcao = int(input('escolha uma opção: \n[1]SOMA \n[2]MULTIPLICAR \n[3]MAIOR NUMERO \n[4]NOVOS NUMEROS \n[5]SAIR \n'))
    print('-' * 20)
    if opcao == 1:
        soma = n1+n2
        print('A soma dos numeros são: {}'.format(soma))
    elif opcao == 2:
        mult = n1*n2
        print('A multiplicação dos dois numeros é de: {}'.format(mult))
    elif opcao == 3:
        if n1>n2:
            print('O maior numero é: {}'.format(n1))
        else:
            print('O menor numero é: {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite um novo valor para o primeiro numero: '))
        n2 = int(input('Digite um novo valor para o segundo numero: '))
    elif opcao == 5:
        print('Encerrando...')
