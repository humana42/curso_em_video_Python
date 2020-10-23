prod = float(input('Digite o valor do produto: '))
desc = prod-(prod*0.05)
print('O valor do produto é de R${:.2f} com desconto ficou em R${:.2f}'.format(prod, desc))
