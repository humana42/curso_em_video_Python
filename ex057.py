sexo = input('Digite o sexo [F/M]: ').upper().strip()[0]
while 'F' != sexo != 'M':
    print('Valo invalido Tente novamente!')
    sexo = input('Digite o sexo [F/M]: ').upper().strip()[0]
if sexo == 'F':
    print('O sexo digitado foi FEMININO')
if sexo == 'M':
    print('O sexo digitado foi MASCULINO')
