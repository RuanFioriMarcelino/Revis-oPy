atualano = int(input("Digite o ano atual: "))
anonasc  = int(input("Digite o ano de nascimento: "))
votar = atualano - anonasc
if votar >= 16:
    print("Poderá votar!")
else:
    print("Não poderá votar ainda!")