'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.'''

peso_pescado = float(input('Qual o peso dos peixes pescados : '))

if peso_pescado >= 50:
    multa = peso_pescado - 50
    multa = multa * 4
    print(f'O peso dos peixes excedeu o limite, a multa é de: {multa}')
else:
    print('O peso esta dentro do permitido, Obrigado')
