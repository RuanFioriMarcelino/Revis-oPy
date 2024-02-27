valores = "valor no intervalo!"
x = 0
cont = 0

for i in range (10):
    x += 1
    v = int(input(f"Digite o valor {x}: "))
    if v >= 10 and v <= 20:
        cont += 1

if cont > 1:
    valores = "valores no intervalo!"
print(f'{cont} {valores}')