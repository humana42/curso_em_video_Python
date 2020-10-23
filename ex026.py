frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.upper().count('A')))
print('A letra A aparece na posição {} pela primeira vez'.format(frase.upper().find('A')+1))
print('A letra A aparece na posição {} pela ultima vez'.format(frase.upper().rfind('A')+1))
