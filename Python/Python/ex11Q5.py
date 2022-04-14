atual = int(input("Digite a quantidade atual no estoque: "))
max = int(input("Digite a quantidade máxima no estoque: "))
min = int(input("Digite a quantidade minima no estoque: "))

media = (max+min)/2

if (atual >= media):
    print("A média foi",media,"não efetuar compra!")
else:
    print("A média foi",media,"efetuar compra!")