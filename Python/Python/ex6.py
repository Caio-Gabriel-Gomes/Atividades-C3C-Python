horas = float(input("Quantas horas foram trabalhadas: "))

salariohora = float(input("Salario por hora: "))

if horas > 160:
    salario = (160 * salariohora) + ((horas-160) * (salariohora * 1.5))
else:
    salario = horas * salariohora
    
print(salario)