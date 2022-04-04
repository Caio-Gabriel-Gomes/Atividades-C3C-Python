numeros = [0,0,0,0,0]

array = []
dicionario = {}

for i in range(5):
    numeros[i] = int(input("Digite um número: "))
    
    if (numeros[i] % 2) == 0:
        dicionario[numeros[i]] = numeros[i]
    else:
        array.append(numeros[i])
        
print("Todos os números são: " + str(numeros))
print("Os números impares são: " + str(array))
print("Os números pares são: " + str(dicionario.values()))