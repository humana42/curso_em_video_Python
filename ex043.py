p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p /(a**2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade')
