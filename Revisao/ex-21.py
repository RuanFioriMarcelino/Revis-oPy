valores = "valor negativo!"
x = 0
cont = 0

for i in range (10):
    x += 1
    v = int(input(f"Digite o valor {x}: "))
    if v < 0:
        cont += 1

if cont > 1:
    valores = "valores negativos!"
print(f'{cont} {valores}')