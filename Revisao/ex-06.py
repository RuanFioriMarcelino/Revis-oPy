maca = int(input("Quantidade de maçãs compradas: "))
if maca >= 12:
    print(f'Custo da compra: R${maca*1}')
else:
    print(f'Custo da compra: R$ {maca*1.30:.2f}')