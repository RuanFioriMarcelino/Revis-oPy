combustivel = input("Gasolina (G) ou Álcool(A)?").upper()
litros      = float(input("Litros abastecidos: "))

if combustivel == "G":
    if litros <= 20:
        valor = ((litros * 3.30) - (litros * 3.30) * 0.04)
        print(f'Valor a ser pago R${valor}')
    if litros > 20:
        valor = ((litros * 3.30) - (litros * 3.30) * 0.06)
        print(f'Valor a ser pago R${valor}')

elif combustivel == "A":
    if litros <= 20:
        valor = ((litros * 2.90) - (litros * 2.90) * 0.03)
        print(f'Valor a ser pago R${valor}')
    if litros > 20:
        valor = ((litros * 2.90) - (litros * 2.90) * 0.05)
        print(f'Valor a ser pago R${valor}')