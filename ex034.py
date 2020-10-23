salario = float(input('Digite o salário: '))
if salario > 1250:
    print('Aumento de 10% no salário \nSalário atual: {:.2f}'.format(salario+(salario*0.1)))
else:
    print('O Aumento de 15% no salario \nSalário atual: {:.2f}'.format(salario+(salario*0.15)))