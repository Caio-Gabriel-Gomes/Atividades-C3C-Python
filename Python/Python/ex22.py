def media(v1, v2):
    acu = 0
    cont = 0
    if v1 > v2:
        for i in range(v2+1,v1,1):
            acu += 1
            cont += 1
    else:
        for i in range(v1+1,v2,1):
            acu += i
            cont += 1
    return acu / cont
n1 = int(input("Digite o valor inicial da contagem: "))
n2 = int(input("Digite o valor final da contagem: "))
print(media(n1,n2))
 
    
