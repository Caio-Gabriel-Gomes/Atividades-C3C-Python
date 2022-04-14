from prettytable import PrettyTable

mercadoria = {}
valorE = []
def cadastroproduto(nome,qatual,qmin,qmax,valor):  
    if qatual > qmax: 
        print("A quantidade atual não pode ser maior que a quntidade maxima do estoque.")
    elif qatual <= 0 or qmin <= 0 or qmax <= 0 or valor <= 0:
        print("A quantidade não pode ser igual ou menor que zero.")
    else: 
        mercadoria[nome] = {'qatual': qatual, 'qmin': qmin, 'qmax': qmax, 'valoru': valor, 'valorTE': valor * qatual}
    valorE.append(mercadoria[nome]['valorTE'])
    return mercadoria
        
def estoque(mercadoria):  
    table1 = PrettyTable(['Produtos', 'Valor do protudo em estoque'])
    table2 = PrettyTable(['Produtos que precisam de reposição'])
    table3 = PrettyTable(['Valor total do estoque'])
    total = sum(valorE)
    for i in mercadoria:
        table1.add_row([i,mercadoria[i]['valorTE']])
        media =  (mercadoria[i]['qmax'] + mercadoria[i]['qmin']) / 2 
    print(table1) 
    if media > mercadoria[i]['qatual']: 
        table2.add_row([i])  
        print(table2)      
    table3.add_row([total/2]) 
    print(table3)
    
        