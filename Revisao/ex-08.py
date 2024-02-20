""" 8) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu). """

atualano = int(input("Digite o ano atual: "))
anonasc  = int(input("Digite o ano de nascimento: "))
votar = atualano - anonasc
if votar >= 16:
    print("Poderá votar!")
else:
    print("Não poderá votar ainda!")