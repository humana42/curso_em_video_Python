import random
ganho = 0
print('+-'*10)
print('Jogo Impar ou Par')
print('+-'*10)
while True:
    print('-'*20)
    escolha = input('Escolha I - para Impar ou P - para Par: ').strip().upper()[0]
    n = int(input('Digite um numero de 1 à 10: '))
    if 'P' != escolha != 'I':
        print('Error! Tente novamente!')
    pc = random.randint(1, 10)
    valor = (pc+n) % 2
    if valor == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    if escolha == 'P' and result == 'PAR':
        print('PAR!! \nVocê ganhou esta partida')
        ganho +=1
    elif escolha == 'I' and result == 'IMPAR':
        print('IMPAR!! Você ganhou essa partida')
    elif escolha == 'P' and result == 'IMPAR':
        print('PAR!! Você perdeu!!')
        break
    elif escolha == 'I' and result == 'IMPAR':
        print('IMPAR!! Você Perdeu!!')
print(f'O total de partidas ganha foi de {ganho} ')
