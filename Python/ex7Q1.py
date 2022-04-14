aluno = {"nome":  input("Digite o seu nome: "),
         "nota1": float(input("Digite sua primeira nota: ")),
         "nota2": float(input("Digite sua segunda nota: ")),
         "media": 0}

aluno["media"] = (aluno["nota1"] + aluno["nota2"]) / 2

if (aluno["nota1"] > 0 and aluno["nota1"] < 10 and aluno["nota2"] > 0 and aluno["nota2"] < 10):
    if aluno["media"] >= 7 :
        print(str(aluno["nome"]) + " parabéns você foi APROVADO! Com uma média " + str(aluno["media"]))
    else: 
        print(str(aluno["nome"]) + " infelismente você foi REPROVADO! Sua média " + str(aluno["media"]) + " foi insuficiente")
else:
    print("Digite notas de 0 a 10")        