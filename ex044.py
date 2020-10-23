p = float(input('Valor da peça: '))
e = int(input('Forma de pagamento: \n[1] A vista \n[2] Cartão 1x \n[3] Cartão 2x \n[4] Cartão 3x ou mais\n'))
if e == 1:
    print(('A forma de pagamento escolhida tem 10% de desconto, o valor total a ser pago é de R${:.2f}'.format(p-(p*0.1))))
elif e ==2:
    print(('A forma de pagamento escolhida tem 5% de desconto, o valor total a ser pago é de R${:.2f}'.format(p-(p*0.05))))
elif e == 3:
    print('A forma de pagamento escolhida não possui desconto, o valor total a ser pago é de R${:.2f}'.format(p))
elif e == 4:
    print('Aforma escolhida de epagamento gera 20% de juros, o valor a ser pago é de R${:.2f}'.format(p+(p*0.2)))
else:
    print('Comando invalido, tente novamente!')