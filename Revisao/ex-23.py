x = 0
cont = 0

for i in range (8):
    x += 1
    v = int(input(f"Digite o valor {x}: "))
    if v < 40:
        cont = cont + v

print(f'{cont} é o valor da soma!')