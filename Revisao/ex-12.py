v1 = int(input("Digite o valor 1: "))
v2 = int(input("Digite o valor 2: "))
v3 = int(input("Digite o valor 3: "))
valores = []
if v1 != v2 and v1 != v3 and v2 != v3:
    valores.append(v1)
    valores.append(v2)
    valores.append(v3)
    valores.sort()
    print(f"Ordem crescente {valores}")

