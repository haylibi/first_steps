import random
number = random.randint(1,1000)
n = 0
tentativa = 0
while n!= number:
	tentativa=tentativa+1
	n=int(input('Numero:',))
	if n<number:
		print('O seu numero é menor que o selecionado')
	else:
		print('O  seu numero é maior que o selecionado')
print('Adivinhou, o numero era ', number)
print('tentativas=', tentativa)
