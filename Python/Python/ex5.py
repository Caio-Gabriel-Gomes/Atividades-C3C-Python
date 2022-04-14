idade = int(input("Digite sua idade: "))

if (idade >= 18) and (idade < 70 ):
    print("Você é obrigado a votar")
elif (idade < 16):
    print("Você não pode votar")
else:
    print("Você tem a opção de votar")