vcasa = float(input('Valor da casa: '))
vsalario = float(input('Valor do salario: '))
vanos = int(input('Quantidade de anos: '))
mensal = vcasa/(vanos*12)
if vsalario < mensal:
    print('Emprestimo recursado')
else:
    print(('Emprestimo aprovado! Valor pagamento mensal é de: {:.2f}'.format(mensal)))
