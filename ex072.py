cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
        'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'desoito', 'dezenove', 'vinte')

while True:
        c = int(input('Digite um numero [0-20]: '))
        if 0 <= c <= 20:
                break
        print('Tente novamente!')
print(f'Numero por extenso é: {cont[c]}')
