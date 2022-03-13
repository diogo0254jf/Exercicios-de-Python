# 26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

gasolina = 2.50
alcool = 1.90

tipocombustivel = input("Selecione o tipo de combustivel: A-álcool ou G-gasolina\n")
quantidadeAbastecida = float(input("Quantos litros gostaria de abastecer?"))
Valorfinal = 0
if tipocombustivel == "A-álcool":
	if quantidadeAbastecida <= 20:
		Valorfinal = quantidadeAbastecida * alcool
		Valorfinal -= alcool * quantidadeAbastecida * 3 / 100
	else:
		Valorfinal = quantidadeAbastecida * alcool
		Valorfinal -= alcool * quantidadeAbastecida * 5 / 100
elif tipocombustivel == "G-gasolina":
	if quantidadeAbastecida <= 20:
		Valorfinal = quantidadeAbastecida * gasolina
		Valorfinal -= gasolina * quantidadeAbastecida * 4 / 100
	else:
		Valorfinal = quantidadeAbastecida * gasolina
		Valorfinal -= gasolina * quantidadeAbastecida * 4 / 100

else:
	print("Tipo de combustivel não suportado")

print(f'o valor a ser pago é de: {Valorfinal} por {quantidadeAbastecida} litros de {tipocombustivel}')