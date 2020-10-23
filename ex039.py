from datetime import date
atual = date.today().year
nasc = int(input('qual sua data de nascimento? '))
calc = atual - nasc
if calc < 18:
    print('Ainda não é hora de se alistar')
elif calc > 18:
    print(('Já passou a hora de se alistar'))
else:
    print('Está na hora de se alistar')
