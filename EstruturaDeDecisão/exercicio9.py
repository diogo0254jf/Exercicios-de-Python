# 27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

fruta = input("Qual fruta deseja?")
quantidade = float(input("quantos kilos?"))
ValorFinal = 0
if fruta == "Morango":
	if quantidade <= 5:
		morango = 2.50
	else:
		morango = 2.20
		
	if quantidade > 8 or ValorFinal > 25.00:
		valorDesconto = (quantidade * morango) * 0.1
		ValorFinal = (quantidade * morango) - valorDesconto
	else:
		ValorFinal = quantidade * morango
elif fruta == "Maca":
	if quantidade <= 5:
		maca = 1.80
	else:
		maca = 1.50
		
	if quantidade > 8 or ValorFinal > 25.00:
		valorDesconto = (quantidade * maca) * 0.1
		ValorFinal = (quantidade * maca) - valorDesconto
	else:
		ValorFinal = quantidade * maca
else:
	print("Fruta não encontrada no sistema.")

if ValorFinal:
	print(f'Voce pagará {ValorFinal:.2f} por {quantidade} Kilos de {fruta}')