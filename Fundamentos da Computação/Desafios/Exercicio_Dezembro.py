#Faça um programa em Python que permita ao usuário informar a idade de quantas pessoas ele desejar.
#Para isso, você pode perguntar a ele, quantas idades serão informadas. Após isso o programa deve calcular:
#- A média de idade das pessoas maiores de idade informadas. 
#- O percentual de pessoas considerando as faixas de idade: 
#        0-17 anos
#        18 a 35 anos
#        35 a 50 anos
#        50 a 65 anos
#        maiores de 65 anos.
#Lembrete: a soma dos percentuais das faixas deve totalizar 100%.

#Ao final, o programa deve exibir esses resultados.
continuar = True

while continuar:
    n_idades = int(input("Por gentileza, quantas idades deseja informar? "))

    soma_maior_18 = 0
    cont = 0

    faixa_0_17 = 0
    faixa_18_35 = 0
    faixa_35_50 = 0
    faixa_50_65 = 0
    faixa_65m = 0
    
    for x in range(0, n_idades):
        idade = int(input("Por gentileza, digite a idade desejada: "))
        if idade >= 18:
            soma_maior_18 = soma_maior_18 + idade
            cont = cont + 1

        if idade < 18:
            faixa_0_17 += 1
        elif idade >= 18 and idade < 35:
            faixa_18_35 += 1
        elif idade >= 35 and idade < 50:
            faixa_35_50 += 1
        elif idade >= 50 and idade < 65:
            faixa_50_65 += 1
        else:
            faixa_65m += 1

           

        
    print(f"A média das idades maiores ou iguais a 18 é {soma_maior_18 / cont}.\n")
    print("A faixa 0-17 anos possui ", (faixa_0_17)*100/n_idades, "%")
    print("A faixa 18 a 35 anos possui ", (faixa_18_35)*100/n_idades, "%")
    print("A faixa 35 a 50 anos possui ", (faixa_35_50)*100/n_idades, "%")
    print("A faixa 50 a 65 anos possui ", (faixa_50_65)*100/n_idades, "%")
    print("A faixa + 65 anos possui ", (faixa_65m)*100/n_idades, "%")
    


    
    resposta = int(input("Deseja continuar? (1 - sim, 0 - Não) "))
    if resposta != 1:
        continuar = False
