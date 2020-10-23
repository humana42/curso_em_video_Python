dis = int(input('Digite a distancia da viagem: '))
if dis<=200:
    print('O custo da viagem é de R${:.2f}'.format(dis*0.5))
else:
    print('O custo da viagem é de R${:.2f}'.format(dis*0.45))
