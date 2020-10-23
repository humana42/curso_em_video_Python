dias = int(input('Qual a quantidade de dias alugado pelo carro: '))
km = float(input('Quantos KM o carro rodou:'))
valorDias = dias * 60
valorKM = km * 0.15
print('Preço por dias rodados é de R${:.2f} e o preço por KM é de R${:.2f}, o toral de ambos é de {:.2f}'.format(valorDias, valorKM, (valorDias+valorKM)))
