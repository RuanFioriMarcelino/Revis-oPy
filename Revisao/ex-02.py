brancos =   int(input("Digite quantos votos em brancos: "))
nulos =     int(input("Digite quantos votos nulos: "))
validos =   int(input("Digite quantos votos válidos: "))
eleitores = brancos + nulos + validos

if brancos < 0:
    print("Inválido")
else:
    print(f'Porcentagem de votos em brancos {(brancos/eleitores)*100}')
if nulos < 0:
    print("Inválido")
else:
    print(f'Porcentagem de votos em brancos {(nulos/eleitores)*100}')
if validos < 0:
    print("Inválido")
else:
    print(f'Porcentagem de votos em brancos {(validos/eleitores)*100}')