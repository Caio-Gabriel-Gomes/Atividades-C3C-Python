aluno = {"nome":  input("Digite o seu nome: "),
         "nota1": float(input("Digite sua primeira nota: ")),
         "nota2": float(input("Digite sua segunda nota: ")),
         "media": 0}

aluno["media"] = (aluno["nota1"] + aluno["nota2"]) / 2

if aluno["media"] >= 7 :
    print(str(aluno["nome"]) + " parabéns você foi APROVADO! Com uma média " + str(aluno["media"]))
else: 
    print(str(aluno["nome"]) + " infelismente você foi REPROVADO! Sua média " + str(aluno["media"]) + " foi insuficiente")