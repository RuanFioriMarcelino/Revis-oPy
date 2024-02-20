""" 9) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total. """

s_fixo = float(input("Digite o sálario fixo do funcionário: "))
vendas = float(input("Digite o valor das vendas efetuadas pelo vendedor: "))
comissao3 = vendas * 0.03
if vendas >= 1.500:
    comissao5 = (vendas - 1.500) * 0.05
    t_salario = s_fixo + comissao3 + comissao5
print("Sálario total do funcionário é de R$",t_salario)