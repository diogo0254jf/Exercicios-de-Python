# 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

notaum = float(input("Digite sua primeira nota\n"))
notadois = float(input("Digite sua segunda nota\n"))

media = (notaum + notadois) / 2
resposta = "neutro"

if media == 10.0:
	resposta = "Aprovado com Distinção"
elif media >= 7.0: 
	resposta = "Aprovado"
else:
	resposta = "Reprovado"
	
print("voce foi:",resposta)