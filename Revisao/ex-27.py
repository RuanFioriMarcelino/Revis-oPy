codigo = int(input("Digite o código do empregado: "))
anonasc= int(input("Digite o ano de nascimento do empregado: "))
anoingr= int(input("Digite o ano de ingresso do empregado na empresa: "))

anocontr = 2024 - anoingr
idade = 2024 - anonasc

if idade >= 65:
    print("Requerer aposentadoria!")

elif anocontr >= 30:
    print("Requerer aposentadoria!")

elif idade >= 60 and anocontr >= 25:
    print("Requerer aposentadoria!")
else:
    print("Não requerer aposentadoria!")

print(f'Ano de contribuição {anocontr}\nIdade do empregado: {idade}')