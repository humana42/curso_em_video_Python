frase = input('Digite a frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, ' ', inverso)
if junto == inverso:
    print('A frase é um Palimetro')
else:
    print('A frase não é um Palimetro')