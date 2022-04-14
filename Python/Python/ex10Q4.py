salario = int(input("Dígite o seu salario fixo: "))
venda = int(input("Dígite o valor das suas vendas: "))

if (venda <= 1500):
    comissao = 0.03 * venda
else:
    comissao = (0.03 * 1500) + (venda - 1500) * 0.05

salarioTotal = salario + comissao

print("O seu salario total foi R$ " + str(salarioTotal))
    