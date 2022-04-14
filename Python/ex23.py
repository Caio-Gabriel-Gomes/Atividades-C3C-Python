from pacote.modulo import *

c = input("Deseja cadastrar um produto? ")

while c == 'Sim':
    nome = input("Nome do produto: ")
    qatual = int(input("Quantidade atual no estoque: "))
    qmin = int(input("Quantidade minima: "))
    qmax = int(input("Quantidade maxima: "))
    valor = int(input("Valor unitario do produto: "))
    cadastroproduto(nome,qatual,qmin,qmax,valor)
    c = input("Deseja cadastrar outo produto? ")
    v = cadastroproduto(nome,qatual,qmin,qmax,valor)
estoque(v)
    
    






     
