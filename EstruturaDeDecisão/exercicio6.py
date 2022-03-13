# 24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.


num1 = float(input("Digite o primeiro numero"))
num2 = float(input("Digite o segundo numero"))

operacao = input("Qual operação deseja fazer?")

if operacao == "+":
	resultado = num1 + num2
	if num1 % num2 == 0:
		print("numero par")
	else:
		print("numero ímpar")
		
	if num1 + num2 > 0:
		print("Numero positivo")
	else:
		print("Numero negativo")
		
		
	if type(resultado) == int:
		print("Inteiro")
	else:
		print("Decimal")	
		
	print('A soma deles são:',resultado)
else:
	print("Digite uma operação valida")