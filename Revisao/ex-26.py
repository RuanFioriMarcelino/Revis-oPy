n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1+n2+n3) / 3
mediaapro = (n1 + n2 * 2 + n3 * 3 + media) / 7

if mediaapro >= 9:
    conceito = "A"
elif mediaapro >= 7.5 and mediaapro < 9:
    conceito = "B"
elif mediaapro >= 6 and mediaapro < 7.5:
    conceito = "C"
if mediaapro < 6:
    conceito = "D"

print("Nota conceito: ",conceito)