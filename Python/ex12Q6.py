x = int(input("Digite um número: "))
y = int(input("digite um outro número: "))
z = (x*y)+5
print(z)
if z <= 0:
    resposta = "A"
elif z <= 100:
    resposta = "B"
else:
    resposta = "C"
print("Resultado final: %i. Resposta: %s" %(z,resposta))

# a) x = 5 e y = 10
#  z = 55 , Resposta = B

# b) x = 200 e y = 100
#  z = 20005 , Resposta = C

# c) x = 27 e y = -34
#  z = -913 , Resposta = A

# d) x = -8 e y = 40
#  z = -315 , Resposta = A

# e) x = 50 e y = 3
#  z = 155 , Resposta = C