""" 7) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada. """

n1= float(input("Digite a nota 1 do aluno: "))
n2= float(input("Digite a nota 2 do aluno: "))
media = n1+n2 / 2
if media >= 6: 
    print("Parabéns! Aluno aprovado com média: ",media)
else:
    print("Que peninha! Aluno reprovado com média: ",media)