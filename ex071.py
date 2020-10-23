resto = nota50 = nota20 = nota10 = nota1 = 0
print('-+'*10)
print('CAIXA ELETRONICO')
print('-+'*10)
print('Sedulas permitida: R$50 , R$20 , R$10 , R$1')
saque = float(input('Valor de saque: R$'))
while saque != 0:
    if saque >= 50:
        saque -= 50
        nota50 += 1
    elif saque >= 20:
        saque -= 20
        nota20 += 1
    elif saque >= 10:
        saque -= 20
        nota10 += 1
    elif saque >= 1:
        saque -= 1
        nota1 += 1
if nota50 != 0:
    print(f'Total de notas R$50 {nota50}')
if nota10 != 0:
    print(f'Total de notas R$20 {nota20}')
if nota20 != 0:
    print(f'Total de notas R$10 {nota10}')
if nota1 != 0:
    print(f'Total de notas R$1 {nota1}')
