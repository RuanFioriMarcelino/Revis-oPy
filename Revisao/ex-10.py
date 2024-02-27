conta = int(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo da conta: "))
debito= float(input("Digite o débito da conta: "))
credito=float(input("Digite o crédito da conta: "))
saldoatual = saldo - debito + credito

if saldoatual > 0:
    print("Saldo positivo! R$",saldoatual)
elif saldoatual == 0:
    print("Saldo Neutro. R$",saldoatual)
else:
    print("Saldo Negativo! R$",saldoatual)