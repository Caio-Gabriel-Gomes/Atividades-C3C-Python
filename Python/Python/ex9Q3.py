hi = int(input("Informe a hora de início do jogo: "))
hf = int(input("Informe a hora de fim de jogo: "))

if (hi >= 1) and (hi <= 24) and (hf >= 1) and (hf <= 24):
    if (hf < hi):
        total = (24-hi) + hf
    elif (hf > hi):
        total = hf - hi
    else:
        total = 24
    print("Voçê jogou " + str(total) + " horas")
else:
    print("Você não pode jogar mais de 24 horas")


    