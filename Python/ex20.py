cont = 0
cont2 = 0
for i in range(5):
    numeros = float(input("Digite um numero: "))
    if (numeros >= 10) and (numeros <= 20):
        cont2 +=1
    else:
        cont +=1
print("Os numeros dentro do intervalo de 10 a 20 são:",cont2,cont)

    