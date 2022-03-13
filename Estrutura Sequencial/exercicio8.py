'''Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

rendimento = int(input('Qual o rendimento da lata ? '))
altura = int(input('Qual a altura da parede ? '))
largura = int(input('Qual a largura da parede ? '))

def calculo_tinta ():
    area = altura * largura
    total = area / rendimento
    print(f'Voce precisa de {total} latas de tintas ')

    
calculo_tinta()
