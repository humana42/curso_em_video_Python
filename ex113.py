def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except:
            print(f'\033[0;31mERRO: Por favor digite um numero inteiro valido!\033[m')
        else:
            break
    return i
def leiaReal(msg):
    while True:
        try:
            r = float(input(msg))
        except:
            print(f'\033[0;31mERRO: Por favor digite um numero real valido!\033[m')
        else:
            break
    return r
inteiro =leiaInt('Digite um numero inteiro: ')
real =leiaReal('Digite um numero Real: ')
print(f'O numero inteiro digitado foi {inteiro} e o real foi {real:.2f}')
