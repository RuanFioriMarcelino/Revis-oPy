""" 14) Ler dois valores e imprimir uma das três mensagens a seguir:
‘Números iguais’, caso os números sejam iguais
‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
‘Segundo maior’, caso o segundo seja maior que o primeiro.
 """

v1 = int(input("Digite o valor 1: "))
v2 = int(input("Digite o valor 2: "))

if v1 == v2:
    print("Números iguais")
elif v1 > v2:
    print("Valor 1 é maior que o valor 2")
elif v2 > v1:
    print("Valor 2 é maior que o valor 1")