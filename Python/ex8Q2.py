array = [0,0,0]

for i in range(3):
    array[i] = int(input("Digite um número: "))

if (array[0] < array[1]) and (array[0] < array[2]) and (array[1] < array[2]):
    array = [array[0], array[1], array[2]]
    
elif (array[0] < array[1]) and (array[0] < array[2]) and (array[2] < array[1]):
    array = [array[0], array[2], array[1]]
    
elif (array[1] < array[0]) and (array[1] < array[2]) and (array[2] < array[0]):
    array = [array[1], array[2], array[0]]
    
elif (array[1] < array[0]) and (array[1] < array[2]) and (array[0] < array[2]):
    array = [array[1], array[0], array[2]]

elif (array[2] < array[0]) and (array[2] < array[1]) and (array[0] < array[1]):
    array = [array[2], array[0], array[1]]

else:
    array = [array[2], array[1], array[0]]
    

print("Os numeros em ordem crescente: ",array)



    