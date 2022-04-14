h1 = int(input("Digite a idade do primeiro homem: "))
h2 = int(input("Digite a idade do segundo homem: "))
m1 = int(input("Digite a idade da primeira mulher: "))
m2 = int(input("Digite a idade da segunda mulher: "))

if (h1>h2) and (m1>m2):
    soma = h1 + m2
    produto = h2 * m1
elif (h1>h2) and (m2>m1):
    soma = h1 + m1
    produto = h2 * m2
elif (h2>h1) and (m1>m2):
    soma = h2 + m2
    produto = h1 * m1
else:
    soma = h2 + m1
    produto = h1 * m2

print("A soma do homem mais velho com a mulher mais nova é: ", soma)
print("O produto do homem mais novo com a mulher mais velha é: ", produto)
