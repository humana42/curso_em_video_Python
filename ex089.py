ficha = list()
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1,nota2], media])
    res = input('Deseja continuar? [S/N]').strip().upper()
    if res in 'N':
        break
print('='*30)
print(f'{"No.":<4}{"NOME":<10}{"Média":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Deseja saber a nota de qual aluno? (999 interrompe) '))
    if opc == '999':
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'NOME: {ficha[opc][0]}    NOTAS: {ficha[opc][1]}')