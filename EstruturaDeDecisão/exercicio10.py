# 28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

escolhaCarne = input("Escolha os tipos de carne entre\n					  Até 5 Kg           Acima de 5 Kg\nFile Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg\nAlcatra         R$ 5,90 por Kg          R$ 6,80 por Kg\nPicanha         R$ 6,90 por Kg          R$ 7,80 por Kg\n")
tipoPagamento = input("Qual tipo de pagamento?\nColoque que atende o atende!\n[1] = Cartao Tabajara\n[2] = Dinheiro\n[3] = cartão de credito\n[4] = cartão de debito\n")
quantidadeKilo = 0
if escolhaCarne == "File Duplo":
	if tipoPagamento == "1":
		quantidadeKilo = float(input(f'quantos quilos de {escolhaCarne} voce gostaria de levar?'))
		if quantidadeKilo > 5:
			valorCarne = 5.80
		else:
			valorCarne = 4.90
		valorDesconto = (quantidadeKilo * valorCarne) * 0.5
		ValorFinal = (quantidadeKilo * valorCarne) - valorDesconto
			
	else:
		if quantidadeKilo > 5:
			valorCarne = 5.80
		else:
			valorCarne = 4.90	
			
		quantidadeKilo = float(input(f'quantos quilos de {escolhaCarne} voce gostaria de levar?'))
		ValorFinal = quantidadeKilo * valorCarne
		
elif escolhaCarne == "Alcatra":
	if tipoPagamento == "1":
		quantidadeKilo = float(input(f'quantos quilos de {escolhaCarne} voce gostaria de levar?'))
		if quantidadeKilo > 5:
			valorCarne = 6.80
		else:
			valorCarne = 5.90		
		valorDesconto = (quantidadeKilo * valorCarne) * 0.5
		ValorFinal = (quantidadeKilo * valorCarne) - valorDesconto
	else:
		if quantidadeKilo > 5:
			valorCarne = 6.80
		else:
			valorCarne = 5.90	
			
		quantidadeKilo = float(input(f'quantos quilos de {escolhaCarne} voce gostaria de levar?'))
		ValorFinal = quantidadeKilo * valorCarne
elif escolhaCarne == "Picanha":
	if tipoPagamento == "1":
		quantidadeKilo = float(input(f'quantos quilos de {escolhaCarne} voce gostaria de levar?'))
		if quantidadeKilo > 5:
			valorCarne = 7.80
		else:
			valorCarne = 6.90		
		valorDesconto = (quantidadeKilo * valorCarne) * 0.5
		ValorFinal = (quantidadeKilo * valorCarne) - valorDesconto
	else:
		if quantidadeKilo > 5:
			valorCarne = 5.80
		else:
			valorCarne = 4.90	
			
		quantidadeKilo = float(input(f'quantos quilos de {escolhaCarne} voce gostaria de levar?'))
		ValorFinal = quantidadeKilo * valorCarne
	
else:
	print("Voce só pode escolher uma das opçoes acima")

if ValorFinal:
	if tipoPagamento == "1":
		tipoPagamento = "Cartao Tabajara"
	elif tipoPagamento == "2":
		tipoPagamento = "Dinheiro"
	elif tipoPagamento == "3":
		tipoPagamento = "cartão de crédito"
	elif tipoPagamento == "4":
		tipoPagamento = "cartão de débito"
	if valorDesconto:
		valorDesconto = (quantidadeKilo * valorCarne) * 0.5
		print(f'voce comprou {quantidadeKilo} Kg de {escolhaCarne}\nValor o kg: {valorCarne}\nMetodo de pagamento: {tipoPagamento}\nPagou um total de: {ValorFinal}\nValor Desconto: 5%')
	else:
		print(f'voce comprou {quantidadeKilo} Kg de {escolhaCarne}\nValor o kg: {valorCarne}\nMetodo de pagamento: {tipoPagamento}\nPagou um total de: {ValorFinal}')