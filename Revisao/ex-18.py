def calcular(x):
    if x == "S":
        n1 = int(input(f"Digite o valor 1: "))
        if n1 < 0 or n1 > 10:
            while n1 < 0 or n1 > 10:
                n1 = int(input(f"Digite o valor 1: "))
        n2 = int(input(f"Digite o valor 2: "))
        if n2 < 0 or n2 > 10 :
            while n2 < 0 or n2 > 10 :
                n2 = int(input(f"Digite o valor 2: "))

        media = (n1 + n2) / 2
        print(f'Média calculada: {media}')
        x=input("Deseja calcular uma nova média(S/N)?")
        if x == "S":
            calcular("S")
        else:
            print("Beleza então!")

calcular("S")