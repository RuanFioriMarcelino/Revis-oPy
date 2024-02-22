v1 = int(input(f"Digite o valor 1: "))
v2 = int(input(f"Digite o valor 2: "))
if v2 == 0:
    while v2 == 0:
        v2 = int(input(f"Digite o valor 2: "))

print(f'A divisão de {v1} por {v2} é {v1/v2}')
